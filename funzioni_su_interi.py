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

def somma():
    #funzione che chiede numeri da tastiera e restituisce la somma
    #si ferma quando viene inserito 0
    somma=0
    flag=1
    while flag==1:
        num=int(input('dammi un numero '))
        if num==0:
            print(àsomma)
            flag=0
        else:
            somma=somma+num