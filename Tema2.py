"""
Pentru toate exercițiile se va folosi noțiunea de if în rezolvare.
Indirect vei exersa și operatorii în cadrul condițiilor ramurilor din if.
X poate fi inițializat direct în cod sau citit de la tastatură, după preferințe.
X este un int.
"""

#1. Explică cu cuvintele tale în cadrul unui comentariu cum funcționează un if / else.
"""
Functia If / Else poate fi  vazuta ca o intersectie. Daca (if) se resepecta o anumita conditie codul isi urmeaza calea si face
ce scrie in cod.
Daca nu respecta conditia, atunci (else) va merge pe alta cale si va face ce este specificat dupa else
"""
#_________________________________________________________________________________

#2. Verifică și afișează dacă x este număr natural sau nu.
# x = int(input("Va rog scrieti un numar "))
# if x > 0 :
#     print(" Numarul selectat este un numar natural")
# else:
#     print("Numarul selectat nu este un numar natural")
#________________________________________________________________________________

#3. Verifică și afișează dacă x este număr pozitiv, negativ sau neutru.
# y = int(input("Va rog scrieti un numar "))
# if y > 0:
#     print("Numarul este pozitiv")
# elif y == 0:
#     print("numarul este neutru")
# else:
#     print("Numarul este negativ")
#________________________________________________________________________________

#4. Verifică și afișează dacă x este între -2 și 13.
# x = int(input("Va rog scrieti un numar "))
# if x > -2 < 13 :
#     print(" Numarul selectat este este intre -2 si 13")
# else:
#     print("Mumarul selectat nu este intre -2 si 13")
#________________________________________________________________________________

#5. Verifică și afișează dacă diferența dintre x și y este mai mică de 5.
# x, y = input("Va rog sa scrieti 2 numere \n").split()
# x = int(x)
# y = int(y)
# if x - y < 5:
#     print('Diferenta dintre X si Y este mai mica de 5')
# else:
#     print('Diferenta dintre X si Y este mai mare de 5')
#_______________________________________________________________________________

#6. Verifică dacă x NU este între 5 și 27 - a se folosi ‘not’.
# x = int(input("Va rog scrieti un numar "))
# if not x < 5 and not x > 27:
#     print(" Numarul selectat este intre 5 si 27")
# else:
#     print("Mumarul selectat NU este intre 5 si 27")
#________________________________________________________________________________

#7.x și y (int).Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai mare
# x, y = input("Va rog sa scrieti 2 numere \n").split()
# x = int(x)
# y = int(y)
# if x == y:
#     print('X este egal cu Y')
# elif x < y:
#     print('Y este mai mare decat X')
# else:
#     print('X este mai mare decat Y')
#_________________________________________________________________________________

#8.X, y, z - laturile unui triunghi. Afișează dacă triunghiul este isoscel, echilateral sau oarecare.

# x, y, z = input("Va rog scrieti 3 numere intregi mai mari de 0. \n").split()
# x = float(x)
# y = float(y)
# z = float(z)
# if x <= 0 or y <= 0 or z <=0:
#     print("Nu ati selecta numere intregi. va rog selectati numere mai mari decat 0")
# elif x == y == z:
#     print("Triunghiul este echilateral")
# elif x == y  or x == z or y == z:
#     print("Triunghiul este isoscel")
# else:
#     print("Triunghiul este oarecare ")
#______________________________________________________________________________

#9. Citește o literă de la tastatură. Verifică și afișează dacă este vocală sau nu
# litera = input('Scrieti o singura litera de la tastatura ').lower()
# vocale = "a", "e", "i", "o", "u"
# cifre = "1", "2", "3", "4", "5", "6", "7", "8", "9"
# if len(litera) > 1:
#     print('Ati scris mai mult de o litera. Va rog scrieti o singura litera')
# elif litera in vocale:
#     print('Litera scrisa este vocala')
# elif litera in cifre:
#     print('Ati scris o cifra. Va rog scrieti o litera din alfabet')
# else:
#     print('Litera scrisa este consoana')
#________________________________________________________________________________

"""10.Transformă și printează notele din sistem românesc în >
Peste 9 => A
Peste 8 => B
Peste 7 => C
Peste 6 => D
Peste 4 => E
4 sau sub => F
"""
# nota = float(input('Va rog sa scrieti o nota de la 1 la 10 '))
# if nota > 10 or nota <= 0:
#     print('Ati ales un numar si nu nota. Va rog scrieti un numar de la 1 la 10')
# elif nota >= 9 <= 10:
#     print("Aveti nota A")
# elif nota >= 8 < 9:
#     print("Aveti nota B")
# elif nota >= 7 < 8:
#     print("Aveti nota C")
# elif nota >= 6 < 7:
#     print("Aveti nota D")
# elif nota >= 4 < 6:
#     print("Aveti nota E")
# elif nota < 4:
#     print("Aveti nota F")
#_____________________________________________________________________________________

"""
Exerciții Opționale - grad de dificultate: Mediu spre greu - might need Google.
1.Verifică dacă x are minim 4 cifre (x e int).
(ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
"""
# numar = int(input("Scrieti un numar din cate cifre doriti"))
# print(type(numar))
# numar = str(numar)
# if len(numar) >= 4:
#     print("Lungimea numarului este mai mare de 4 cifre")
# else:
#     print("Lungimea numarului este mai mica de 4 cifre")
#_____________________________________________________________________________________

