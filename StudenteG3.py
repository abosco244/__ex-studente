class Studente:
    def __init__(self, nome = "", cognome = "", eta = 0, numero =0, lista = []):

        self.__nome = nome
        self.__cognome = cognome
        self.__eta = eta
        self.__numero = numero
        self.__lista = lista
    
     # Using @property decorator
    @property  
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, val):
       if type(val) == str: 
            self.__nome = val
       else:
        print("Il nome deve essere una stringa")

    @property  
    def cognome(self):
        return self.__cognome

    @cognome.setter
    def cognome(self, val):
         if type(val) == str:
            self.__cognome = val
         else:
            print("Il cognome deve essere una stringa")

    @property  
    def eta(self):
        return self.__eta
    @eta.setter
    def eta(self, val):
         if type(val) == int and val > 0:
            self.__eta = val
         else:
            print("eta inserita non valida")

    @property  
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, val):
        if len(str(val)) == 10 and type(val) == int:
            self.__numero = val
        else:
         print("Il numero inserito non valido")

    @property  
    def lista(self):
        return self.__lista
    
    
    @lista.setter   
    def lista(self, val):
        if type(val) == str:
            self.__lista = self.__lista + [val]
        else:
            print("corso non valido")
     # Deleter method
    @lista.deleter
    def lista(self, val):
       del self.__lsita[val]
 

