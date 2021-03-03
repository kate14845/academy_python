import random

def scalaViteACaso(dizionario):
    # funzione che prende un dizionario come input dove ad ogni nome è associato un intero
    # stampa a schermo i nomi inseriti in modo casuale per un numero di volte pari al numero di vite
    # quando tutti i participanti hanno finito le vite ricomincia da capo
    
    ordix=dizionario.copy()

    nomi=list(dizionario.keys())
    originale=nomi.copy()
    tastiera=input('ecco un nome')
    while 0<1:
        while  tastiera!=" " and len(nomi)>0:
                seed=random.randint(0,len(nomi)-1)
                nome=nomi[seed]
                dizionario[nome]-=1
                print(nome)
                if dizionario[nome]==0:
                    nomi.remove(nome)    
                #print(nomi)        
                tastiera=input('ecco un nome')
        print('si ricominicia')
        nomi=originale.copy()
        dizionario=ordix.copy()
#scalaViteACaso({'marius':5,'elem3':6})

def estraiDaLista(lista)
# funzione che, data una lista in ingresso, ne estrae gli elementi in ordine causale una volta per chiascun elemento
# una volta finiti, ricomincia
# si chiude inserendo uno spazio
    originale=lista.copy()
    tastiera=input('premi invio per aver un elemento, inserisci uno spazio per chiudere')
    while tastiera!=" " and len(lista)>0:
        seed=random.randint(0,len(lista)-1)
        print(lista[seed])
        temp=lista.pop(seed)
        tastiera=input('premi invio per aver un elemento, inserisci uno spazio per chiudere')
    lista=originale.copy()

#estraiDaLista([elem1,elem2,elem3])