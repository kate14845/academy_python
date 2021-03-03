import math
import random


def ilPiuGrande(a,b):
    #funzione che prende in input due interi e restituisce 
    #il maggiore 

    if a>=b:
        return a
    else:
        return b


def isTriangle(a, b, c):
    # funzione che prende tre interi e stampa a schermo se possono essere le lunghezze di lati di un triangolo

    if a+b>=c and a+c>=b and b+c>=a:
        if a+b==c or a+c==b or b+c==a:
            print("Triangolo degenere")
        else:
             print("sì, è un triangolo!")
    else:
        print("no, non è un triangolo :(")

def sommanumeriinseriti():
    #funzione che chiede numeri da tastiera e restituisce la somma
    #si ferma quando viene inserito 0
    somma=0
    flag=1
    while flag==1:
        num=int(input('dammi un numero '))
        if num==0:
            print(somma)
            flag=0
        else:
            somma=somma+num


def indovina():
    # funzione che chiede di indovinare un numero casuale tra 1 e 1000 
    # e si chiude quando il numero inserito è esatto
    
    import random
    numeroRandom=random.randint(1,1000)
    print(numeroRandom)
    flag=0
    while flag==0:
        guess=int(input('indovina un numero da 1 a 1000 '))
        if guess==numeroRandom:
            print('esatto!')
            flag=1
        elif guess<numeroRandom and 0<guess<=1000:
            print('il numero è maggiore')
        elif guess>numeroRandom and 0<guess<=1000:
            print('il numero è minore')
        else:
            print('sei fuori dal range')

def sommaNminori():
    #funzione che chiede un numero intero positivo da tastiera
    #e stampa il piu grande numero intero per il quale la somma con gli interi precedenti è minore o uguale al 
    #numero immesso
    num=int(input('dammi un numero positivo '))
    somma=0
    cont=1
    while somma+cont<=num:
        somma=somma+cont
        cont+=1
    print(cont-1)

def risultatoesame():
    # funzione che chiede in input da tastiera i voti dello scritto e dell'orale di un esame 
    # e restituisce il risultato dell'esame
    
    bandiera=1
    while bandiera>0:
        scritto=int(input('voto scritto = '))
        pratica=int(input('voto pratica = '))
        if (-8<=scritto<=8 and 0<=pratica<=24):
            bandiera=0
    finale=scritto+pratica
    esito=0
    if scritto<=0 and finale>0:
        esito=1
    if scritto<=0 and pratica<18:
        esito=1
    if scritto>0 and finale<18:
        esito=1
    if finale==31 or finale==32:
        print('congratulazioni')
    elif esito==1:
        print('bocciato')
    else:
        print ('promosso con ',finale)
    
    def isto():

def isto():
    # funzione che chiede da tastiera dei numeri 
    # e stampa un diagramma a barre orizzontali di asterischi dei numeri inseriti 
    toprint=''
    while 3>1:        
        num=int(input('dammi un numero'))
        if num==0:
            break
        for k in range(0,num):
            toprint=toprint+'*'
        toprint=toprint+'\n'
    print(toprint)


def fibonacci():
    # funzione che chiede un intero positivo da tastiera
    # e restituisce la serie di fibonacci fino a quel numero

    n=input('dammi un intero positivo ')
    n1=0
    n2=1
    for k in range(0,int(n)):   
        if k==0:       
            print(k)  
        elif k==1:
            print(k)  
        else:
            tot=n1+n2
            n1=n2
            n2=tot
            print(tot)


def numeri():
    # funzione che chiede un numero variabile di numeri da tastiera
    # e restituisce il massimo
    # si chiude quando viene immesso 0

    num=int(input('dammi un numero '))
    max=num
    if num==0:
        return 'no numeri'
    while 3>1:
        num=int(input('dammi un numero '))
        if num==0:
            return max
        elif num>max:
            max=num

def ordine(a,b):
    # funzione che, dati due interi, stampa a video il più piccolo seguito dal più grande
    if a>b:
        print(b+', '+a)
    else: 
        print(a+', '+b)


def ruotadi90(angolo):
    #funzione che, dato un angolo in gradi 
    #restituisce il seno dell'angolo ruotato di 90 gradi 
    
    risultato=math.sin(math.radians(angolo)+math.pi/2)
    print(risultato)

def chevoto():
    # funzione che dato un intero restituisce l'esito del voto
    voto=int(input('dammi un voto da 0 a 10 '))
    if voto>5:
        print('Promosso')
    elif voto==5:
        print('Rimandato')
    elif 2<voto<5:
        print('Bocciato')
    elif voto<=2:
        print('Espulso')
