import random
# import time

# Dicionario onde as perguntas são as chaves e os valores as alternativas
dic = {'Qual é o TR1ΔNGULO isósceles?': ['2. ⊿','3. △','4. ◯','5. ▽','1'], 
       'Em que ano foi fundada a Bosch?': ['1980','1893','2010','1922','1886'],
       'Qual foi o primeiro nome do jogo Tetris?': ['Pentamino', 'Blocks Puzzle', 'Stacking', 'Tessaro', 'Tetris'],
       'Qual dessas linguagens de programação é de baixo nível?': ['Python','C#','JavaScript','PHP','Assembly'],
       'Quem foi a única pessoa na história a receber o Prêmio Nobel em áreas científicas diferentes?': ['1. Albert Einstein','2. Linus Pauling','3. Stephen Hawking','4. Marie Curie','4'],
       'O que significa a sigla WWW?': ['1. Wide World Web','2. World Wide Web','3. Web Wide World','4. Wide Web World','2'],
       'Qual o lugar mais profundo dos oceanos?': ['1. Fossa de Java','2. Fossa das Marianas','3. Fossa de Tonga','4. Fossa de Bentley','2'],
       'Em quais planetas chove diamantes?': ['1. Netuno e Urano','2. Mercúrio e Saturno','3. Urano e Vênus','4. Netuno e Júpiter','1']}

# def devagarinho(texto):
#     lista = []
    
#     texto = texto.replace('','@')
#     devagar = texto.split('@')
#     devagar.pop(0)
#     devagar.pop(len(devagar)-1)

#     for i in devagar:
#         lista.append(i)
#     for i in range(len(lista)):
#         print(lista[i], end = '')
#         time.sleep(0.2)   

# Função que pega todas as chaves do dicionario e retorna todas elas misturadas dentro de uma lista
def randomquest():
    global dic
    chaves = []
    # Cria uma tupla com todas as chaves
    unchaves = dic.keys()
    
    # Pega cada item de unchaves e coloca dentro de uma lista
    for chave in unchaves:
        chaves.append(chave)
        
    # Mistura todos os valores da lista
    random.shuffle(chaves)
    
    return chaves
    
def printandoperguntas(chaves):
    # Cria um for com o número de itens dentro da lista chaves
    for i in range(len(chaves)):
        # Printa o número da questão e a questão em si de acordo com i
        print('\n'*30)
        print('_'*99)
        print('')
        print(f'{i+1}) {chaves[i]}'.center(100))
        print('_'*99)
        print('')
        
        # Armazena a lista de alternativas de acordo com a chave
        alternativas = dic[chaves[i]]
        
        print('')
        # Printa todas as alternativas da questão no centro
        for j in range(4):
            print(alternativas[j].center(100))
        
        # Muda a legenda inferior de acordo com a questão
        if chaves[i] == 'Em que ano foi fundada a Bosch?':
            print('')
            print('Python Game - Smart Quiz 1886'.center(160))
            print('_'*99)
        elif chaves[i] == 'Qual dessas linguagens de programação é de baixo nível?':
            print('')
            print('Assembly Game - Smart Quiz 2023'.center(160))
            print('_'*99)
        else:
            print('')
            print('Python Game - Smart Quiz 2023'.center(160))
            print('_'*99)
    
        resposta = input('> ')
        
        # Verifica a resposta e retorna False se estiver errada
        if resposta != alternativas[4]:
            return False
    # Se a pessoa acertar todas as questões retorna True
    return True

escolha = 0
continuar = 1

try:
    # Printa a interface inicial
    while(continuar == 1):
        print('\n'*30)
        print('_'*99)
        print('')
        print('_______________'.center(100))
        print('|   SMART QUIZ  |'.center(100))
        print('| A Python game |'.center(100))
        print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾'.center(100))
        
        print('_______________'.center(100))
        print('|    Iniciar    |'.center(100))
        print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾'.center(100))
        print('_______________'.center(100))
        print('|    Créditos   |'.center(100))
        print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾'.center(100))
        print('_'*99)
        
        # Se a pessoa colocar um valor inválido anteriormente, vai exibir a mensagem de que há algo errado
        if escolha == 1:
            print('\nO valor inserido anteriormente não era válido, tente novamente.')
        e = input('> ')
        
        if e == 'Iniciar' or e == 'iniciar' or e == 'INICIAR' or e == 'i':
            escolha = 0
            # Verifica se a função principal do jogo retorna False ou True
            if printandoperguntas(randomquest()) == False:
                print('\n'*30)
                print('Você errou!'.center(100))
                print('Deseja tentar novamente?'.center(100))
                print('___________'.center(100))
                print('|    SIM    |'.center(100))
                print('‾‾‾‾‾‾‾‾‾‾‾'.center(100))
                print('___________'.center(100))
                print('|    NÃO    |'.center(100))
                print('‾‾‾‾‾‾‾‾‾‾‾'.center(100))
                
                while(True):
                    e2 = input('> ')
                    
                    # Verifica a resposta de se deseja continuar ou não
                    if e2 == 'não' or e2 == 'nao' or e2 == 'NÃO' or e2 == 'NAO' or e2 == 'n' or e == 'N':
                        continuar = 0
                        break
                    elif e2 == 'sim' or e2 == 'SIM' or e2 == 's':
                        break
                    else:
                        print('Valor inserido não é válido!')
                        continue
            else:
                print('\n'*30)
                print('PARABÉNS, VOCÊ É UM GÊNIO!'.center(100))
                print('Apenas 0.00001% das pessoas consegue resolver esse quiz.'.center(100))
                break
            
        elif e == 'Créditos' or e == 'Creditos' or e == 'creditos' or e == 'CREDITOS' or e == 'créditos' or e == 'CRÉDITOS' or e == 'c' or e == 'C':
            print('\n'*30)
            print('_______________'.center(100))
            print('|    Créditos   |'.center(100))
            print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾'.center(100))
            print('Criador:'.center(100))
            print('Luiz Antonio Rosa Cardoso'.center(100))
            print('')
            print('Gênio Quiz Original:'.center(100))
            print('André Birnfield'.center(100))
            print('')
            print('Digite "sair" para sair da tela de créditos'.center(100))
            
            while(True):
                e3 = input('> ')
                
                # Verifica a resposta de se deseja continuar ou não
                if e3 == 'sair' or e3 == 'SAIR' or e3 == 's':
                    break
                else:
                    print('Valor inserido não é válido!')
                    continue
            
        else:
            escolha = 1

except KeyboardInterrupt:
    print('\nPrograma encerrado pelo administrador.')
except:
    print('\nAlgum erro ocorreu durante a execução do programa.')