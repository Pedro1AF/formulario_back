print ("Seja Bem-Vindos")

print ("Voce pode cadatrar quantas variaveis quiser.digite 'sair' para finalizar")

while True:
    nome = input("digite o nome da variavel:")
   
    if nome.lower() == 'sair':
        break
    valor = input(f"digite o valor para {nome}: ")
   
    variavel[nome] = valor
       
print("n/variaveis cadastradas:")
for nome, valor in variavel.items():
    print(f"{nome} = {valor}")
           
print("\nFim do programa! Obrigado por utilizar.")