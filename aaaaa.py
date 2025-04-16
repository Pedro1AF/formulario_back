arq = open('registrados.txt', 'a')
print('Olá, aqui você pode adicionar uma nova conta!')
nome_usuario = input('Digite o nome de usuário: ')

arq.write('{}\n'.format(nome_usuario))
'''
Adição da constante \n new line
Uma vez que write não o adiciona automaticamente
'''

print('Cadastro realizado com sucesso!\n')
arq.close() #O arquivo é fechado do modo de adição para ser aberto
            #posteriormente no modo de leitura

arq = open('registrados.txt') #abrindo no modo de leitura
print('Efetue o seu login')
nome_login = input('Digite o seu nome de usuario: ')

registrados = arq.readlines()
if nome_login + '\n' in registrados:
    print('Bem vindo, {}!'.format(nome_login))
else:
    print('Você deve ter digitado seu nome de usuario errado, por favor verifique.')
arq.close()