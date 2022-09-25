
"""
1.
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
Itereaza prin listă alte_numere
Populează corect celelalte liste
Afișeaza cele 4 liste la final
"""
# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_pare = []
# numere_impare = []
# numere_pozitive = []
# numere_negative = []
# for n in alte_numere:
#     if n > 0:
#         numere_pozitive.append(n)
#     else:
#         numere_negative.append(n)
#     if n % 2 == 0:
#         numere_pare.append(n)
#     else:
#         numere_impare.append(n)
# print(f'Numerele pare sunt : {numere_pare}')
# print(f'Numerele impare sunt : {numere_impare}')
# print(f'Numerele pozitive sunt: {numere_pozitive}')
# print(f'Numerele negative sunt : {numere_negative}')
#_______________________________________________________________________________________________________________________
"""
2. Aceeași listă:
Ordonează crescător lista fară să folosești sort.
Te poți inspira vizual de aici.
https://www.youtube.com/watch?v=lyZQPjUT5B4
"""
# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# n = 0
# alte_numere_sortate = []
# while len(alte_numere) > 0:
#     alte_numere_sortate.append(min(alte_numere))
#     alte_numere.remove(min(alte_numere))
#     n += 1
# print(alte_numere_sortate)
#_______________________________________________________________________________________________________________________

"""
3. Ghicitoare de număr:
numar_secret = Generați un număr random între 1 și 30
Numar_ghicit = None
Folosind un while
User alege un număr

Programul îi spune:
● Nr secret e mai mare
● Nr secret e mai mic
● Felicitări! Ai ghicit!
"""
# import random
#
# numar_secret = random.randint(1,30)
# numar_ghicit = None
#
# while numar_ghicit != numar_secret:
#     numar_ghicit = int(input(" Alege un numar intre 1 si 30 \n"))
#     if numar_ghicit > numar_secret:
#         print('Nr secret e mai mic')
#     elif numar_ghicit < numar_secret:
#         print('Nr secret e mai mare')
#     else:
#         print(f'Felicitari! Ai ghicit')
#_______________________________________________________________________________________________________________________

"""
4. Alege un număr de la tastatură
Ex: 7
Scrie un program care să genereze în consolă următoarea piramidă
1
22
333
4444
55555
666666
7777777

Ex:3
1
22
333
"""
# nr = int(input("Va rog alegeti o cifra de la 1 la 10\n"))
# for n in range(nr):
#     for i in range(n+1):
#         print(n+1,end=" ")
#     print('\n')
#_______________________________________________________________________________________________________________________

"""
5.
tastatura_telefon = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9],
[0]
]
Iterează prin listă 2d
Printează ‘Cifra curentă este x’
(hint: nested for - adică for în for)
"""
# tastatura_telefon = [
# [1, 2, 3],
# [4, 5, 6],
# [7, 8, 9],
# [0]
# ]
# for n in tastatura_telefon:
#     for i in n:
#         print(f'Cifra curentă este {i}')
#_______________________________________________________________________________________________________________________

"""
Se da un string (o sa ti-l dau eu). Foloseste cicluri repetitve pentru a numara toate vocalele din string (a, e, i, o, u)
"""
# prop = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
# a = 0
# e = 0
# i = 0
# o = 0
# u = 0
# for v in prop.lower():
#     if v == "a":
#         a += 1
#     elif v == "e":
#         e += 1
#     elif v == "i":
#         i +=1
#     elif v == "o":
#         o += 1
#     elif v == "u":
#         u += 1
# else:
#     print(f'Vocala "a" se regaseste de {a} ori')
#     print(f'Vocala "e" se regaseste de {e} ori')
#     print(f'Vocala "i" se regaseste de {i} ori')
#     print(f'Vocala "o" se regaseste de {o} ori')
#     print(f'Vocala "u" se regaseste de {u} ori')
#_______________________________________________________________________________________________________________________

"""
Se citesc doua numere naturale de la tastatura, sa se afiseze toate numerele prin aflate in intervalul x si y
De exemplu, daca se citesc numerele 25 si 50, ar trebui sa afisez
29,  31, 37, 41, 43, 47
"""
# num_1 = int(input(f'Va rog scrieti primul numar cuprins intre 1 si 999 \n'))
# num_2 = int(input(f'Va rog scrieti al doilea numar cuprins intre 1 si 999 \n'))
# numar_prim = []
# if num_1 < num_2:
#     for numar in range(num_1, num_2):
#         if numar > 1:
#             for i in range(2, numar):
#                 if (numar % i) == 0:
#                     break
#             else:
#                 numar_prim.append(numar)
# else:
#     for numar in range(num_2, num_1):
#         if numar > 1:
#             for i in range(2, numar):
#                 if (numar % i) == 0:
#                     break
#             else:
#                 numar_prim.append(numar)
# print(f'Numerele prime in intervalul selectat sunt urmatoarele :\n{numar_prim}')
#_______________________________________________________________________________________________________________________

"""
First Factorial
Have the function FirstFactorial(num) take the num parameter being passed and return the factorial of it. 
For example: if num = 4, then your program should return (4 * 3 * 2 * 1) = 24. 
For the test cases, the range will be between 1 and 18 and the input will always be an integer. 
 Input: 4
Output: 24

Input: 8
Output: 40320 
"""
#Exercitiul cere sa se faca folosind urmatoarele elemente:
"""def FirstFactorial(num):
   
  # code goes here
  return num

# keep this function call here 
print(FirstFactorial(input()))
"""

#Rezolvare simpla facuta cu elemente cunoscute
# num = int(input(f"Please select a number between 1 and 18\n"))
# first_factorial = 1
# if 1 <= num <= 18:
#     for i in range(1, num+1):
#         first_factorial *= i
#
# print(first_factorial)