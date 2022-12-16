from studente import Studente

nome = input("Inserisci Nome: ")
cognome = input("Inserisci Cognome: ")
eta = int(input("Inserisci età: "))
telefono =  input("Numero di telefono: ")

Studente1 = Studente(nome,cognome,eta,telefono)

    
Studente1.append("Matematica")

Studente1.append("Italiano")

Studente1.append("Geografia")

Studente1.remove("Italiano")

Studente1.remove("Inglese")

Studente1.print()

