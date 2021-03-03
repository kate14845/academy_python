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

def estraiDaLista(lista):
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

def sommaDizionari(d1,d2):
    # funzione che chiede due dizionari in ingresso 
    # e restituisce un terzo dizionario con la somma dei valori nelle chiavi comuni 
    # e aggiunge le chiavi non comuni

    d3=dict()
    for k1 in d1:
        for k2 in d2:
            if k1==k2:
                d3[k1]=d1[k1]+d2[k2]
                break

    for k1 in list(d1.keys()):
        if k1 not in list(d3.keys()):
            d3[k1]=d1[k1]

    for k2 in list(d2.keys()):
        if k2 not in list(d3.keys()):
            d3[k2]=d2[k2]
    return d3

#d1={'a':1,'b':2,'c':3}
#d2={'a':2,'b':3,'d':4}
#print(sommaDizionari(d1,d2))

def sommalistestrana(d1,d2):
    #funzione che prende in ingresso due liste
    # somma i valori nella stessa posizioni
    # e aggiunge gli elementi della lista più lunga

    if len(d1)<len(d2):
        lmin=len(d1)
        lmax=len(d2)
        flag=2
    else:
        lmin=len(d2)
        lmax=len(d1)
        flag=1
    d3=list(range(0,lmax))

    for i in range(lmin):
        d3[i]=d1[i]+d2[i]
    for i in range(lmin+1,lmax):
        if flag==1:
            d3[i]=d1[i]
        else:
            d3[i]=d2[i]

    return d3

d1=[100,200,300]
d2=[200,400,26,600,700]
print(sommalistestrana(d1,d2))
