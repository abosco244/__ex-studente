class Studente:
    
    def __init__(self):
        self.nome = None
        self.cognome = None
        self.eta = None
        self.telefono = None
        self.corsi_dello_studente = []
        
    
    def __init__(self,nome,cognome,eta,telefono):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
        self.telefono = telefono
        self.corsi_dello_studente = []
        
       
    @property
    def nome(self):
        return self.__nome
    
    @property
    def cognome(self):
        return self.__cognome
    
    @property
    def eta(self):
        return self.__eta

    @property
    def telefono(self):
        return self.__telefono
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
        
    @cognome.setter
    def cognome(self, cognome):
        self.__cognome = cognome
        
    @eta.setter
    def eta(self, eta):
        self.__eta = eta
        
    @telefono.setter
    def telefono(self, telefono):
        if len(str(telefono)) < 10:
            print("Errore di validazione:numero minore di 10 cifre")
        else:
            self.__telefono = telefono
    
    def append (self, obj):
        self.corsi_dello_studente.append(obj.lower())
        print(f"Corso aggiunto: {obj}  ")
        
    def remove(self, obj):
        if self.corsi_dello_studente.count(obj.lower()) > 0:
            self.corsi_dello_studente.remove(obj.lower())
            print(f"Corso rimosso: {obj}  ")
        else: 
            print(f"Il corso {obj} non è nella lista!")
        
    def print(self):
        print("Questi sono i corsi dello studente: ")
        print(*self.corsi_dello_studente, sep = ", ")
    
