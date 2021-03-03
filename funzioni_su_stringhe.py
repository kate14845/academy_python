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


def lenper():
# funzione che chiede una frase da tastiera e stampa il numero di caratteri della frase
    frase=input('dammi una frase: ')
    conta=0
    for lettera in frase:
        if lettera !=" ":
            conta+=1
    print(conta)