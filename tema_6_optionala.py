
from datetime import date
from prettytable import PrettyTable
"""
1. Clasa Factura
Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor
avea aceeași serie), număr, nume_produs, cantitate, pret_buc
Constructor: toate atributele, fara serie
Metode:
● schimbă_cantitatea(cantitate)
● schimbă_prețul(pret)
● schimbă_nume_produs(nume)
● generează_factura() - va printa tabelar dacă reușiți
Factura seria x numar y
Data: generați automat data de azi
Produs | cantitate | preț bucată | Total
Telefon | 7 | 700 | 49000
"""
#
#
# class Factura:
#     SERIA = "XYZ"
#     numar = 0
#
#     def __init__(self, nume_produs, cantitate, pret_buc):
#         self.nume_produs = nume_produs
#         self.cantitate = cantitate
#         self.pret_bucata = pret_buc
#         self.today = date.today()
#
#     def schimba_cantitatea(self, noua_cantitate):
#         self.cantitate = noua_cantitate
#
#     def schimba_pretul(self, noul_pret):
#         self.pret_bucata = noul_pret
#
#     def schimba_nume_produs(self, noul_nume_produs):
#         self.nume_produs = noul_nume_produs
#
#     def genereaza_factura(self):
#         pret_total = self.cantitate * self.pret_bucata
#
#         Factura.numar += 1
#         print(f"Factura seria {self.SERIA} numar {Factura.numar}")
#         print(f"Data : {self.today}")
#         t = PrettyTable(["Produs", "Cantitate", "Pret bucata", "Total"])
#         t.add_row([self.nume_produs, self.cantitate, self.pret_bucata, pret_total])
#         print(t)
#
#
# telefon = Factura("telefon", 3, 1200)
#
# laptop = Factura("laptop", 2, 2500)
#
# telefon.genereaza_factura()
# print("_" * 100)
# telefon.schimba_cantitatea(5)
# telefon.schimba_nume_produs("telefon mobil")
# telefon.schimba_pretul(900)
# telefon.genereaza_factura()
# print("_" * 100)
# laptop.genereaza_factura()
# print("_" * 100)
# laptop.genereaza_factura()
# print("_" * 100)
# laptop.genereaza_factura()
#_______________________________________________________________________________________________________________________

"""
2.Clasa Masina
Atribute: marca, model, viteza maxima, viteza_actuala, culoare,
culori_disponibile (set), inmatriculata (bool)
Culoare = gri - toate mașinile cand ies din fabrica sunt gri
Viteza_actuală = 0 - toate mașinile stau pe loc când ies din fabrica
Culori disponibile = alegeți voi 5-7 culori
Marca = alegeți voi - fabrica produce o singură marca dar mai multe modele
Inmatriculata = False
Constructor: model, viteza_maxima
Metode:
● descrie() - se vor printa toate atributele, în afară de culori_disponibile
● înmatriculare() - va schimba atributul înmatriculată în True
● vopsește(culoare) - se va vopsi mașina în noua culoare DOAR dacă noua
culoare e în opțiunea de culori disponibile, altfel afișați o eroare
● accelerează(viteza) - se va accelera la o anumită viteza, dacă viteza e
negativă-eroare, daca viteza e mai mare decat viteza_max - masina va
accelera până la viteza maximă
● franeaza() - mașina se va opri și va avea viteza 0
"""
#
#
# class Masina:
#     marca = "Hyudai"
#     viteza_actuala = 0
#     culoare = "Gri"
#     culori_disponibile = {"negru", "alb", "rosu", "roz", "maro", "albastru"}
#     inmatriculata = False
#
#     def __init__(self, model, viteza_maxima):
#         self.model = model
#         self.viteza_maxima = viteza_maxima
#
#     def descrie(self):
#         print(f"Masina aleasa este marca {self.marca}, modelul {self.model}, culoarea {self.culoare}, "
#               f"avand viteza maxima {self.viteza_maxima} km/h, viteza actuala fiind {self.viteza_actuala} km/h "
#               f"iar statusul inmatricularii este {self.inmatriculata}")
#
#     def inmatriculare(self):
#         if self.inmatriculata is True:
#             print(f"Masina este deja inmatriculata")
#         else:
#             self.inmatriculata = True
#
#     def vopseste(self, culoare):
#         if culoare.lower() in self.culori_disponibile:
#             self.culoare = culoare
#         else:
#             print(f"Culoarea aleasa nu este in lista de culori disponibile")
#
#     def accelereaza(self, viteza):
#         if viteza < 0:
#             print(f"Masina nu poate accelera cu viteza negativa ")
#         elif viteza > self.viteza_maxima:
#             self.viteza_actuala = self.viteza_maxima
#         else:
#             self.viteza_actuala = viteza
#
#     def franeaza(self):
#         if self.viteza_actuala == 0:
#             print("Masina este deja oprita")
#         else:
#             self.viteza_actuala = 0
#
#
# kona = Masina("Kona", 160)
# kona.descrie()
# print("_" * 100)
# kona.inmatriculare()
# kona.vopseste("verde")
# kona.vopseste("albastru")
# kona.inmatriculare()
# kona.accelereaza(180)
# kona.descrie()
# print("_" * 100)
# kona.franeaza()
# kona.descrie()
#_______________________________________________________________________________________________________________________


