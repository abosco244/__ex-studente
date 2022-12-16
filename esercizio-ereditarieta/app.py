class Persona:
    def __init__(self, nome, cognome, eta):
        self.__nome = nome
        self.__cognome = cognome
        self.__eta = eta
 
    def __str__(self):
        return f"Nome: {self.__nome}, Cognome: {self.__cognome}, Età: {self.__eta}"
 
 
class Studente(Persona):
    def __init__(self, nome, cognome, eta, voto):
        Persona.__init__(self, nome, cognome, eta)
        self.__voto = voto
 
    def __str__(self):
        return Persona.__str__(self)+", Voto: "+ str(self.__voto)
 
 
class Lavoratore(Persona):
    def __init__(self, nome, cognome, eta, stipendio):
        super.__init__(self, nome, cognome, eta)
        self.__stipendio = stipendio
 
    def __str__(self):
        return Persona.__str__(self)+", Stipendio: "+ str(self.__stipendio)
 
def main():
    persona1 = Persona("Mario", "Rossi", 25)
    studente1 = Studente("Luigi", "Tortellini", 15, 8)
    lavoratore1 = Lavoratore("Giovanni", "Bianchi", 46, 1300)
    print(persona1)
    print(studente1)
    print(lavoratore1)
main()