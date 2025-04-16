arq = open('registrados.txt', 'a')
print('Olá, aqui você pode adicionar uma nova conta!')
nome_usuario = input('Digite o nome de usuário: ')
senha_usuario = input('Digite a sua senha: ')

arq.write(f"{nome_usuario}:{senha_usuario}\n")
print('Cadastro realizado com sucesso!\n')
arq.close()

arq = open('registrados.txt', 'r')
registrados = arq.readlines()
max_tentativas = 3
tentativas = 0
login_valido = False

while tentativas < max_tentativas and not login_valido:
    print('\nEfetue o seu login')
    nome_login = input('Digite o seu nome de usuario: ')
    senha_login = input('Digite a sua senha: ')

    for linha in registrados:
        usuario_armazenado, senha_armazenada = linha.strip().split(':')
        if nome_login == usuario_armazenado and senha_login == senha_armazenada:
            login_valido = True
            break

    if login_valido:
        print(f'\nBem-vindo, {nome_login}!')
    else:
        tentativas += 1
        restantes = max_tentativas - tentativas
        print(f'\nUsuário ou senha incorretos. Tentativas restantes: {restantes}')

arq.close()

if not login_valido:
    print('\nVocê excedeu o número máximo de tentativas. Tente novamente mais tarde.')