"""
3. Clasa TodoList
Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
La început nu avem taskuri, dict e gol și nu avem nevoie de constructor
Metode:

● adauga_task(nume, descriere) - se va adauga in dict
● finalizează_task(nume) - se va sterge din dict
● afișează_todo_list() - doar cheile
● afișează_detalii_suplimentare(nume_task) - în funcție de numele taskului,
printăm detalii suplimentare.
○ Dacă taskul nu e în todo list, întrebam utilizatorul dacă vrea să-l
adauge.
○ Dacă acesta răspunde nu - la revedere
○ Dacă răspunde da - îi cerem detalii task și salvăm nume+detalii în
dict
"""


class TodoList:
    todo = {}

    def __init__(self):
        pass

    def adauga_task(self, nume, descriere):
        self.nume = nume
        self.descriere = descriere
        self.todo.update({self.nume.lower(): self.descriere})

    def finalizeaza_task(self, nume):
        if nume.lower() in self.todo:
            self.todo.pop(nume.lower())
        else:
            print("Task-ul nu este in lista")

    def afiseaza_todo_list(self):
        print(self.todo.keys())

    def afiseaza_detalii_suplimentare(self, nume_task):
        if nume_task.lower() in self.todo:
            print(f"pentru task-ul {nume_task} avem urmatorul mesaj: {self.todo.get(nume_task.lower())}")
        else:
            raspuns = input(f"Task-ul {nume_task} nu este in lista de todo. Vrei sa il adaugi? da/nu?\n").lower()
            if raspuns == "nu":
                print("La revedere")
            elif raspuns == "da":
                detalii_task = input(f" Te rog scrie detaliile taskului\n")
                self.todo.update({nume_task: detalii_task})
            else:
                print("Nu ai raspuns corect cu da sau nu. te rog mai incearca")



cosmin = TodoList()
cosmin.adauga_task("Mancare", "pus mancarea in frigider")
cosmin.afiseaza_todo_list()
cosmin.adauga_task("tema", "Tema trebuie facuta pana vineri")
cosmin.afiseaza_todo_list()
cosmin.afiseaza_detalii_suplimentare("Tema")
print("-" * 100)
cosmin.afiseaza_detalii_suplimentare("pastile")
cosmin.afiseaza_detalii_suplimentare("pastile")
cosmin.afiseaza_todo_list()
print("-" * 100)
cosmin.finalizeaza_task("Mancare")
cosmin.afiseaza_todo_list()
