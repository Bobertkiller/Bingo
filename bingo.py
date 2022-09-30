import datetime as dt 
import random as r 

def intro():
    Intro = '''
    Bem Vindo Ao/Welcome to 
     _     _                   
    | |__ (_)_ __   __ _  ___  
    | '_ \| | '_ \ / _` |/ _ \ 
    | |_) | | | | | (_| | (_) |
    |_.__/|_|_| |_|\__, |\___/ 
                   |___/       

    Versão Atual / Current Version: 0.5

    Isso é um trabalho feito para minha Faculdade, pretendo posteriormente melhorar o código e fazer um bingo normal com colunas nas cartelas
    This is a College homework that I have developed and I pretend to further improve the code
    '''
    return Intro
#essa função registra o tempo e horario e formata para uma saida de data em Ingles seguindo um padrão determinado

def pega_tempo():
    data_atual = dt.datetime.now()
    string_tempo = data_atual.strftime('%A, %B %d, %Y, %H:%M:%S')
    return string_tempo
#essa função sorteia a cartela dentre do arquivo Cartelas.txt 

def sorteia_cartela():
    a = open('Cartelas.txt', 'r', encoding='utf-8')
    b = a.readlines()
    c = [0]*4
    for i in range(4):
        d=b[r.randint(0,len(b)-1)]
        d = d.strip('\n')
        c[i] = d.split(',')
        for j in range(5):
            c[i][j] = int(c[i][j])
    a.close()
    return c, 0

#Essa função Devolve a cartela atual do jogador e as demais cartelas

def dev_cartela(c, atual):
    print(f'Cartela ATUAL:\n{c[atual]}\n')
    print('As demais cartelas:\n')
    for i in range(4):
        if i == atual:
            pass
        else:
            print(f'{c[i]}\n')
#Essa função permite ao jogador a trocar a cartela dele     
#    
def troca_cartela(c,atual):
    print('Favor responder a pergunta com S, s , Sim, sim ou enter para seguir adiante')
    a = input('Você deseja trocar de cartela? ')
    a = a.lower()
    if a == 's' or a == 'sim':
        while True:
            for i in range(4):
                if i == atual:
                    pass
                else:
                    print(f'Cartela {i+1}:\n{c[i]}\n')
            b = int(input('Favor Escolha uma das cartelas apresentadas: '))
            b -= 1
            if b == 0:
                print('Opção Invalida, escolha outra cartela')
            else:
                break
        return b
    else:
        return atual
#Essa função sorteia o numero, verifica a existencia desse numero nas cartelas e se encontrar o numero troca por X para indicar q o numero ja foi sorteado
def gera_lista_al(x,y):
    return r.sample(range(x),k=y)

def sorteio(c):
    return gera_lista_al(50, 50)

#essa função verifica o ganhador

def verif_ganha(c, atual):
    x = 0
    for i in range(5):
        if c[atual][i] == 'X':
            x +=1
        if x == 5:
            print('Parabens Jogador, você ganhou e tera seu nome gravado no rol dos vencedores')
            return True, 1
            exit()
    for i in range(4):
        x = 0
        for j in range(5):
            if i == atual:
                pass
            if c[i][j] == 'X':
                x += 1
            if x == 5:
                print('Temos um ganhador, mas infelizmente não foi sua vez Jogador')
                return True, 0
                exit()
    return False, 0

def master():
    cartela,atual = sorteia_cartela()
    f = False
    while f == False:
        dev_cartela(cartela, atual)
        atual = troca_cartela(cartela, atual)
        cartela = sorteio(cartela)
        f, j = verif_ganha(cartela, atual)
    if j == 1:
        a = input('Favor Insira o nome do Campeão: ')
        v = open('Vencedores.txt', 'a', encoding='utf-8')
        v.write(f'{a} - {pega_tempo()}')
        v.close()
    print('Fim do Bingo')
