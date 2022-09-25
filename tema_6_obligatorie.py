import math
"""
1.Clasa Cerc
Atribute: raza, culoare
Constructor pentru ambele atribute
Metode:
● descrie_cerc() - va PRINTA culoarea și raza
● aria() - va RETURNA aria
● diametru()
● circumferinta()
"""

# class Cerc:
#
#     def __init__(self, raza, culoare):
#         self.raza = raza
#         self.culoare = culoare
#
#
#     def descrie_cerc(self):
#         print(f"Culoarea este {self.culoare} iar raza este {self.raza}")
#
#
#     def aria(self):
#         return math.pi * (self.raza * self.raza)
#
#
#     def diametru(self):
#         return 2 * self.raza
#
#
#     def circumferinta(self):
#         return 2 * math.pi * self.raza
#
#
# cerc_rosu = Cerc(3.11, "Rosu")
# cerc_verde = Cerc(-2, "Verde")
#
# cerc_rosu.descrie_cerc()
# cerc_verde.descrie_cerc()
# print("_" * 100)
#
# print(cerc_rosu.aria())
# print(cerc_verde.aria())
# print("_" * 100)
#
# print(cerc_rosu.diametru())
# print(cerc_verde.diametru())
# print("_" * 100)
#
# print(cerc_rosu.circumferinta())
# print(cerc_verde.circumferinta())
#_______________________________________________________________________________________________________________________


"""
2. Clasa Dreptunghi
Atribute: lungime, latime, culoare
Constructor pentru toate atributele
Metode:
● descrie()
● aria()
● perimetrul()
● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
Ea va lua ca și parametru o nouă culoare și va suprascrie atributul
self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei
descrie().
"""
#
# class Dreptunghi:
#
#     def __init__(self, lungime, latime, culoare):
#         self.lungime = lungime
#         self.latime = latime
#         self.culoare = culoare
#
#
#     def descrie(self):
#         print(f"Dreptunghiul are lungimea de {self.lungime}, latimea  de {self.latime} si are culoarea {self.culoare}")
#
#
#     def aria(self):
#         return self.lungime * self.latime
#
#
#     def perimetru(self):
#         return 2 * (self.lungime + self.latime)
#
#
#     def schimba_culoarea(self, noua_culoare):
#         self.culoare = noua_culoare
#
#
# dreptungi_rosu = Dreptunghi(12, 6, "rosu")
# dreptunghi_verde = Dreptunghi( -8.11, -14, "verde")
# dreptunghi_albastru = Dreptunghi(2, -3.14, "albastru")
#
# dreptungi_rosu.descrie()
# dreptunghi_verde.descrie()
# dreptunghi_albastru.descrie()
# print("_" * 100)
# print(f"Aria pentru dreptungi_rosu este {dreptungi_rosu.aria()}")
# print(f"Aria pentru dreptunghi_verde este {dreptunghi_verde.aria()}")
# print(f"Aria pentru dreptungi_albastru este {dreptunghi_albastru.aria()}")
# print("_" * 100)
# print(f"Perimetru pentru dreptunghi_rosu este {dreptungi_rosu.perimetru()}")
# print(f"Perimetru pentru dreptunghi_verde este {dreptunghi_verde.perimetru()}")
# print(f"Perimetru pentru dreptunghi_albastru este {dreptunghi_albastru.perimetru()}")
# print("_" * 100)
# dreptungi_rosu.schimba_culoarea("roz")
# dreptunghi_verde.schimba_culoarea("kaki")
# dreptunghi_albastru.schimba_culoarea("azur")
# dreptungi_rosu.descrie()
# dreptunghi_verde.descrie()
# dreptunghi_albastru.descrie()
#_______________________________________________________________________________________________________________________

"""
3. Clasa Angajat
Atribute: nume, prenume, salariu
Constructor pt toate atributele
Metode:
● descrie()
● nume_complet()
● salariu_lunar()
● salariu_anual()
● marire_salariu(procent)
"""
#
#
# class Angajat:
#
#
#     def __init__(self, nume, prenume, salariu):
#         self.nume = nume
#         self.prenume = prenume
#         self.salariu = salariu
#
#
#     def descriere(self):
#         print(f"Angajatul {self.prenume} {self.nume} are salariu {self.salariu}")
#
#
#     def nume_complet(self):
#         print(f"Numele complet al angajatului este  {self.prenume} {self.nume}")
#
#
#     def salariu_lunar(self):
#         print(f"Salariul lunar al angajatului este {self.salariu}")
#
#
#     def salariu_anual(self):
#         print(f"Salariul anual al angajatului este {12 * self.salariu}")
#
#
#     def marire_salariu(self, procent):
#         self.salariu += (self.salariu * procent) / 100
#         print(f"Angajatul {self.nume} a primit o marire de {procent} procente. Noul salariu este de  {self.salariu}")
#
#
# angajat_1 = Angajat("Craciun", "Cosmin", 1200)
# angajat_2 = Angajat("Gheorghiut", "Gheorghe", 3500)
# angajat_3 = Angajat("Talpaiute", "Moldovan", 5500)
#
# angajat_1.descriere()
# angajat_2.descriere()
# angajat_3.descriere()
# print("_" * 100)
# angajat_1.nume_complet()
# angajat_2.nume_complet()
# angajat_3.nume_complet()
# print("_" * 100)
# angajat_1.salariu_lunar()
# angajat_2.salariu_lunar()
# angajat_3.salariu_lunar()
# print("_" * 100)
# angajat_1.salariu_anual()
# angajat_2.salariu_anual()
# angajat_3.salariu_anual()
# print("_" * 100)
# angajat_1.marire_salariu(15)
# angajat_2.marire_salariu(10)
# angajat_3.marire_salariu(7)
# print("_" * 100)
# angajat_1.descriere()
# angajat_2.descriere()
# angajat_3.descriere()
#_______________________________________________________________________________________________________________________

""""
4.Clasa Cont
Atribute: iban, titular_cont, sold
Constructor pentru toate atributele
Metode:
● afisare_sold() - Titularul x are în contul y suma de n lei
● debitare_cont(suma)
● creditare_cont(suma)
"""
#
#
# class Cont:
#
#
#     def __init__(self, iban, titular_cont, sold):
#         self.iban = iban
#         self.titular_cont = titular_cont
#         self.sold = sold
#
#
#     def afisare_sold(self):
#         print(f"Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} lei")
#
#
#     def debitare_cont(self, suma):
#         if suma > self.sold:
#             print(f"Fonduri insuficiente. aveti in cont {self.sold} lei")
#         else:
#             self.sold -= suma
#             print(f"Ati extras {suma} lei. Mai aveti  {self.sold} lei in cont")
#
#
#     def creditare_cont(self, suma):
#         self.sold += suma
#
#
# cont_1 = Cont("RO001", "Craciun", 2200)
# cont_2 = Cont("RO002", "Gheorghiut", 7300)
# cont_3 = Cont("RO003", "Talpaiute", 15700)
#
# cont_1.afisare_sold()
# cont_2.afisare_sold()
# cont_3.afisare_sold()
# print("_" * 100)
# cont_1.debitare_cont(2300)
# cont_2.debitare_cont(1200)
# cont_3.debitare_cont(0)
# print("_" * 100)
# cont_1.afisare_sold()
# cont_2.afisare_sold()
# cont_3.afisare_sold()
# print("_" * 100)
# cont_1.creditare_cont(1200)
# cont_2.creditare_cont(0)
# cont_3.creditare_cont(-17)
# cont_1.afisare_sold()
# cont_2.afisare_sold()
# cont_3.afisare_sold()
#_______________________________________________________________________________________________________________________