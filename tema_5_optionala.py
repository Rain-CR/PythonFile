from calendar import monthrange


"""
1. Funcție care primește o lună din an și returnează câte zile are acea luna
"""
#cu import calendar
#
#
# def calculate_days_per_month(year, month):
#     return monthrange(year, month)[1]
#
#
# print(calculate_days_per_month(2022,5))

#fara import calendar
#
#
# def calculate_days_per_month(month):
#     month = month.lower()
#     if month == "january":
#         print("Luna are 31 de zile")
#     elif month == "february":
#         print("Luna are 28 de zile")
#     elif month == "march":
#         print("Luna are 31 de zile")
#     elif month == "april":
#         print("Luna are 30 de zile")
#     elif month == "may":
#         print("Luna are 31 de zile")
#     elif month == "june":
#         print("Luna are 30 de zile")
#     elif month == "july":
#         print("Luna are 31 de zile")
#     elif month == "august":
#         print("Luna are 31 de zile")
#     elif month == "september":
#         print("Luna are 30 de zile")
#     elif month == "october":
#         print("Luna are 31 de zile")
#     elif month == "november":
#         print("Luna are 30 de zile")
#     elif month == "december":
#         print("Luna are 31 de zile")
#     else:
#         print('Nu ai scrisc corect. Te rog reincearca')
#
#
# calculate_days_per_month("april")
#_______________________________________________________________________________________________________________________

"""
2. Funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea,
împărțirea a două numere.
În final vei putea face:
a, b, c, d = calculator(10, 2)
● print("Suma: ", a)
● print("Diferenta: ", b)
● print("Inmultirea: ", c)
● print("Impartirea: ", d)
"""
#
#
# def calculate_all(x, y):
#     sum = x + y
#     dif = x - y
#     mul = x * y
#     div = x / y
#     return sum, dif, mul, div
#
#
# sum, dif, mul, div = calculate_all(5, 7)
# print("Suma numerelor este: ", sum)
# print("Diferenta numerelor este: ", dif)
# print("Inmultirea numerelor da : ", mul)
# print("Impartirea numerelor da: ", div)
#_______________________________________________________________________________________________________________________

"""
3. Funcție care primește o lista de cifre (adică doar 0-9)
Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
Returnează un DICT care ne spune de câte ori apare fiecare cifră
=> dict {
0: 0
1 :2
2: 0
3: 1
4: 0
5: 3
6: 0
7: 2
8: 0
9: 1
}
"""
#
#
# def calculate_number_occurance(number_list):
#     dict_list = {}
#     for n in range(0, 10):
#         dict_list.update({n: number_list.count(n)})
#     return dict_list
#
#
# number_list = [1, 3, 1, 5, 9, 7, 7, 5, 5]
# print(calculate_number_occurance(number_list))
#_______________________________________________________________________________________________________________________

"""
4. Funcție care primește 3 numere. Returnează valoarea maximă dintre ele
"""
#
# def compared_max_value(x, y, z):
#     if x > y and x > z:
#         return  x
#     elif y > x and y > z:
#         return y
#     else:
#         return z
#
#
# print(compared_max_value(-219, -271, -33))
#_______________________________________________________________________________________________________________________

"""
5. Funcție care să primească un număr și să returneze suma tuturor numerelor
de la 0 la acel număr
Exemplu: daca dam nr 3. Suma va fi 6 (0+1+2+3)
"""
#
#
# def exponential_sum(numer):
#     sum = 0
#     for n in range(0, numer+1):
#         sum +=n
#     return sum
#
#
# print(exponential_sum(33))
#_______________________________________________________________________________________________________________________


# OPTIONALE BONUS

"""1.Funcție care primește 2 liste de numere (numerele pot fi dublate). Returnați
numerele comune

Exemplu:
list1 = [1, 1, 2, 3]

list2 = [2, 2, 3, 4]
Răspuns: {2, 3}
"""
list1 = [1, 1, 2, 3, 7, 4, 6]
list2 = [2, 2, 3, 4, 6]

#aici rezolvarea cu ajutor de la google.
# def common_element(list_1, list_2):
#     common_list = {element for element in list_1 if element in list2}
#     return common_list
#
#print(common_element(list1, list2))


#aici rezolvarea mea "ingenioasa" pentru a face set si a printa ca in rezolvare. initial cu metoda asta imi lua dictionar nu Set
# def common_element(list_1, list_2):
#     common_list = {True}
#     for element in list_1:
#         if element in list_2:
#             common_list.add(element)
#     common_list.remove(True)
#     return common_list
#
# print(common_element(list1,list2))
#_______________________________________________________________________________________________________________________

"""
2.. Funcție care să aplice o reducere de preț
Dacă produsul costa 100 lei și aplicăm reducere de 10%. Pretul va fi 90
Tratați cazurile în care reducerea e invalida. De exemplu o reducere de 110% e
invalidă.
"""
#
#
# def discount_calculator(price, discount):
#     if discount < 100:
#         new_price = price - (discount*price/100)
#         print(f'New price is {new_price} currency.')
#     else:
#         print('Invalid discount. Try again')
#
#
# discount_calculator(170, 80)
#_______________________________________________________________________________________________________________________

import datetime


"""
3. Funcție care să afișeze data și ora curentă din ro
(bonus: afișați și data și ora curentă din China)  *** Not finished ***
"""
#
#
# def show_date_and_time(country):
#     if country == "Romania":
#         now = datetime.datetime.now()
#         print("Current date and time in Romania is : ")
#         print(now.strftime("%Y-%m-%d %H:%M:%S"))
#
#


"""
4. Funcție care să afișeze câte zile mai sunt până la ziua ta / sau până la
Crăciun dacă nu vrei să ne zici cand e ziua ta :)
"""
#
#
# def crhistmas_countdown(year, month, day):
#     dt = datetime.datetime
#     cr_year = year
#     cr_month = 12
#     cr_day = 25
#     if cr_year == year and month == 12 and day >= 25:
#         cr_year += 1
#     time_left = dt(cr_year, cr_month, cr_day) - dt(year, month, day)
#     print(f"Days left until Christmas : {time_left.days}")
#
#
# crhistmas_countdown(2022, 9, 9)

#si automat fara sa mai punem noi anul, luna, ziua:
#
#
# def crhistmas_countdown(year=True, month=True, day=True):
#     dt = datetime.datetime
#     now = dt.now()
#     cr_year = now.year
#     cr_month = 12
#     cr_day = 25
#     if cr_year == year and now.month == 12 and now.day >= 25:
#         cr_year += 1
#     time_left = dt(cr_year, cr_month, cr_day) - dt(year=now.year, month=now.month, day=now.day)
#     print(f"Days left until Christmas : {time_left.days}")
#
#
# crhistmas_countdown()



