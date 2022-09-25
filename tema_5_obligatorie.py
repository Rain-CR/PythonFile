

"""
1.Funcție care să calculeze și să returneze suma a două numere
"""


# def sum_of_two(a, b):
#     return a+b
#
#
# a = int(input("Scrieti primul numar \n"))
# b = int(input("Scrieti al doilea numar \n"))
# print(f"Suma cifrelor {a} si {b} este {sum_of_two(a,b)}")
# print(f'Suma este {sum_of_two(7, 6)}')
#_______________________________________________________________________________________________________________________

"""
2. Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar
"""


# def is_odd(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False
#
#
# print(is_odd(12))
#_______________________________________________________________________________________________________________________

"""
3. Funcție care returnează numărul total de caractere din numele tău complet.
(nume, prenume, nume_mijlociu)
"""


# def total_name_char(name, surname, middle_name = None):
#     if middle_name == None:
#         return  len(name) + len(surname)
#     else:
#         return len(name) + len(surname) + len(middle_name)
#
#
# name = input("write your name \n")
# surname = input("write your surname \n")
# middle_name = input("write your middle name \n")
# print(f"The total number of characters in your name is {total_name_char(name,surname,middle_name)}")
# print(total_name_char('Cosmin', 'Craciun'))
#_______________________________________________________________________________________________________________________

"""
4. Funcție care returnează aria dreptunghiului
"""


# def arie_dreptunghi(lungime, latime):
#     return float(lungime) * float(latime)
#
#
# lungime = input("Scrieti lungimea dreptunghiului")
# latime = input("Scrieti latimea dreptunghiului")
# print(f"Aria dreptunghiului este de {arie_dreptunghi(lungime, latime)} cm patrati ")
# print(arie_dreptunghi(12.5, 7.42))
#_______________________________________________________________________________________________________________________

"""
5. Funcție care returnează aria cercului
"""
#
#
# def aria_cercului(raza):
#     return 3.14 * (raza * raza)
#
#
# raza = float(input("Scrieti raza cercului"))
# print(f"Aria cercului este {aria_cercului(raza)}")
# print(aria_cercului(3.12))
#_______________________________________________________________________________________________________________________

"""
6. Funcție care returnează True dacă un caracter x se găsește într-un string dat
și Talse dacă nu găsește.
"""
#
#
# def find_char_in_strng(char, strng):
#     for character in strng.lower():
#         if character == char.lower():
#             return True
#     else:
#         return False
#
#
# char = input("Selectati caracterul pe care doriti sa il cautati \n")
# strng = input("Scrieti propozitia in care doriti sa cautati caracterul \n")
# print(find_char_in_strng(char, strng))
# print(find_char_in_strng("f", "In America cea mai mica nota este F"))
#_______________________________________________________________________________________________________________________

"""
7. Funcție fără return, primește un string și printează pe ecran:
● Nr de caractere lower case este x
● Nr de caractere upper case exte y
"""
#
#
# def upper_lower_calculator(strng):
#     upper_case = 0
#     lower_case = 0
#     for char in strng:
#         if char.isupper():
#             upper_case += 1
#         elif char.islower():
#             lower_case += 1
#         else:
#             pass
#     print(f" Your string is:  {strng}")
#     print(f' Your string contains {upper_case} with upper case letter')
#     print(f' Your string contains {lower_case} with lower case letter')
#
#
# upper_lower_calculator("Hello World. Let`s all be friends")
#_______________________________________________________________________________________________________________________

"""
8. Funcție care primește o LISTA de numere și returnează o LISTA doar cu
numerele pozitive
"""
#
#
# def positive_numbers(numbers):
#     positive_list = []
#     for number in numbers:
#         if number >= 0:
#             positive_list.append(number)
#     print(f"Numerele pozitive din lista ta sunt {positive_list}")
#
#
# positive_numbers([5, 21, -4, -77, -0.25, 3.14])
#_______________________________________________________________________________________________________________________

"""
9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
● Primul număr x este mai mare decat al doilea nr y
● Al doilea nr y este mai mare decat primul nr x
● Numerele sunt egale.
"""
#
#
# def higher_number(a, b):
#     if a > b:
#         print(f'Primul număr {a} este mai mare decat al doilea nr {b}')
#     elif a < b:
#         print(f'Al doilea nr {b} este mai mare decat primul nr {a}')
#     else:
#         print('Numerele sunt egale.')
#
#
# a = int(input("Scrieti primul numar \n"))
# b = int(input('Scrieti al doilea numar \n'))
# higher_number(a, b)
# higher_number(-20, -21)
#_______________________________________________________________________________________________________________________

"""
10. Funcție care primește un număr și un set de numere.
● Printeaza ‘am adaugat numărul nou în set’ + returnează True
● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ +
returnează False
"""


def set_update(number, set):
    if number in set:
        print('Nu am adaugat numărul în set. Acesta există deja')
        return False
    else:
        set.add(number)
        print('Am adaugat numărul nou în set')
        return True

number = 6.11
set = {6.11, 22, -5.4, 7.3}
set_update(number, set)
set_update(4.3, {22.41, 7, -9.3, 12})
#_______________________________________________________________________________________________________________________