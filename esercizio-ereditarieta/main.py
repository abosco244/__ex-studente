
# Si ha la necessità di definire tre classi in Python: persona, studente, lavoratore. Le ultime due classi elencate, ovvero studente e lavoratore sono classe derivate dalla classe persona. Scrivere il codice Python che permette di definire le tre classi su elencate (tenendo conto del concetto di ereditarietà) e un piccolo main che ne richiama i metodi definiti. NOTA IMPORTANTE: si definiscano solo gli attributi (3 per la classe persona, 1 specifico di studente, 1 specifico di lavoratore) e i metodi init e str.

from persona import Persona
from studente import Studente
from lavoratore import Lavoratore

persona1 = Persona("Alessandro", "bosco", 15)

persona1.__str__()

studente1 = Studente("Alessandro", "bosco", 15, "Don Luigi Sturzo")

studente1.__str__()

lavoratore1 = Lavoratore("Alessandro", "bosco", 15, "insegnante")

lavoratore1.__str__()
