from models.categoria import Categoria
import json

class CategoriaDAO:
    def __init__(self):
        self.__arquivo = "categorias.json"
        self.__objetos = []
        self.__abrir()
    def inserir(self, obj):
        self.__objetos.append(obj)
        self.__salvar()
    def listar(self):
        return self.__objetos
    def listar_id(self, id):
        for obj in self.__objetos:
            if obj.get_id() == id: return obj
        return None
    def atualizar(self, obj):
        aux = self.listar_id(obj.get_id())
        if aux != None:
            self.__objetos.remove(aux)
            self.__objetos.append(obj)
            self.__salvar()
    def excluir(self, id):
        aux = self.listar_id(id)
        if aux != None:
            self.__objetos.remove(aux)
            self.__salvar()
    def __abrir(self):
        try:
            arquivo = open(self.__arquivo, mode="r")
            objetos_json = json.load(arquivo)
            arquivo.close()
            self.__objetos = []
            for obj in objetos_json:
                self.__objetos.append(Categoria.from_json(obj))
        except FileNotFoundError:
            pass
    def __salvar(self):
        arquivo = open(self.__arquivo, mode="w")
        json.dump(self.__objetos, arquivo, default=Categoria.to_json, indent=2)
        arquivo.close()