import tkinter as tk
from tkinter import ttk
import numpy as np
from tkinter import *

# programma che permette di giocare a tris in due persone con una piccola interfaccia grafica 

win=tk.Tk()
win.title('tris')
testo=ttk.Label(win, text='testo').grid(column=0,row=0)
global matrice
matrice=np.array([[0,0,0],[0,0,0],[0,0,0]])
global giocatore
giocatore=1
global contatore


def cambiabottone(i,j):
    if giocatore==1:
        carattere='X'
    else:
        carattere='O'
    if i==0 and j==0:
        cella00.configure(text=carattere)
        cella00['state']=DISABLED
    if i==0 and j==1:
        cella01.configure(text=carattere)
        cella01['state']=DISABLED
    if i==0 and j==2:
        cella02.configure(text=carattere)
        cella02['state']=DISABLED
    if i==1 and j==0:
        cella10.configure(text=carattere)
        cella10['state']=DISABLED
    if i==1 and j==1:
        cella11.configure(text=carattere)
        cella11['state']=DISABLED
    if i==1 and j==2:
        cella12.configure(text=carattere)
        cella12['state']=DISABLED
    if i==2 and j==0:
        cella20.configure(text=carattere)
        cella20['state']=DISABLED
    if i==2 and j==1:
        cella21.configure(text=carattere)
        cella21['state']=DISABLED
    if i==2 and j==2:
        cella22.configure(text=carattere)
        cella22['state']=DISABLED


def controllo(): 
    for i in range(3):
        if matrice[0][i]==giocatore and matrice[1][i]==giocatore and matrice[2][i]==giocatore:
            return True
        if matrice[i][0]==giocatore and matrice[i][1]==giocatore and matrice[i][2]==giocatore:
            return True
    if matrice[0][0]==giocatore and matrice[1][1]==giocatore and matrice[2][2]==giocatore:
        return True
    if matrice[2][0]==giocatore and matrice[1][1]==giocatore and matrice[0][2]==giocatore:
        return True
        return False

def pareggio():
    for i in range(3):
        for j in range(3):
            if matrice[i][j]==0:
                return False
    return True

def finiscipartita():
    cella00['state']=DISABLED
    cella01['state']=DISABLED
    cella02['state']=DISABLED
    cella10['state']=DISABLED
    cella11['state']=DISABLED
    cella12['state']=DISABLED
    cella20['state']=DISABLED
    cella21['state']=DISABLED
    cella22['state']=DISABLED

def click_me(i,j): 
    global matrice
    global giocatore
    vincitore=0
    matrice[i][j]=giocatore
    cambiabottone(i,j)   
    if controllo():
        messaggio.configure(text='ha vinto il giocatore '+str(giocatore))
        vincitore=1
        finiscipartita()
    if pareggio()and vincitore==0:
        messaggio.configure(text='pareggio')    
    if giocatore==1:
        giocatore=2
    else:
        giocatore=1

cella00=ttk.Button(win, text='',command=lambda: click_me(0,0))
cella00.grid(row=0,column=0)
cella01=ttk.Button(win, text='',command=lambda: click_me(0,1))
cella01.grid(row=0,column=1)
cella02=ttk.Button(win, text='',command=lambda: click_me(0,2))
cella02.grid(row=0,column=2)


cella10=ttk.Button(win, text='',command=lambda: click_me(1,0))
cella10.grid(row=1,column=0)
cella11=ttk.Button(win, text='',command=lambda: click_me(1,1))
cella11.grid(row=1,column=1)
cella12=ttk.Button(win, text='',command=lambda: click_me(1,2))
cella12.grid(row=1,column=2)

cella20=ttk.Button(win, text='',command=lambda: click_me(2,0))
cella20.grid(row=2,column=0)
cella21=ttk.Button(win, text='',command=lambda: click_me(2,1))
cella21.grid(row=2,column=1)
cella22=ttk.Button(win, text='',command=lambda: click_me(2,2))
cella22.grid(row=2,column=2)

messaggio=Label(win,text='')
messaggio.grid(row=3,columnspan=3)


win.mainloop()