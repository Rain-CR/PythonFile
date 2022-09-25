# import getpass
#
# #variabila tip string este o variabila ce inregistreaza o insiruire de caractere de la tastatura (ex. un cuvant sau o propozitie)
# """
# Un sting poate contine de exeplu o parola ce are in componenta atat litere cat si cifre sau simboluri
# ex : parola = 1234abc
# """
#
# #declaram si initializam clasa ca sting
# clasa = "Testare automata"
# #declaram si initializam prezenta ca boolian
# prezenta = True
# #definim si initializam numarColegi ca intiger
# numarColegi = 8
# #definim si initializam mediaVarstei ca float
# mediaVarstei = 27.42
# #printam toate informatiile inregsitrate pana acum
# # print(f"Fac parte din clasa {clasa}")
# # print(f'Prezenta mea la curs este {prezenta}')
# # print(f'La curs suntem un total de  {numarColegi} colegi')
# # print(f'Media varstei este fictiva si este de {mediaVarstei} ani')
# # print(type(mediaVarstei))
# # mediaVarstei = round(mediaVarstei)
# # print(f"noua medie a varstei este  {mediaVarstei}")
# # print(type(clasa))
# # print(type(prezenta))
# # print(type(numarColegi))
# # print(type(mediaVarstei))
#
# #----------------------------------------------------------------------------------
#
# #Programul tipareste numere in 3 in 3 incepand cu i = 1  pana la i < 20
# #( ceea ce insemana ca incepand cu cifra 1 pana la 19)
# # for i in range(1,20,3):
# #     print(i)                        # va printa 1,4,7,10,13,16,19
# #
# # #_________________________________________________________________________________
# # #
nume = input(f" Va rog sa scrieti numele")
prenume = input(f" Va rog sa scrieti prenumele")
totalLitere = len(nume) + len(prenume)
print(f"Numele complet are {totalLitere} caractere")
#sau totalLitere = totalLitere.split()
#
#
#
# #__________________________________________________________________________________
# #
lungimea = float(input(f" Va rog sa scrieti lungimea "))
latimea = float(input(f" Va rog sa scrieti latimea "))
aria = lungimea * latimea
print(f'aria dreptungiului este {aria}')

# #__________________________________________________________________________________
#
fact = 'Coral is either the stupidest animal or the smartest rock'
print(fact.count(' the '))
#sau putem creea o categorie noua care sa contina de cate ori apare cuvantul the in propozitie.
theLetters = fact.count("the")
print(f"the word the appears {theLetters} times")

#pentru a numara cate cuvinte avem intr-o propozitie putem numara spatiile si adaugam  + 1
totalWord = fact.count(" ") + 1
print(f"the number of total words is {totalWord} ")
assert isinstance(fact, int)

for cifre in fact:
    if cifre.isnumeric():
        cifre == totalWord
        print(f"the sting contains only numbers")
    else:
        print(f"The sting does not contain only numbers")

#Exerciții Opționale - grad de dificultate: Mediu spre greu

"""
1. Exercițiu:
- citește de la tastatură un string de dimensiune impară;
- afișează caracterul din mijloc.
2. Folosind assert, verifică dacă un string este palindrom.
"""
#
caractere = input(f"va rog scrieti un cuvant sau o propozitie ")
Mij = caractere[(len(caractere)-1)//2:(len(caractere)+2)//2]
print(f"litera de mijloc este {Mij}")
assert caractere == caractere[::-1]
print(f'este palindrom')

#_________________________________________________________________________________________
"""
3. Folosind o singură linie de cod :
- citește un string de la tastatură (ex: 'alabala portocala');
- salvează fiecare cuvânt într-o variabilă;
- printează ambele variabile pentru verificare.
"""

a, b = input('scrie doua cuvinte' ).split(); print(a,"\n",b)

#__________________________________________________________________________________________
"""
Exercițiu:
- citește un string de la tastatură (ex: alabala portocala);
- salvează primul caracter într-o variabilă - indiferent care este el, încearcă
cu 2 stringuri diferite;
- capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul
caracter => alAbAlA portocAla.
"""

cuvant = input("Introdu un doua cuvinte de la tastatura:\n")
prima_litera= cuvant[0] # ne va da prima litera/char
last_index = int(cuvant.rindex(prima_litera)) # asa aflam indexul unde gasim prima litera ultima oara in string de la stanga la dreapta
rest_chars = cuvant[last_index:len(cuvant)] # asa putem face sa printam doar anumite caractere din string dintr-un interval(index)
# important print(string[2:5]) va printa doar caracterele de la index 2 pana la 4 nu si pe cel de la index 5
cuvant = cuvant[1:last_index].replace(prima_litera, prima_litera.upper()) # asa schimbam prima litera in upper in afara de prima aparitie si ultima
cuvant_cu_upper = prima_litera + cuvant + rest_chars
print(cuvant_cu_upper)




#_____________________________________________________________________________________

"""
5.Exercițiu:
- citește un user de la tastatură;
- citește o parolă;
- afișează: 'Parola pt user x este ***** și are x caractere';
- ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să
afișeze corect.
eg: parola abc => ***
parola abcd => ****
"""


user = input(f"Scrieti username ")
password = input(f'Scrieti parola')
pass_length = len(password)
print(pass_length)
show_pass = pass_length * '*'
print(f'Parola pentru user {user} este {show_pass} si are {pass_length} caractere')

#_________________________________________________________________________________________