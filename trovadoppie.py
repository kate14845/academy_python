#trova le parole con le doppie in un file.txt
def trovadoppie(fileloc):
    #funzione che apre il file con nome fileloc e salva le parole in una lista
    with open(fileloc, "r") as fileInput:
        parole=fileInput.read().strip().split()
    # mette le parole con doppie in una nuova lista
    parolecondoppie=[]
    for parola in parole:
        for j,lettera in enumerate(parola[:-1]):
                if parola[j+1]==lettera:
                    parolecondoppie.append(parola)
                    break
    return parolecondoppie
            
print(len(trovadoppie('words.txt')))