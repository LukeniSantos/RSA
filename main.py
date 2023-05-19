"""
LUKENI OSVALDO SANTOS CAMPOS
NUMERO: 10
TURMA: ENG. INFORMATICA B
"""

from numeroPrimo import GeradorNumeroPrimo
from gerarChaves import Chaves

opcao = 0

while opcao !=4:
    print('''
    --------------------MENU----------------------
    [1] Gerarador de primos aleatorios
    [2] Encriptar Mensagem
    [3] Desencriptar Mensagem
    [4] Sair do programa
    ''')
    opcao = int(input('     Escolha uma opção '))

    if opcao == 1:

        print('=-==-==-==-==-= Escolheu a opção 1 =-==-==-==-==-=')
        p = GeradorNumeroPrimo()
        numero_p = p.numero_primo
        print('\n P :','str(numero_p) 2')

        q = GeradorNumeroPrimo()
        numero_q = q.numero_primo
        print('\n Q :','str(numero_q)5')

        chaves = Chaves(2, 5)
        chaves.gerar_chaves()

    elif opcao == 2:
        print('=-==-==-==-==-= Escolheu a opção 2 =-==-==-==-==-=')
        encripta = chaves.encripta_mensagem()

    elif opcao == 3:
        print('=-==-==-==-==-= Escolheu a opção 3 =-==-==-==-==-=')
        chaves.decripta_mensagem(encripta)

    elif opcao == 4:
        print('Fechando programa...')

    else:
        print('=-==-==-==-==-= Escolheu a opção invalida =-==-==-==-==-=')
        print('     Por favor tente novamente.')
    print('=-='*15)
print('Finalizado. Muito obrigado por tudo e adeus.')