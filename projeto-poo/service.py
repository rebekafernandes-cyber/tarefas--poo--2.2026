from models.cliente import Cliente
from models.clienteDAO import ClienteDAO
from models.categoria import Categoria
from models.categoriaDAO import CategoriaDAO
from models.produto import Produto
from models.produtoDAO import ProdutoDAO
from datetime import datetime
import json 

class Service:
    @staticmethod
    def cliente_inserir(nome, email, fone, senha):
        lista = ClienteDAO().listar()
        id = 1
        for obj in lista:
            if obj.get_id() >= id: id = obj.get_id() + 1
        c = Cliente(id, nome, email, fone, senha)
        ClienteDAO().inserir(c)
    @staticmethod
    def cliente_listar():
        return ClienteDAO().listar()
    @staticmethod
    def cliente_listar_id(id):
        return ClienteDAO().listar_id(id)
    @staticmethod
    def cliente_atualizar(id, nome, email, fone, senha):
        c = Cliente(id, nome, email, fone, senha)
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
    @staticmethod
    def cliente_criar_admin():
        for c in Service.cliente_listar():
            if c.get_email() == "admin": return
        Service.cliente_inserir("admin", "admin", "fone", "1234")
    @staticmethod
    def cliente_autenticar(email, senha):
        for c in Service.cliente_listar():
            if c.get_email() == email and c.get_senha() == senha:
                return {"id": c.get_id(), "nome": c.get_nome()}
        return None 
    @staticmethod
    def pedido_listar():
        try:
            arquivo = open("pedidos.json", mode="r", encoding="utf-8")
            pedidos = json.load(arquivo)
            arquivo.close()
            return pedidos
        except FileNotFoundError:
            return []

    @staticmethod
    def pedido_comprar(usuario_id, usuario_nome, carrinho):
        if len(carrinho) == 0:
            raise ValueError("O carrinho está vazio.")
        produtos = ProdutoDAO()
        itens = []
        total = 0
        for item in carrinho:
            produto = produtos.listar_id(int(item["produto_id"]))
            quantidade = int(item["quantidade"])
            if produto == None:
                raise ValueError("Um produto do carrinho não existe mais.")
            if quantidade <= 0 or produto.estoque < quantidade:
                raise ValueError("Estoque insuficiente para: " + produto.descricao)
            itens.append({
                "produto_id": produto.id,
                "descricao": produto.descricao,
                "preco": produto.preco,
                "quantidade": quantidade,
                "subtotal": produto.preco * quantidade
            })
            total += produto.preco * quantidade

        for item in itens:
            produto = produtos.listar_id(item["produto_id"])
            produto.estoque -= item["quantidade"]
            produtos.atualizar(produto)

        pedidos = Service.pedido_listar()
        id = 1
        for pedido in pedidos:
            if pedido["id"] >= id: id = pedido["id"] + 1
        pedido = {
            "id": id,
            "cliente_id": usuario_id,
            "cliente_nome": usuario_nome,
            "data": datetime.now().strftime("%d/%m/%Y %H:%M"),
            "itens": itens,
            "total": total
        }
        pedidos.append(pedido)
        arquivo = open("pedidos.json", mode="w", encoding="utf-8")
        json.dump(pedidos, arquivo, indent=2, ensure_ascii=False)
        arquivo.close()
        return pedido

    @staticmethod
    def minhas_compras(usuario_id):
        return [p for p in Service.pedido_listar() if p["cliente_id"] == usuario_id]

    @staticmethod
    def listar_vendas():
        return Service.pedido_listar()  