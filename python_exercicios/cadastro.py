from datetime import date

variavel = {}

print("Seja Bem-Vindos")

print("Você pode cadastrar quantas variáveis quiser. Digite 'sair' para finalizar.")

while True:
    
    primeiro_campo = input("Digite o nome da variável: ")

    if primeiro_campo.lower() == 'sair':
        break

    valor = input(f"Digite o valor para {primeiro_campo}: ")
    
    data = date.today()

    variavel[primeiro_campo] = {"valor": valor, "atual": data}

print("\nVariáveis cadastradas:")

for nome, dados in variavel.items():
    
    print(f"{dados['atual']} - {nome} = {dados['valor']}")

print("\nFim do programa! Obrigado por utilizar.")
