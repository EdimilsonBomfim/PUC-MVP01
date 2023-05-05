from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

#from model import Base, Comentario
from model import Base

class Ferramenta(Base):
    __tablename__ = 'ferramenta'

    id = Column("pk_ferramenta", Integer, primary_key=True)
    descricao_longa = Column(String(140), unique=True, nullable=False)
    descricao_curta =  Column(String(50), unique=True)
    nome_curto_fornecedor = Column(String(30))
    quantidade_estoque = Column(Integer)
    valor_unitario_venda = Column(Float)
    valor_unitario_compra = Column(Float)
    data_inclusao = Column(DateTime, default=datetime.now())

    # Definição do relacionamento entre o ferramenta e o comentário.
    # Essa relação é implicita, não está salva na tabela 'ferramenta',
    # mas aqui estou deixando para SQLAlchemy a responsabilidade
    # de reconstruir esse relacionamento.
    #comentarios = relationship("Comentario")

    def __init__(self, descricao_longa: str, descricao_curta: str,
                 nome_curto_fornecedor: str, quantidade_estoque: int,
                 valor_unitario_venda: float, valor_unitario_compra: float,
                 data_inclusao: Union[DateTime, None] = None):
        """
        Cadastrar uma ferramenta

        Arguments:
            descricao_longa: Descrição da ferramenta utilizado pelo fronecedor.
            descricao_curta: Descrição abrevida da ferramenta  
            nome_curto_fornecedor: Nome curto do fornecedor
            quantidade_estoque: quantidade atual em estoque
            valor_unitario_venda: Indica o valor da ferramenta a ser vendido
            valor_unitario_compra: Indica o valor de compra da ferramenta
            data_inclusao: data de quando o produto foi inserido na base
        """
        self.descricao_longa = descricao_longa
        self.descricao_curta = descricao_curta
        self.nome_curto_fornecedor = nome_curto_fornecedor
        self.quantidade_estoque = quantidade_estoque
        self.valor_unitario_venda = valor_unitario_venda
        self.valor_unitario_compra = valor_unitario_compra
        #self.data_inclusao = Column(DateTime, default=datetime.now())

        # se não for informada, será o data exata da inserção no banco
        if data_inclusao:
            self.data_insercao = data_inclusao

   