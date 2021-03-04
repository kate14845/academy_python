import Biblioteca as B

# comandi sulla classe Biblioteca

# creo l'oggetto Biblioteca e lo chiamo b
b = B.Biblioteca("Biblioteca Civica di Trieste", "Trieste")
# aggiungo dei clienti
b.aggiungiCliente("Giacomo", "Rossi")
b.aggiungiStudente("Mario", "Resistenza",'ingegneria')
b.aggiungiCliente("Max", "Brutus")
b.aggiungiCliente("Bruno", "Verdi")
# questo ciclo deve stampare nome e cognome dei clienti
for cliente in b.getListaClienti():
    print(cliente.nome, cliente.cognome)
# produrra` come risultato:
#
#Giacomo Rossi
#Mario Resistenza
#Bruno Verdi
#Max Brutus
# interroghiamo l'oggetto biblioteca per cercare un cliente
# e vedere se e` uno studente
mb = b.cercaCliente("Max","Brutus")

print(mb.nome,mb.cognome)

print(mb.isStudente())
print(mb.bonusGiorniPrestito())

# aggiungo degli articoli:
b.aggiungiArticolo("CD06", "Pink Floyd", "The Wall", "Rock", "CD")
b.aggiungiArticolo("L205", "Schopenhauer", "Il mondo come volontà", "Filosofia", "libro")
b.aggiungiArticolo("L208", "Freud", "L'interpretazione dei Sogni", "Filosofia", "libro")
# richiedo la lista degli articoli:
for i in b.getListaArticoli():
    print(i.titolo, i.autore, i.genere)

b.registraPrestito("Pink Floyd", "The Wall", "Giacomo", "Rossi", "01-03-2021")
b.registraPrestito("Schopenhauer", "Il mondo come volontà", "Mario", "Resistenza", "21-01-2021")
b.registraPrestito("Freud", "L'interpretazione dei Sogni", "Max", "Brutus", "23-01-2021")
for prestito in b.getListaPrestiti():
    print(prestito.cliente.nome, prestito.cliente.cognome, prestito.articolo.titolo)
    b.controllaPrestito(prestito)
#Giacomo Rossi 12-01-2012 7 Pink Floyd The Wall
#Mario Resistenza 8-12-2012 40 Schopenhauer Il mondo come volonta
#print(prestito.cliente.nome, prestito.cliente.cognome, prestito.dataInizioPrestito,prestito.durataPrestito(), prestito.articolo.titolo, prestito.articolo.autore)