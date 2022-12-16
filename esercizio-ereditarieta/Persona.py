class Persona:
    def __init__(self, nome, cognome, eta):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
    
    def __str__(self):
        return f"Nome: {self.nome}\n Cognome: {self.cognome} \n Eta: {self.eta} \n"


class Studente(Persona):
    def __init__(self, nome, cognome, eta, corso):
        super().__init__(nome, cognome, eta)
        self.corso = corso

    def __str__(self):
        return f"Nome: {self.nome}\n Cognome: {self.cognome} \n Eta: {self.eta} \n Corso: {self.corso} \n"

class Lavoratore(Persona):
    def __init__(self, nome, cognome, eta, lavoro):
        super().__init__(nome, cognome, eta)
        self.lavoro = lavoro

    def __str__(self):
        return f"Nome: {self.nome}\n Cognome: {self.cognome} \n Eta: {self.eta} \n Lavoro: {self.lavoro} \n"


