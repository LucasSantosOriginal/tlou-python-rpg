from time import sleep
import random

print(''' 
Você acaba de acordar depois de um sono profundo
em uma casa abandonada no seu acampamento improvisado.
Acordando aos poucos você fica sentada na cama, parece que você dormiu por anos...

''')

Nome = input('Qual o seu nome mesmo? ')
print(f'{Nome} você sente suas costas doendo\n, percebe que precisa descansar mais um pouco')
print()
print('...')
sleep(1)
print('......')
sleep(1)

print('Agora olhando com mais atenção no chão do seu acampamento improvisado\n você percebe rastros de sangue ')
print()
print('O que você vai fazer?')
print('''
    [1] Procurar sua arma
    [2] Seguir o sangue
    [3] Continuar sentada esperando alguma coisa acontecer
''')
escolha = input('O que você faz? ')

if escolha == '1':
    print('Você procura e não acha, '
          'mas acredita que está na sua mochila')
    print('''
    [1] Procurar na mochila (Role o dado)
    [2] Ignorar
    ''')
    escolha = input('faça sua escolha: ')

    if escolha == '1':
        dado = random.randint(1, 20)  # Corrigido para randint
        print("Valor do dado foi de...", dado)
        if dado > 10:
            print("Você achou a arma e ela está com 5 munições")
            print('...')
            sleep(1)
            print('voce ouve um barulho de algo batendo na porta do porão.')
            print('''
            O que você faz?
            [1] Vai em direção a porta 
            [2] nada
            ''')
            escolha = input ('O que você faz? ')
            if escolha == '1':
                dado = random.randint(1,20)
                print ('rolando um dado...', dado)
                if dado > 12:
                    print('A PORTA ABRE COM UM GRANDE ESTRONDO! E UM INFECTADO PULA EM VOCE')
        else:
            print("Você achou sua arma e ela está com apenas 2 munições")
            print('...')
            sleep(1)
            print('voce ouve um barulho de algo batendo na porta do porão.')
            print('''
            O que você faz?
            [1] Vai em direção a porta 
            [2] nada
            ''')
            escolha = input('O que você faz? ')
            if escolha == '1':
                dado = random.randint(1, 20)
                print('rolando um dado...', dado)
                if dado < 12:
                    print('a porta continua batendo...')
elif escolha == '2':
    print ('Ao seguir o sangue você vê uma porta que você nunca tinha visto antes '
           '\n ela parece seguir em direção ao porão')
    print()
    print('...')
    sleep(1)
    print('O que você faz?')
    print('''
    [1] Você volta para o quarto 
    [2] Entrar no porão
    [3] Abrir inventário 
    ''')

