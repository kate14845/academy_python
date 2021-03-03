def controllo_palindromo():
    # funzione che chiede una parola da schermo 
    # in ingresso e restituisce True se è palindroma
    # o False se non lo è

    parola=input('dammi una parola ')
    lung=len(parola)
    for i in range(lung):
        if parola[i]!=parola[-i-1]:
            return False
    return True

def palindroma():
    # funzione che chiede da tastiera una parola e stampa a video se è palindroma
    parola=input('dammi una parola ')
    lung=len(parola)
    flag=True
    for i in range(lung):
        if parola[i]!=parola[-i-1]:
            flag=False
    if flag:
        print(parola+' è palindroma') 
    else:
        print(parola+' non è palindroma') 



def lenper():
# funzione che chiede una frase da tastiera e stampa il numero di caratteri della frase
    frase=input('dammi una frase: ')
    conta=0
    for lettera in frase:
        if lettera !=" ":
            conta+=1
    print(conta)

def findlettera():
    # funzione che chiede da tastiera una parola e una lettera
    # e stampa quante volte la lettera appare nella parola
        parola=input('che parola vuoi? ')
        lettera=input('che lettera cerchi? ')
        k=0
        contatore=0
        while k<len(parola):
                if parola[k]==lettera:
                        contatore=contatore+1
                k+=1
        print(lettera+' appare in '+parola,contatore,'volte')
