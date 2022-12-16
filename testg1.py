from StudenteG3 import Studente
studente1 = Studente()

studente1.nome="Alessandro"
studente1.cognome = "Rossi"
studente1.eta = 44
studente1.numero = 1000000000
studente1.lista = "corso1"
studente1.lista = "corso2"

del studente1.lista[0]
print('lista: ',studente1.lista)