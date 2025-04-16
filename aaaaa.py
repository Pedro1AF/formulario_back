# Verifica se um usuário já existe no arquivo
def usuario_existe(nome):
    try:
        with open('registrados.txt', 'r') as arq:
            for linha in arq:
                usuario_salvo = linha.split(':')[0]  # Pega apenas o nome (antes do ':')
                if usuario_salvo == nome:
                    return True
        return False
    except FileNotFoundError:
        return False  # Se o arquivo não existe, não há usuários cadastrados

# --- Modo de CADASTRO (com validação) ---
print('Olá, aqui você pode adicionar uma nova conta!')
nome_usuario = input('Digite o nome de usuário: ')

if usuario_existe(nome_usuario):
    print('\nERRO: Este nome de usuário já está em uso. Tente outro.')
else:
    senha_usuario = input('Digite a sua senha: ')
    with open('registrados.txt', 'a') as arq:
        arq.write(f"{nome_usuario}:{senha_usuario}\n")
    print('\nCadastro realizado com sucesso!\n')

# --- Modo de LOGIN (original) ---
arq = open('registrados.txt', 'r')
print('Efetue o seu login')
nome_login = input('Digite o seu nome de usuário: ')
senha_login = input('Digite a sua senha: ')

login_valido = False
registrados = arq.readlines()

for linha in registrados:
    usuario, senha = linha.strip().split(':')
    if nome_login == usuario and senha_login == senha:
        login_valido = True
        break

if login_valido:
    print(f'\nBem-vindo, {nome_login}!')
else:
    print('\nUsuário ou senha incorretos. Verifique e tente novamente.')

arq.close()