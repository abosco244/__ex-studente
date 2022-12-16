from persona import Persona

class Studente (Persona):
    def __init__(self,nome, cognome, eta, scuola):
        super().__init__(nome, cognome, eta)
        self.scuola = scuola
        
    def __str__(self):
        print(f"studente -> {self.nome}, {self.cognome}, {self.eta}, {self.scuola}")
    
