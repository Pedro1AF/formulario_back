# Senha de acesso
chave = "2345"

# Lista para armazenar os clientes (cada cliente é um dicionário)
clientes = []

while True:
    entrada = input("Digite a senha: ")
    if entrada == chave:
        print("Acesso concedido!")
    else:
        print("Acesso negado")
        break

    while True:
        print("\nOpções:")
        print("1. Adicionar novo cliente")
        print("2. Buscar cliente por nome")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            # Adicionar novo cliente
            nome = input("Digite o nome do cliente: ")
            idade = input("Digite a idade do cliente: ")
            cpf = input("Digite o CPF do cliente: ")
            endereco = input("Digite o endereço do cliente: ")
            telefone = input("Digite o telefone do cliente: ")

            cliente = {
                "nome": nome,
                "idade": idade,
                "cpf": cpf,
                "endereco": endereco,
                "telefone": telefone
            }

            clientes.append(cliente)
            print("Cliente adicionado com sucesso!")

        elif opcao == "2":
            # Buscar cliente por nome
            busca_nome = input("Digite o nome do cliente que deseja buscar: ")
            encontrado = False

            for cliente in clientes:
                if cliente["nome"] == busca_nome:
                    print("\nInformações do cliente:")
                    print(f"Nome: {cliente['nome']}")
                    print(f"Idade: {cliente['idade']}")
                    print(f"CPF: {cliente['cpf']}")
                    print(f"Endereço: {cliente['endereco']}")
                    print(f"Telefone: {cliente['telefone']}")
                    encontrado = True
                    break

            if not encontrado:
                print("Cliente não encontrado.")

        elif opcao == "3":
            # Sair do programa
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")
