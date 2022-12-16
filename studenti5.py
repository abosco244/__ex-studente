class Studente:
    
    
    
    def __init__(self, nome, cognome, eta, telefono):
        self.__nome = nome
        self.__cognome = cognome
        self.__eta = eta
        self.__telefono = telefono
        self.corso=[]

    def __str__(self):
        return f"Nome studente: {self.nome}\n Cognome studente: {self.cognome}\n Età: {self.eta}\n Numero di telefono: {self.telefono}\n Corso: {self.corsi}\n "


    

    def aggiunta_corso(self, nome_corso):
        self.corsi.append(nome_corso)
        print(f"{nome_corso} aggiunto")

    def rimozione_corso(self, nome_corso):
        if nome_corso in self.corsi:
            self.corsi.remove(nome_corso)
            print(f"{nome_corso} rimosso")
        else:
            print(f"{nome_corso} non presente")

    def stampa_testo(self):
        print(self.corsi)



    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        if type(self.nome) == str:
            self.__nome = nome
            print("Nome aggiunto")
        else:
            print("Nome non valido")
    
    nome= property (get_nome, set_nome)

    def get_cognome(self):
        return self.__cognome

    def set_cognome(self, cognome):
        if type(cognome) == str:
            self.__cognome = cognome
            print("Cognome aggiunto")
        else:
            print("Cognome non valido")
    
    cognome= property (get_cognome, set_cognome)
    
    def get_eta(self):
        return self.__eta
    
    def set_eta(self, eta):
        if eta > 18:
            self.__eta = eta
            print("Età aggiunta")
        else:
            print("Età non valida")

    eta= property (get_eta, set_eta)
    
    def get_telefono(self):
        return self.__telefono

    
    def set_telefono(self, telefono):
        if len(str(self.telefono)) != 10:
            print("Numero di telefono non valido")
        else:
            self.__telefono = telefono
    
    telefono= property (get_telefono, set_telefono)


studente1 = Studente('giovanni', 'rossi', 26, 3476449251)
studente2 = Studente('marco', 'ferri', 23, 3654336272)

print(studente1, studente2)
print("-"*40)


studente1.set_eta(17)

print(studente1)
print("-"*40)

studente1.stampa_testo()

            
        