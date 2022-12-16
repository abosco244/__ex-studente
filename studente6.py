class Studente:
    def __init__(self, nome, cognome, eta, telefono):
        self.__nome = nome
        self.__cognome = cognome
        self.__eta = eta
        self.__telefono = telefono

    def __str__(self):
        return f"Nome studente: {self.nome}\n Cognome studente: {self.cognome}\n Età: {self.eta}\n Numero di telefono: {self.telefono}\n Corso: {self.corsi}\n "


    corsi = ["corso1", "corso2", "corso3"]

    def aggiunta_corso(self, nome_corso):
        self.corsi.append(nome_corso)

    def rimozione_corso(self, nome_corso):
        if nome_corso in self.corsi:
            self.corsi.remove(nome_corso)
            print(f"{nome_corso} rimosso")
        else:
            print(f"{nome_corso} non presente")

    def stampa_testo(self):
        print(self.corsi)



    @property 
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        if type(self.nome) == str:
            self.__nome = nome
            print("Nome aggiunto")
        else:
            print("Nome non valido")

    @property 
    def cognome(self):
        return self.__cognome

    @cognome.setter
    def cognome(self, cognome):
        if type(cognome) == str:
            self.__cognome = cognome
            print("Cognome aggiunto")
        else:
            print("Cognome non valido")
    
    @property 
    def eta(self):
        return self.__eta

    @eta.setter
    def eta(self, eta):
        if eta > 18:
            self.__eta = eta
            print("Età aggiunta")
        else:
            print("Età non valida")

    @property 
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, telefono):
        if len(str(self.telefono)) != 10:
            print("Numero di telefono non valido")
        else:
            self.__telefono = telefono

studente1 = Studente('giovanni', 'rossi', 26, 3476449251)
studente2 = Studente('marco', 'ferri', 23, 3654336272)

print(studente1, studente2)


studente1.eta=17

print(studente1)


    
            
        