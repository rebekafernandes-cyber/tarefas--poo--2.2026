class Produto:
    def __init__(self, id, descricao, preco, estoque, idCategoria):
        self.id = id
        self.descricao = descricao
        self.preco = preco
        self.estoque = estoque
        self.idCategoria = idCategoria
    def __str__(self):
        return f"{self.id} - {self.descricao} - R$ {self.preco:.2f} - Estoque: {self.estoque} - Categoria: {self.idCategoria}"
    def set_id(self, id):
        self.id = id
    def get_id(self):
        return self.id
    def set_preco(self, preco):
        self.preco = preco
    def to_json(self):
        dic = {}
        dic["id"] = self.id
        dic["descricao"] = self.descricao
        dic["preco"] = self.preco
        dic["estoque"] = self.estoque
        dic["idCategoria"] = self.idCategoria
        return dic
    @staticmethod
    def from_json(dic):
        return Produto(dic["id"], dic["descricao"], dic["preco"], dic["estoque"], dic["idCategoria"])