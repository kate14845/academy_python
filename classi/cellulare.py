class Cellulare:
# classe che simula la gestione del credito di un telefono 
# gli attributi di Cellulare sono il credito e il numero di chiamate effettuate
    def __init__(self,carica=0):
        self.carica=carica
        self.chiamate=0
    
    def ricarica(self,soldi):
        #aggiunge credito
        self.carica+=soldi

    def chiamata(self,minuti):
        #scala il costo di una chiamata
        if self.carica<=0:
            print('credito esuarito. fai una ricarica')
        else:
            self.chiamate+=1
            self.carica-=minuti*0.20
    def numero404(self):
        return self.carica
    def NumeroChiamate(self):
        return self.chiamate
    def AzzeraChiamate(self):
        self.chiamate=0
    def stato(self):
        #stampa il riepilogo di credito e numero chiamate
        print('hai fatto',self.chiamate,'chiamate, e ti rimangono',self.carica,'euro')

    


