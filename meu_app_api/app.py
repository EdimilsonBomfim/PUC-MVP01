from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

# from model import Session, Ferramenta, Comentario
from model import Session, Ferramenta
from logger import logger
from schemas import *
from flask_cors import CORS

info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação",
               description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
ferramenta_tag = Tag(name="Ferramenta", 
               description="Adição, visualização e remoção de ferramentas à base")

@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')

@app.post('/ferramenta', tags=[ferramenta_tag],
          responses={"200": FerramentaViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_ferramenta(form: FerramentaSchema):
    """Adiciona uma novo ferramenta à base de dados

    Retorna uma representação dos ferramentas e comentários associados.
    """
    ferramenta = Ferramenta(
        descricao_longa=form.descricao_longa,
        descricao_curta=form.descricao_curta,
        nome_curto_fornecedor=form.nome_curto_fornecedor,
        quantidade_estoque=form.quantidade_estoque,
        valor_unitario_venda=form.valor_unitario_venda,
        valor_unitario_compra=form.valor_unitario_compra)

    logger.debug(
        f"Adicionando ferramenta de nome: '{ferramenta.descricao_curta}'")
    try:
        # criando conexão com a base
        session = Session()
        # adicionando ferramenta
        session.add(ferramenta)
        # efetivando o camando de adição de novo item na tabela
        #print(session)
        session.commit()
        logger.debug(
            f"Adicionado ferramenta de nome: '{ferramenta.descricao_curta}'")
        return apresenta_ferramenta(ferramenta), 200
    
    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "o nome da ferramenta já cadastrada no banco de dados :/"
        logger.warning(
            f"Erro ao adicionar ferramenta '{ferramenta.descricao_curta}', {error_msg}")
        return {"mesage": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(
            f"Erro ao adicionar ferramenta '{ferramenta.descricao_curta}', {error_msg}")
        return {"mesage": error_msg}, 400

@app.get('/ferramentas', tags=[ferramenta_tag],
         responses={"200": ListagemferramentasSchema, "404": ErrorSchema})
def get_ferramentas():

    print(Ferramenta.descricao_curta)
    """Faz a busca de todas ferramenta cadastradas no banco de dados

    Retorna uma representação da listagem de ferramentas.
    """
    print("teste1")
    logger.debug(f"Coletando ferramentas ")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    ferramentas = session.query(Ferramenta).all()

    if not ferramentas:
        # se não há ferramentas cadastrados
        return {"ferramentas": []}, 200
    else:
        logger.debug(f"%d ferramentas econtradas" % len(ferramentas))
        
    # retorna a representação de ferramenta
    return apresenta_ferramentas(ferramentas), 200

@app.get('/ferramenta', tags=[ferramenta_tag],
         responses={"200": FerramentaViewSchema, "404": ErrorSchema})
def get_ferramenta(query: FerramentaBuscaSchema):
    """Faz a busca por ferramenta a partir do codigo id informando
    """
    ferramenta_id = query.id
    logger.debug(f"Coletando dados sobre ferramenta #{ferramenta_id}")

    # criando conexão com a base
    session = Session()

    # fazendo a busca
    ferramenta = session.query(Ferramenta).filter(Ferramenta.id == ferramenta_id).first()

    if not ferramenta:
        # Gera log de alerta quando a ferramenta não foi encontrado
        error_msg = "ferramenta não encontrado no banco de dados :/"
        logger.warning( f"Erro ao buscar a ferramenta - Id: '{ferramenta_id}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"ferramenta econtrado: '{ferramenta.descricao_curta}'")

        # retorna a representação de ferramenta
        return apresenta_ferramenta(ferramenta), 200

@app.delete('/ferramenta', tags=[ferramenta_tag],
            responses={"200": FerramentaDelSchema, "404": ErrorSchema})
def del_ferramenta(query: FerramentaBuscaSchema):
    """Deleta uma ferramenta a partir do id iinformado

    Retorna uma mensagem de confirmação da remoção da ferramenta no banco de dados.
    """
    ferramenta_id = query.id
    str_ferramenta_id = str(ferramenta_id)
    logger.debug(f"Coletando dados sobre ferramenta #{str_ferramenta_id}")
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Ferramenta).filter(
        Ferramenta.id == ferramenta_id).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Ferramenta excluida do banco - Id: #{str_ferramenta_id}")
        return {"mesage": "Ferramenta foi removida do banco de dados", "id": str_ferramenta_id}
    else:
        # se o ferramenta não foi encontrado
        error_msg = "ferramenta não encontrado na no banco de dados :/"
        logger.warning( f"Erro na tentativa de excluir a ferramenta do banco de dados: #'{str_ferramenta_id}', {error_msg}")
        return {"mesage": error_msg}, 404

# @app.put('/ferramenta', tags=[ferramenta_tag],
#          responses={"200": ferramentaUpdateSchema, "404": ErrorSchema})
# def update_ferramenta(query: FerramentaBuscaSchema, form: FerramentaUpdateSchema):
#     """Edita ferramenta a partir do codigo id informado

#     Retorna uma mensagem de confirmação da edição.
#     """
#     ferramenta_id = query.id
#     str_ferramenta_id = str(ferramenta_id)
#     logger.debug(f"Alterando os dados da ferramenta #{str_ferramenta_id}")

#     # criando conexão com a base
#     session = Session()

#     # capturando o dados e fazendo alteracao
#     dados_editar = session.query(Ferramenta).filter(Ferramenta.id == ferramenta_id).first()

#     dados_editar.descricao_longa = form.descricao_longa
#     dados_editar.descricao_curta = form.descricao_curta
#     dados_editar.nome_curto_fornecedor = form.nome_curto_fornecedor
#     dados_editar.quantidade_estoque = form.quantidade_estoque
#     dados_editar.valor_unitario_venda = form.valor_unitario_venda
#     dados_editar.valor_unitario_compra = form.valor_unitario_compra

#     session.commit()

#     if dados_editar:
#         # retorna a representação da mensagem de confirmação
#         logger.debug(f"Alteracao concluida do id da ferramenta #{str_ferramenta_id}")
#         return {"mesage": "Ferramenta alterada com sucesso", "id": Stringpi}
#     else:
#         # se o produto não foi encontrado
#         error_msg = "Id da ferramenta informado, não encontrada na base :/"
#         logger.warning(
#             f"Erro na tentativa de realizar alteração na ferramenta, id #'{str_ferramenta_id}', {error_msg}")
#         return {"mesage": error_msg}, 404
#     return apresenta_produto(dados_editar), 200