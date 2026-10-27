import json
class Cliente:
    def __init__(self, id, nome, email, fone):
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__fone = fone

    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_email(self):
        return self.__email
    def get_fone(self):
        return self.__fone

    def set_nome(self, nome):
        self.__nome = nome
    def set_email(self, email):
        self.__email = email
    def set_fone(self, fone):
        self.__fone = fone

    def __str__(self):
        return (
            f"ID: {self.__id} | "
            f"Nome: {self.__nome} | "
            f"Email: {self.__email} | "
            f"Telefone: {self.__fone}"
        )

class ClienteDAO:
    objetos = []

    @classmethod
    def Inserir(cls, obj):
        cls.objetos.append(obj)
        cls.Salvar()

    @classmethod
    def Listar(cls):
        return cls.objetos

    @classmethod
    def Listar_Id(cls, id):
        for cliente in cls.objetos:
            if cliente.get_id() == id:
                return cliente
        return None

    @classmethod
    def Atualizar(cls, obj):
        for i, cliente in enumerate(cls.objetos):
            if cliente.get_id() == obj.get_id():
                cls.objetos[i] = obj
                cls.Salvar()
                return

    @classmethod
    def Excluir(cls, obj):
        if obj in cls.objetos:
            cls.objetos.remove(obj)
            cls.Salvar()

    @classmethod
    def Abrir(cls):
        try:
            with open("clientes.json", "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)

                cls.objetos = [
                    Cliente(
                        item["id"],
                        item["nome"],
                        item["email"],
                        item["fone"]
                    )
                    for item in dados
                ]

        except FileNotFoundError:
            cls.objetos = []

        except json.JSONDecodeError:
            cls.objetos = []

    @classmethod
    def Salvar(cls):
        dados = []

        for cliente in cls.objetos:
            dados.append({
                "id": cliente.get_id(),
                "nome": cliente.get_nome(),
                "email": cliente.get_email(),
                "fone": cliente.get_fone()
            })

        with open("clientes.json", "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)

class UI:

    @staticmethod
    def Menu():
        print("\n===== SISTEMA DE CLIENTES =====")
        print("1 - Listar clientes")
        print("2 - Inserir cliente")
        print("3 - Atualizar cliente")
        print("4 - Excluir cliente")
        print("0 - Finalizar")

        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            return -1

    @staticmethod
    def Cliente_Listar():
        clientes = ClienteDAO.Listar()

        if not clientes:
            print("Nenhum cliente cadastrado.")
            return

        for cliente in clientes:
            print(cliente)

    @staticmethod
    def Cliente_Inserir():
        try:
            id = int(input("ID: "))
        except ValueError:
            print("O ID deve ser um número inteiro.")
            return

        if ClienteDAO.Listar_Id(id) is not None:
            print("Já existe um cliente com esse ID.")
            return

        nome = input("Nome: ")
        email = input("Email: ")
        fone = input("Telefone: ")

        cliente = Cliente(id, nome, email, fone)
        ClienteDAO.Inserir(cliente)

        print("Cliente cadastrado com sucesso!")

    @staticmethod
    def Cliente_Atualizar():
        try:
            id = int(input("Digite o ID do cliente: "))
        except ValueError:
            print("O ID deve ser um número inteiro.")
            return

        cliente = ClienteDAO.Listar_Id(id)

        if cliente is None:
            print("Cliente não encontrado.")
            return

        print("Deixe vazio o campo que não deseja alterar.")

        nome = input("Novo nome: ")
        email = input("Novo email: ")
        fone = input("Novo telefone: ")

        if nome:
            cliente.set_nome(nome)

        if email:
            cliente.set_email(email)

        if fone:
            cliente.set_fone(fone)

        ClienteDAO.Atualizar(cliente)
        print("Cliente atualizado com sucesso!")

    @staticmethod
    def Cliente_Excluir():
        try:
            id = int(input("Digite o ID do cliente: "))
        except ValueError:
            print("O ID deve ser um número inteiro.")
            return

        cliente = ClienteDAO.Listar_Id(id)

        if cliente is None:
            print("Cliente não encontrado.")
            return

        ClienteDAO.Excluir(cliente)
        print("Cliente excluído com sucesso!")

    @staticmethod
    def Main():
        ClienteDAO.Abrir()

        while True:
            opcao = UI.Menu()

            if opcao == 1:
                UI.Cliente_Listar()

            elif opcao == 2:
                UI.Cliente_Inserir()

            elif opcao == 3:
                UI.Cliente_Atualizar()

            elif opcao == 4:
                UI.Cliente_Excluir()

            elif opcao == 0:
                ClienteDAO.Salvar()
                print("Sistema finalizado!")
                break

            else:
                print("Opção inválida.")
UI.Main()
