#o import é usado para importar bibliotecas e a biblioteca random é usada para gerar numeros aleatorios
import random
# criando uma variavel para armazenar as palavras que serao sorteadas 
palavras = []
#criamos uma variavel vazia para quando o jogador digitar uma letra errada
letrasErradas = ''
#criamos uma variavel vazia para quando o jogador digitar uma letra certa
letrasCertas = ''
#variavel utilizada para adicionar um caractere a cada letra que o jogador errar
FORCAIMG = ['''
 
  +---+
  |   |
      |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

#funçao usada para criar uma funçao
def principal():
    """
    Função Princial do programa
    """
#o print é usado para imprimir
    print('F O R C A')
    palavrasSugeridas():
#funçao que sera definida por sortearPalavra(uma palavra da lista sera sorteada  e essa sera a apalavra secreta)
    palavrasSugeridas():
    palavraSecreta = sortearPalavra()
#palpite do jogador
    palpite = ''
#reconhece qual é a palavra certa e avalia se o palpite do jogador esta certo ou errado ,se estiver errado ele acrescenta um caractere a FORCAIMG
    desenhaJogo(palavraSecreta,palpite)
#enquanto for verdadeiro o loop continuara rodando ( o jogador digita seu palpite e continua jogando)
    while True:
        palpite = receberPalpite()
        desenhaJogo(palavraSecreta,palpite)
#se o jogador errar todos os palpites disponiveis e perder o jogo a funçao perdeuJogo sera ativada
        if perdeuJogo():
#o print vai imprimir na tela a mensagem avisando o jogador que ele perdeu o jogo
            print('Voce Perdeu!!!')
#o break fara com que o loop pare de rodar
            break
#se o jogador acertar os seus palpites e acertar a palavra secreta a funçao ganhouJogo sera ativada
        if ganhouJogo(palavraSecreta):
#o print vai imprimir na tela a mensagem avisando o jogador que ele ganhou o jogo
            print('Voce Ganhou!!!')
#o break fara com que o loop pare de rodar
            break            
#funçao perdeu o jogo
def perdeuJogo():
#o global é uma funçao que pode chamar qualquer variavel que esteja em qualquer lugar do programa
    global FORCAIMG
#o len fala quantos itens tem numa lista(ele vai contar quantas letras esta errada e indicar para FORCAIMG
    if len(letrasErradas) == len(FORCAIMG):
#se a funçao perdeuJogo for verdadeira ele retorna para quem chamou a funçao
        return True
    else:
#se a funçao perdeuJogo for falsa ele nao executa nada
        return False
# se o jogador tiver acertado a palavra secreta a funçao global vai ligar a variavel letrasCertas e ganhou sera verdadeiro
def ganhouJogo(palavraSecreta):
    global letrasCertas
    ganhou = True
#se para cada letra que tiver na palavraSecreta e nao estiver na lista de letras certas vai indicar que ganhou é falso, e caso seja verdadeira vai indicar que o jogador ganhou
    for letra in palavraSecreta:
        if letra not in letrasCertas:
            ganhou = False 
    return ganhou        
        

#funçao receber palpite
def receberPalpite():
#quando o jogador digitar mais uma letra,ira aparecer na tela para ele digitar so uma por vez.    
    palpite = input("Adivinhe uma letra: ")
    palpite = palpite.upper()
    if len(palpite) != 1:
        print('Coloque um unica letra.')
#quando voce ja estiver digitado a letra ,ira aparecer que essa letra ja foi digitada
    elif palpite in letrasCertas or palpite in letrasErradas:
        print('Voce ja disse esta letra.')
#se o jogador digitar um caractere diferente do alfabeto,aparecer para escolher so letras.
    elif not "A" <= palpite <= "Z":
        print('Por favor escolha apenas letras')
#se caso todas as afirmaçoes acima for falsa ele retorna no palpite para a pessoa palpitar.
    else:
        return palpite
    
#essa funçao vai chamara as variaveis letrasCertas,letraserradas e FORCAIMG para imprimir na tela as letras Certas  e erradas e desenhar uma parte do boneco. 
def desenhaJogo(palavraSecreta,palpite):
    global letrasCertas
    global letrasErradas
    global FORCAIMG

    print(FORCAIMG[len(letrasErradas)])
    
#para cada letra da palavra secreta adicione um "-"(tracinho).     
    vazio = len(palavraSecreta)*'-'
#se o palpite do jogador estiver na palavra secreta vai adicionar na viriavel letrasCertas.se nao adicionara em letrasErradas.

    if palpite in palavraSecreta:
        letrasCertas += palpite
    else:
        letrasErradas += palpite

    for letra in letrasCertas:
        for x in range(len(palavraSecreta)):
            if letra == palavraSecreta[x]:
                vazio = vazio[:x] + letra + vazio[x+1:]
#vai imprimir na tela as letras erradas ecertas e tambem os tracinhos                
    print('Acertos: ',letrasCertas )
    print('Erros: ',letrasErradas)
    print(vazio)
     
#funçao sortear uma pálavra
def sortearPalavra():
    global palavras
#funçao upper e pra deixar tudo maiusculo
    return random.choice(palavras).upper()
#nessa funçao o jogador pode sujerir as palavras que deseja que faca parte do jogo.
def palavrasSugeridas():
    global palavras
    while True:
        sugestao=input("escreva as palavras que deseja para o jogo")
        sugestao.append(sugestao)
        if sugestao=="":
            break
        
        

    
principal()
