class Categoria:
    def __init__(self, id, descricao):
        self.id = id
        self.descricao = descricao
    def __str__(self):
        return f"{self.id} - {self.descricao}"
    def set_id(self, id):
        self.id = id
    def get_id(self):
        return self.id
    def to_json(self):
        dic = {}
        dic["id"] = self.id
        dic["descricao"] = self.descricao
        return dic
    @staticmethod
    def from_json(dic):
        return Categoria(dic["id"], dic["descricao"])