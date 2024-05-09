# import random

# chute_aleatorio = random.randint(1,2)
# # condição simples
# if chute_aleatorio == 2:
#     print('acertei',chute_aleatorio)

# import random

# chute_aleatorio = random.randint(1,10)
# # condição composta
# if chute_aleatorio == 2:
#     print('acertei', chute_aleatorio)
# else:
#     print('errei', chute_aleatorio)


#Jogo # condição composta

# import random

# aleatorio = random.randint(1,10)

# meu_chute = int(input('digite seu chute'))
# #condição verdadeira
# if meu_chute == aleatorio:
#     print('show de bola', aleatorio)
#     #condição falsa
# else:
#     print('Tente novamente', aleatorio)



#DESAFIO
#SISTEMA DE SENHAS 
# 1 - O COMPUTADOR CRIA UMA SENHA ALEATÓRIA
# 2 - VOCE DIGITA SENHA DE ACESSO
# 3 - VERIFICAR SE O USUARIO PODE ACESSAR O SISTEMA



import random

senha_sist = random.randint(10000,10001)

senha_usuario = int(input('Digite a senha :'))

if senha_usuario == senha_sist:
    print('Você está sendo logado',senha_sist)
else:
    print('Senha incorreta',senha_sist)

