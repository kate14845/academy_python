import random
class Dado:
    #funzione che simula il lancio di un dado
    def __init__(self,numeroDiFacce=6):
        self.facce=numeroDiFacce
        self.seed=random.randint(1,self.facce)
        #inizializza il dado a un numero casuale
    
    def getRandom(self):
        # ritorna la faccia del dado
        return self.seed
    def lancio(self):
        # lancia il dado 
        print(self.seed)
        self.seed=random.randint(1,self.facce)
   