#2.Verifică dacă x are exact 6 cifre.
# numar = int(input("Scrieti un numar din cate cifre doriti"))
# print(type(numar))
# print(numar)
# if numar < 0 :
#     lungime_numar_negativ = len(str(numar))-1
#     if not lungime_numar_negativ == 6:
#         print("Lungimea numarului nu este de 6 cifre")
#     else:
#         print("Lungimea numarului este de 6 cifre")
# elif len(str(numar)) == 6:
#     print("Lungimea numarului este de 6 cifre")
# else:
#     print("Lungimea numarului nu este de 6 cifre")
#__________________________________________________________________________________

#3.Verifică dacă x este număr par sau impar (x e int).
# numar = int(input("Scrieti un numar"))
# if numar % 2 == 0:
#     print("Numarul este par")
# else:
#     print("Numarul este inpar")
#___________________________________________________________________________________

#4. x, y, z (int). Afișează care este cel mai mare dintre ele?

# x, y, z = input("Te rog scrie 3 numere diferentiate cu spatiu").split()
# x = int(x)
# y = int(y)
# z = int(z)
# if x > y and x > z:
#     print(f"{x} este cel mai mare numar ales de tine")
# elif y > x and y > z:
#     print(f"{y} este cel mai mare numar ales de tine")
# else:
#     print(f"{z} este cel mai mare numar ales de tine")
#__________________________________________________________________________________

#5. X, y, z - reprezintă unghiurile unui triunghi. Verifică și afișează dacă triunghiul este valid sau nu.
# x, y, z = input(" Va rog scrieti 3 valori pentru unghiurile unui triunghi. ele insumate trebuiesc sa fie 180. Valorile nu pot fi negative\n").split()
# x = float(x)
# y = float(y)
# z = float(z)
# suma_unghiurilor = x+y+z
# if x <= 0 or y <= 0 or z <= 0:
#     print("Ati selectat un unghi prea mic iar triunghiul NU este valid. Va rog selectati 3 valori care insumate sa dea 180")
# elif suma_unghiurilor < 180:
#     print('Suma unghiurilor este mai mica de 180 grade iar triunghiul NU este valid. Va rog selectati 3 valori care insumate sa dea 180')
# elif suma_unghiurilor > 180:
#     print('Suma unghiurilor este mai mare de 180 grade iar triunghiul NU este valid. Va rog selectati 3 valori care insumate sa dea 180')
# else:
#     print("Suma unghiurilor este de 180 grade iar triunghiul este Valid. FELICITARI!!!")
#_________________________________________________________________________________________________

"""
6. Având stringul: 'Coral is either the stupidest animal or the smartest rock'
● Citiți de la tastatură un int x
● Afișează stringul fără ultimele x caractere
Exemplu: daca ati ales 7 => 'Coral is either the stupidest animal or the smarte'
"""
# prop = 'Coral is either the stupidest animal or the smartest rock'
# x = int(input('selectati de la tastatura o valoare cuprinsa intre 0 si 57'))
# print(prop[:(-x)])

#7.Același string. Declară un string nou care să fie format din primele 5 caractere + ultimele 5
# prop_noua = prop[:5] + prop[-5:]
# print(prop_noua)

#__________________________________________________________________________________________________

"""
8. Același string.
● Salvează într-o variabilă și afișează indexul de start al cuvântului rock (hint:
este o funcție care te ajuta sa faci asta)
● Folosind această variabilă + slicing, afișează tot stringul până la acest
cuvant
● output: 'Coral is either the stupidest animal or the smartest '
"""
# prop = 'Coral is either the stupidest animal or the smartest rock'
# rock_index = prop.rfind("rock")
# print(prop[:rock_index])
#_________________________________________________________________________________________________

#9. Citește de la tastatura un string.
# Verifică dacă primul și ultimul caracter sunt la fel. Se va folosi un assert
# Atentie: se dorește ca programul sa fie case insensitive - 'apA' e acceptat
# prop = input('Scrieti un cuvand sau o propozitie la alegere.  \n')
# first_char = prop[0]
# last_char = prop[-1]
# assert first_char.lower() == last_char.lower()
# print("Litera de inceput si de sfarsit este aceeasi")
#_________________________________________________________________________________________________

"""
10. Avand stringul '0123456789'
● Afișați doar numerele pare
● Afișați doar numerele impare
(hint: folositi slicing, controlați din pas)
"""
# x = '0123456789'
# print(x[::2])
# print(x[1::2])

#_________________________________________________________________________________________________

"""
Exerciții Bonus (may need google) .
11. Joc ghicit zarul
Caută pe net și vezi cum se generează un număr random
Ne imaginăm ca dai cu zarul și salvăm acest număr în dice_roll

Luați un numărul ghicit de la utilizator
Verificați și afișați dacă utilizatorul a ghicit
Veți avea 3 opțiuni
● Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y
● Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y
● Ai ghicit. Felicitari! Ai ales x si zarul a fost y
"""
# import random
# dice_roll = random.randint(1,6)
# print(dice_roll)
# numar_ales = int(input("Alegeti un numar de la 1 la 6 pentru a ghici valoarea zarului"))
# if numar_ales < dice_roll:
#     print(f"Ai pierdut. Ai ales un numar mai mic. Ai ales {numar_ales} dar a fost {dice_roll}")
# elif numar_ales > dice_roll:
#     print(f"Ai pierdut. Ai ales un numar mai mare. Ai ales {numar_ales} dar a fost {dice_roll}")
# else:
#     print(f"Ai ghicit. Felicitari! Ai ales {numar_ales} si zarul a fost {dice_roll}")