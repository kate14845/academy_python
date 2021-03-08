import random


global sudoku

def stampa():
    stringa='  0 1 2   3 4 5   6 7 8 \n'
    for indice,riga in enumerate(sudoku):
        stringa+=str(indice)+' '
        for j,lettera in enumerate(riga[:-1]):
            if j==2 or j==5:
                stringa+=str(lettera)+' | '
            else: 
                stringa+=str(lettera)+' '
        stringa+=str(riga[-1])+'\n'
        if indice==2 or indice==5:
            stringa+='---------------------\n'
    print(stringa)

def nuovogioco():
    with open('puzzles.txt', "r") as fileInput:
        gioco=fileInput.readlines()[0].strip() #random.randomint(0,49)
    for indice,carattere in enumerate(gioco):
        if carattere!='.':
            sudoku[indice//9][indice%9]=int(carattere)
                   

def inizializza():
    for indice in range(9):
        sudoku.append([0 for i in range(9)])

def controlla(x,y, numero): 
    # prende tre interi e ritorna True se posso mettere 'numero' alla posizione (x,y)
    if numero in sudoku[x]:
        return False
    elif numero in [riga[y] for riga in sudoku]:
            return False
    else:
        cella=[]
        for riga in sudoku[3*(x//3):3*(x//3+1)]:
            cella.extend(riga[3*(y//3):3*(y//3+1)])
        if numero in cella:
            return False
        else:
            return True

sudoku=[]
inizializza()
#stampa()
nuovogioco()
stampa()
#random.shuffle(lista)
numero=int(input('dammi un numero da 1 a 9 '))
coor=input('dove lo vuoi mettere? ')
x=int(coor[0])
y=int(coor[1])
if sudoku[x][y]==0:
    if controlla(x,y,numero):
        sudoku[x][y]=numero
    else:
        print('non puoi!')
else:
    print('occupata!')
stampa()