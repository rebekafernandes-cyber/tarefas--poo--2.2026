class Cliente:
    def __init__(self, id, nome, email, fone, senha):
        self.id = id
        self.nome = nome
        self.email = email
        self.fone = fone
        self.senha = senha
    def __str__(self):
        return f"{self.id} - {self.nome} - {self.email} - {self.fone} - {self.senha}"
    def set_id(self, id):
        self.id = id
    def get_id(self):
        return self.id
    def set_nome(self, nome):
        self.nome = nome
    def get_nome(self):
        return self.nome
    def set_email(self, email):
        self.email = email
    def get_email(self):
        return self.email
    def set_fone(self, fone):
        self.fone = fone
    def get_fone(self):
        return self.fone
    def set_senha(self, senha):
        self.senha = senha
    def get_senha(self):
        return self.senha
    def to_json(self):
        dic = {}
        dic["id"] = self.id
        dic["nome"] = self.nome
        dic["email"] = self.email
        dic["fone"] = self.fone
        dic["senha"] = self.senha
        return dic
    @staticmethod
    def from_json(dic):
        return Cliente(dic["id"], dic["nome"], dic["email"], dic["fone"], dic["senha"])
