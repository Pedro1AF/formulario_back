usuarios_cadastrados = {
    "": {
        "Nome": "",
        "Email": "",
        "Senha": "",
        "Telefone": "",
        "Saldo": 1500
    }
}

def cadastrar_usuario():
    print("\n=== CADASTRO ===")
    nome = input("Nome: ")
    cpf = input("CPF (apenas números): ")
    email = input("Email: ")
    senha = input("Senha: ")
    telefone = input("Telefone: ")
    
    usuarios_cadastrados[cpf] = {
        "Nome": nome,
        "Email": email,
        "Senha": senha,
        "Telefone": telefone,
        "Saldo": 0 
    }
    print("\nCadastro realizado com sucesso!")
    return cpf 

def fazer_login():
    print("\n=== LOGIN ===")
    cpf = input("CPF: ")
    senha = input("Senha: ")
    
    if cpf in usuarios_cadastrados and usuarios_cadastrados[cpf]["Senha"] == senha:
        print(f"\nBem-vindo(a), {usuarios_cadastrados[cpf]['Nome']}!")
        return cpf
    else:
        print("\nCPF ou senha incorretos.")
        return None

def pagina_inicial(cpf_usuario):
    while True:
        print("\n=== PÁGINA INICIAL ===")
        print(f"Saldo: R${usuarios_cadastrados[cpf_usuario]['Saldo']:.2f}")
        print("\nOpções:")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Simulador de Investimentos")
        print("4 - Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            valor = float(input("Valor para depositar: R$"))
            usuarios_cadastrados[cpf_usuario]["Saldo"] += valor
            print(f"\nDepósito de R${valor:.2f} realizado!")
        elif opcao == "2":
            valor = float(input("Valor para sacar: R$"))
            if valor <= usuarios_cadastrados[cpf_usuario]["Saldo"]:
                usuarios_cadastrados[cpf_usuario]["Saldo"] -= valor
                print(f"\nSaque de R${valor:.2f} realizado!")
            else:
                print("\nSaldo insuficiente.")
        elif opcao == "3":
            valor = float(input("Valor para investir: R$"))
            tempo = int(input("Quanto tempo irá durar? (em meses) "))
            juros = float(input("Qual vai ser a taxa de juros? "))
            investimento = valor * (juros / 100) * tempo
            print(f"\nO valor será de R${investimento:.2f}")
                    
        elif opcao == "4":
            print("\nSaindo...")
            break
        else:
            print("\nOpção inválida.")


while True:
    print("\n=== Bem vindo ao Banco Monedas!===\n")
    print("1 - Fazer login")
    print("2 - Cadastrar-se")
    print("3 - Sair")
    
    escolha = input("Escolha uma opção: ")
    
    if escolha == "1":
        cpf_logado = fazer_login()
        if cpf_logado:
            pagina_inicial(cpf_logado)
    elif escolha == "2":
        cpf_logado = cadastrar_usuario()
        pagina_inicial(cpf_logado) 
    elif escolha == "3":
        print("\nAté logo!")
        break
    else:
        print("\nOpção inválida. Tente novamente.")
