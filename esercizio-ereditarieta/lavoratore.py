from persona import Persona

class Lavoratore (Persona):
    def __init__(self,nome, cognome, eta, mansione):
        super().__init__(nome, cognome, eta)
        self.mansione = mansione
        
    def __str__(self):
        print(f"lavoratore -> {self.nome}, {self.cognome}, {self.eta}, {self.mansione}")
    
