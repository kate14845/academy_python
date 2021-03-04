import datetime

# classi di gestione di una biblioteca che contiene una lista clienti, una lista articoli e un registo prestiti
# permette di registrare nuovi articoli come libri o CD e nuovi clienti e specificare se sono studenti
# registra i nuovi prestiti calcolando il tempo di prestito a seconda se l'articolo è un CD o un libro 
# e se l'utente è uno studente o meno
# controlla se i prestiti sono scaduti al giorno corrente


class Articolo():
    #classe per gli articoli della biblioteca caratterizzati da titolo autore e tipo che può essere CD o libro

    def __init__(self,collocazione,titolo,autore,tipo):
        self.collocazione=collocazione
        self.titolo=titolo
        self.autore=autore
        self.tipo=tipo
    
    def durataPrestito(self):
        # imposta la durata del prestito di default a 30 giorni

        durata=30
        return durata

class Libro(Articolo):
    # sottoclasse per i libri caratterizzati dal genere
    
    def __init__(self,collocazione,titolo,autore,tipo,genere=None):
        self.genere = genere 
        Articolo.__init__(self,collocazione,titolo,autore,tipo)

class CD(Articolo):
    # sottoclasse per i CD caratterizzati dal genere e dalla durata del prestito di 7 giorni
    
    def __init__(self,collocazione,titolo,autore,tipo,genere=None):
        self.genere = genere 
        Articolo.__init__(self,collocazione,titolo,autore,tipo)

    def durataPrestito(self):
        # setta il prestito a 7 giorni
        durata=7
        return durata

class Cliente():
    # classe per i clienti caratterizati da nome e cognome
    def __init__(self,nome,cognome):
        self.nome=nome
        self.cognome=cognome

    def __str__(self):
        # come viene stampato il nome del cliente se un oggetto cliente viene messo in un print
        return self.nome+' '+self.cognome

    def bonusGiorniPrestito(self):
        # gli studenti hanno 10 giorni di bonus per il prestito, gli altri no
        return 0

    def isStudente(self):
        # controlla che l'utente non sia uno studente
        return False

class Studente(Cliente):
    #definisce la classe studenti che gode di un bonus prestiti
    def __init__(self,nome,cognome,facolta=None):
        self.facolta = facolta 
        Cliente.__init__(self,nome,cognome)

    def bonusGiorniPrestito(self):
        # aggiunge 10 giorni al prestito per gli studenti
        return 10
    
    def isStudente(self):
        # controlla che una persona sia uno studente
        return True
class Prestito():
    # definisce gli oggetti prestito caratterizzandoli con il nome cliente
    # e l'articolo preso in prestito
    def __init__(self,cliente,articolo,dataInizioPrestito):
            self.cliente = cliente 
            self.articolo = articolo  
            self.dataInizioPrestito=dataInizioPrestito
    
    def durataPrestito(self):
        #calcola la durata del prestito a seconda del tipo di articolo 
        # e se il cliente sia uno studente o meno
        durata=self.articolo.durataPrestito()+self.cliente.bonusGiorniPrestito()
        return durata

class Biblioteca():
    # classe di gestione della biblioteca che controlla la lista cliente argomenti e prestiti
    def __init__(self,denominazione,luogo):
            self.denominazione = denominazione 
            self.luogo = luogo  
            self.listaClienti=[]
            self.listaArticoli=[]
            self.listaPrestiti=[]
    
    def getListaPrestiti(self):
        # restituisce la lista prestiti
        return self.listaPrestiti
    
    def getListaArticoli(self):
        # restituisce la lista articoli
        return self.listaArticoli

    def getListaClienti(self):
        # restituisce la lista prestiti
        return self.listaClienti
    
    def aggiungiCliente(self,nome, cognome):
        self.listaClienti.append(Cliente(nome,cognome))

    def aggiungiStudente(self,nome, cognome, facolta):
        self.listaClienti.append(Studente(nome,cognome,facolta))

    def aggiungiArticolo(self,collocazione, titolo, autore, genere, tipo):
        if tipo=='libro':
            self.listaArticoli.append(Libro(collocazione,titolo,autore,tipo,genere))
        elif tipo=='CD':
            self.listaArticoli.append(CD(collocazione,titolo,autore,tipo,genere))
        else:
            print('Tipo non supportato')

    def cercaCliente(self,nome, cognome):     
        for cliente in self.listaClienti:
            if cliente.nome==nome and cliente.cognome==cognome:
                return cliente
        print('Cliente non trovato')
  
    
    def cercaArticolo(self,titolo,autore):     
        # controlla se un articolo è nella biblioteca
        for articolo in self.listaArticoli:
            if articolo.titolo==titolo and articolo.autore==autore:
                return articolo
        print('Articolo non trovato')
    
    def controllaPrestito(self,prestito):
        # stampa lo stato del prestito
        dataoggi=datetime.datetime.now()
        datainizio=datetime.datetime.strptime(prestito.dataInizioPrestito, '%d-%m-%Y')
        tempoprestito=(dataoggi-datainizio).days
        if tempoprestito>prestito.durataPrestito():
            print('Prestito scaduto da',tempoprestito-prestito.durataPrestito(),'giorni.')
        elif tempoprestito==prestito.durataPrestito():
            print('Da consegnare')
        else:
            print('Prestito attivo. Hai ancora',prestito.durataPrestito()-tempoprestito,'giorni.')
        

    
    def registraPrestito(self,titolo, autore, nomeCliente, cognomeCliente, dataPrestito):
        if self.cercaArticolo(titolo,autore)!=None and self.cercaCliente(nomeCliente,cognomeCliente)!=None:
            self.listaPrestiti.append(Prestito(self.cercaCliente(nomeCliente,cognomeCliente),self.cercaArticolo(titolo,autore),dataPrestito))
        

