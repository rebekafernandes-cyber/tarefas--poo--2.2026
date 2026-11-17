from service import Service

class UI:
    @staticmethod
    def main():
        op = -1
        while op != 0:
            op = UI.menu()
            if op == 1: UI.cliente_inserir()
            if op == 2: UI.cliente_listar()
            if op == 3: UI.cliente_atualizar()
            if op == 4: UI.cliente_excluir()
            if op == 5: UI.categoria_inserir()
            if op == 6: UI.categoria_listar()
            if op == 7: UI.categoria_atualizar()
            if op == 8: UI.categoria_excluir()
            if op == 9: UI.produto_inserir()
            if op == 10: UI.produto_listar()
            if op == 11: UI.produto_atualizar()
            if op == 12: UI.produto_excluir()
            if op == 13: UI.produto_reajustar()
            if op < 0 or op > 13: print("Opção inválida")
    @staticmethod
    def menu():
        print()
        print("1 - Inserir cliente")
        print("2 - Listar clientes")
        print("3 - Atualizar cliente")
        print("4 - Excluir cliente")
        print("5 - Inserir categoria")
        print("6 - Listar categorias")
        print("7 - Atualizar categoria")
        print("8 - Excluir categoria")
        print("9 - Inserir produto")
        print("10 - Listar produtos")
        print("11 - Atualizar produto")
        print("12 - Excluir produto")
        print("13 - Reajustar preço dos produtos")
        print("0 - Finalizar")
        return int(input("Informe a opção: "))
    @staticmethod
    def cliente_inserir():
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        fone = input("Informe o fone: ")
        Service.cliente_inserir(nome, email, fone)
    @staticmethod
    def cliente_listar():
        for c in Service.cliente_listar(): print(c)
    @staticmethod
    def cliente_atualizar():
        UI.cliente_listar()
        id = int(input("Informe o id do cliente a ser atualizado: "))
        nome = input("Informe o novo nome: ")
        email = input("Informe o novo e-mail: ")
        fone = input("Informe o novo fone: ")
        Service.cliente_atualizar(id, nome, email, fone)
    @staticmethod
    def cliente_excluir():
        UI.cliente_listar()
        id = int(input("Informe o id do cliente a ser excluído: "))
        Service.cliente_excluir(id)
    @staticmethod
    def categoria_inserir():
        descricao = input("Informe a descrição da categoria: ")
        Service.categoria_inserir(descricao)
    @staticmethod
    def categoria_listar():
       for c in Service.categoria_listar(): print(c)
    @staticmethod
    def categoria_atualizar():
        UI.categoria_listar()
        id = int(input("Informe o id da categoria a ser atualizada: "))
        descricao = input("Informe a nova descrição: ")
        Service.categoria_atualizar(id, descricao)
    @staticmethod
    def categoria_excluir():
        UI.categoria_listar()
        id = int(input("Informe o id da categoria a ser excluída: "))
        Service.categoria_excluir(id)
    @staticmethod
    def produto_inserir():
        descricao = input("Informe a descrição do produto: ")
        preco = float(input("Informe o preço: "))
        estoque = int(input("Informe o estoque: "))
        UI.categoria_listar()
        idCategoria = int(input("Informe o id da categoria: "))
        Service.produto_inserir(descricao, preco, estoque, idCategoria)
    @staticmethod
    def produto_listar():
        for p in Service.produto_listar(): print(p)
    @staticmethod
    def produto_atualizar():
        UI.produto_listar()
        id = int(input("Informe o id do produto a ser atualizado: "))
        descricao = input("Informe a nova descrição: ")
        preco = float(input("Informe o novo preço: "))
        estoque = int(input("Informe o novo estoque: "))
        UI.categoria_listar()
        idCategoria = int(input("Informe o id da categoria: "))
        Service.produto_atualizar(id, descricao, preco, estoque, idCategoria)
    @staticmethod
    def produto_excluir():
        UI.produto_listar()
        id = int(input("Informe o id do produto a ser excluído: "))
        Service.produto_excluir(id)
    @staticmethod
    def produto_reajustar():
        percentual = float(input("Informe o percentual (positivo para reajuste e negativo para promoção): "))
        Service.produto_reajustar(percentual)
        print("Preços atualizados.")

UI.main()
