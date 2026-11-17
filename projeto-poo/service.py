from models.cliente import Cliente
from models.clienteDAO import ClienteDAO
from models.categoria import Categoria
from models.categoriaDAO import CategoriaDAO
from models.produto import Produto
from models.produtoDAO import ProdutoDAO

class Service:
    @staticmethod
    def cliente_inserir(nome, email, fone):
        lista = ClienteDAO().listar()
        id = 1
        for obj in lista:
            if obj.get_id() >= id: id = obj.get_id() + 1
        c = Cliente(id, nome, email, fone)
        ClienteDAO().inserir(c)
    @staticmethod
    def cliente_listar():
        return ClienteDAO().listar()
    @staticmethod
    def cliente_listar_id(id):
        return ClienteDAO().listar_id(id)
    @staticmethod
    def cliente_atualizar(id, nome, email, fone):
        c = Cliente(id, nome, email, fone)
        ClienteDAO().atualizar(c)
    @staticmethod
    def cliente_excluir(id):
        ClienteDAO().excluir(id)

    @staticmethod
    def categoria_inserir(descricao):
        lista = CategoriaDAO().listar()
        id = 1
        for obj in lista:
            if obj.get_id() >= id: id = obj.get_id() + 1
        c = Categoria(id, descricao)
        CategoriaDAO().inserir(c)
    @staticmethod
    def categoria_listar():
        return CategoriaDAO().listar()
    @staticmethod
    def categoria_listar_id(id):
        return CategoriaDAO().listar_id(id)
    @staticmethod
    def categoria_atualizar(id, descricao):
        c = Categoria(id, descricao)
        CategoriaDAO().atualizar(c)
    @staticmethod
    def categoria_excluir(id):
        CategoriaDAO().excluir(id)

    @staticmethod
    def produto_inserir(descricao, preco, estoque, idCategoria):
        lista = ProdutoDAO().listar()
        id = 1
        for obj in lista:
            if obj.get_id() >= id: id = obj.get_id() + 1
        p = Produto(id, descricao, preco, estoque, idCategoria)
        ProdutoDAO().inserir(p)
    @staticmethod
    def produto_listar():
        return ProdutoDAO().listar()
    @staticmethod
    def produto_listar_id(id):
        return ProdutoDAO().listar_id(id)
    @staticmethod
    def produto_atualizar(id, descricao, preco, estoque, idCategoria):
        p = Produto(id, descricao, preco, estoque, idCategoria)
        ProdutoDAO().atualizar(p)
    @staticmethod
    def produto_excluir(id):
        ProdutoDAO().excluir(id)
    @staticmethod
    def produto_reajustar(percentual):
        dao = ProdutoDAO()
        for p in dao.listar():
            preco = p.preco * (1 + percentual / 100)
            p.set_preco(preco)
            dao.atualizar(p)
