from pydantic import BaseModel
from typing import Optional, List
from model.ferramenta import Ferramenta

class FerramentaSchema(BaseModel):
    """ Define como uma nova ferramenta deve ser representado na operação de inclusão
    """
    descricao_longa: str = "Vonder Jogo De Ferramentas Com 110 Peças Caixa Aberta"
    descricao_curta: Optional[str] = "Jogo de ferramentas com maleltas"
    nome_curto_fornecedor: Optional[str] = "Vonder"
    quantidade_estoque: int = 10
    valor_unitario_venda: float = 95.20
    valor_unitario_compra: float = 50.11

class FerramentaBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita com base na informação da  descrição curta da ferramenta.
    """
    id: int = 1
 
class FerramentaBuscaNomeCurtoSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita com base na informação da  descrição curta da ferramenta.
    """
    descricao_curta: str = "Maleta Completa"

class ListagemferramentasSchema(BaseModel):
    """ Define como uma listagem de ferramentas será retornada.
    """
    ferramentas: List[FerramentaSchema]

#Metodo para apresentas todas as ferramentas
def apresenta_ferramentas(ferramentas: List[Ferramenta]):
    print( "Chamando apresenta_resultados")

    result = []
    for ferramenta in ferramentas:
        result.append({
            "id": ferramenta.id,
            "descricao_longa": ferramenta.descricao_longa,
            "descricao_curta": ferramenta.descricao_curta,
            "nome_curto_fornecedor": ferramenta.nome_curto_fornecedor,
            "quantidade_estoque": ferramenta.quantidade_estoque,
            "valor_unitario_venda": ferramenta.valor_unitario_venda,
            "valor_unitario_compra": ferramenta.valor_unitario_compra,
        } )

    return {"ferramentas": result}


class FerramentaViewSchema(BaseModel):
    """ Define como um ferramenta será retornado: ferramenta + comentários.
    """
    id: int = 1
    descricao_longa: str = "Vonder Jogo De Ferramentas Com 110 Peças Caixa Aberta"
    descricao_curta: Optional[str] = "Jogo de ferramentas com maleltas"
    nome_curto_fornecedor: Optional[str] = "Vonder"
    quantidade_estoque: int = 10
    valor_unitario_venda: float = 95.20
    valor_unitario_compra: float = 50.11

class FerramentaDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    nome_curto_fornecedor: str

class ferramentaUpdateSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de alteração
    """
    descricao_longa: str
    descricao_curta: str
    nome_curto_fornecedor: str
    quantidade_estoque: int
    valor_unitario_venda: float
    valor_unitario_compra: float


def apresenta_ferramenta(ferramenta: Ferramenta):
    """ Retorna uma representação do ferramenta seguindo o schema definido em
        ferramentaViewSchema.
    """
    return {
        "id": ferramenta.id,
        "descricao_longa": ferramenta.descricao_longa,
        "descricao_curta": ferramenta.descricao_curta,
        "nome_curto_fornecedor": ferramenta.nome_curto_fornecedor,
        "quantidade_estoque": ferramenta.quantidade_estoque,
        "valor_unitario_venda": ferramenta.valor_unitario_venda,
        "valor_unitario_compra": ferramenta.valor_unitario_compra,
    }
