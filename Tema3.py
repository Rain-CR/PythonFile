"""
Pentru toate exercițiile se va folosi noțiunea de if în rezolvare.
Indirect vei exersa și operatorii în cadrul condițiilor ramurilor din if.
X poate fi inițializat direct în cod sau citit de la tastatură, după preferințe.
X este un int.
"""
"""
1. Declară o listă note_muzicale în care să pui do re mi etc până la do
● Afișeaz-o
● Inversează ordinea folosind slicing și suprascrie această listă.
● Printează varianta actuală (inversată).
● Pe această listă aplică o metodă care bănuiești că face același lucru,
adică să îi inverseze ordinea. Nu trebuie să o suprascrii în acest caz,
deoarece metoda face asta automat.
● Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta
inițială.
"""
# music_sheat = [ 'do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
# print(music_sheat)
# music_revers = music_sheat[::-1]
# print(music_revers)
# music_revers.reverse()
# print(F'The new reversed list is {music_revers}')
"""
Concluzii: slicing e temporar, dacă vrei să păstrezi noua variantă va trebui să
suprascrii lista sau să o salvezi într-o listă nouă. Metoda găsită de tine face
suprascrierea automat și permanentizează aceste modificări. Ambele variante
își găsesc utilitatea în funcție de ce ne dorim în acel moment.
"""
#________________________________________________________________________________________________

#2. De câte ori apare ‘do’?
# music_sheat = [ 'do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
# print(music_sheat.count('do'))
#_______________________________________________________________________________________________

#3.Având 2 liste, [3, 1, 0, 2] și [6, 5, 4] - Găsește 2 variante să le unești într-o singură listă.
# a = [3, 1, 0, 2]
# b = [6, 5, 4]
# new_list = a + b
# print(new_list)
# new_list2 = a
# print(new_list2)
# new_list2 = new_list2.__add__(b)
# print(new_list2)
#____________________________________________________________________________________________

"""
4.
● Sortează și afișază lista generată la exercițiul anterior.
● Sterge numărul 0 folosind o funcție.
● Afișaza iar lista.

"""
# same_list = [3, 1, 0, 2, 6, 5, 4]
# print(same_list)
# same_list.sort()
# print(same_list)
# del same_list[0]
# print(same_list)

#_____________________________________________________________________________________________

"""
5. Folosind un if verifică lista generată la exercițiul 3 și afișază:
● Lista este goală.
● Lista nu este goală.
"""
# same_list = [3, 1, 0, 2, 6, 5, 4]
# print(len(same_list))
# if len(same_list) != 0:
#     print("Lista nu este goala")
# else:
#     print('Lista este goala')
#____________________________________________________________________________________________

#6. Folosește o funcție care să șteargă lista de la exercițiul 3.
# same_list = [3, 1, 0, 2, 6, 5, 4]
# print(same_list)
# same_list.clear()   #cu clear stergem toate elementele din lista
# print(same_list)
# del same_list       #cu del stergem lista.
# print(same_list)    # Va da eroare pentru ca nu mai exista lista definita
#____________________________________________________________________________________________

#7. Copy paste la exercițiul 5. Verifică încă o dată. Acum ar trebui să se afișeze că lista e goală.
# same_list = []
# print(len(same_list))
# if len(same_list) != 0:
#     print("Lista nu este goala")
# else:
#     print('Lista este goala')
#____________________________________________________________________________________________

#8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5} Folosește o funcție că să afișezi Elevii (cheile)
# dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# print(f"Elevii din clasa sunt {dict1.keys()}")
#____________________________________________________________________________________________

#9. Printează cei 3 elevi și notele lor Ex: ‘Ana a luat nota {x}’ Doar nota o vei lua folosindu-te de cheie
# dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# print(f"Ana a luat nota {dict1['Ana']}")
# print(f"Gigel a luat nota {dict1['Gigel']}")
# print(f"Dorel a luat nota {dict1['Dorel']}")
#____________________________________________________________________________________________

"""
10. Dorel a făcut contestație și a primit 6
● Modifică nota lui Dorel în 6
● Printează nota după modificare
"""
# dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# print(f"Dorel a avut nota {dict1['Dorel']} inainte de contestatie.")
# dict1['Dorel'] = 6
# print(dict1)
# print(f"Dupa contestatie Dorel are nota {dict1['Dorel']}. ")
#____________________________________________________________________________________________

"""
11. Gigel se transferă din clasă
● Căuta o funcție care să îl șteargă
● Vine un coleg nou. Adaugă Ionică, cu nota 9
● Printează noii elevi
"""
# dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# print(dict1)
# del dict1['Gigel']
# print(dict1)
# dict1['Ionel'] = 9
# print(dict1)
# print(f"Elevii din clasa sunt {dict1.keys()}")
#____________________________________________________________________________________________

"""12.Set
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
● Adaugă în zilele_sapt ‘luni’
● Afișeaza zile_sapt
"""
# zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
# weekend = {'sâmbăta', 'duminică'}
# print(zile_sapt)
# zile_sapt.add('luni')
# print(zile_sapt)
#____________________________________________________________________________________________

"""
13.Folosește un if și verifică dacă:
● Weekend este un subset al zilelor din săptămânii.
● Weekend nu este un subset al zilelor din săptămânii.
"""
# zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
# weekend = {'sâmbăta', 'duminică'}
# if weekend.issubset(zile_sapt):
#     print("Weekend este un subset al zilelor din săptămânii")
# else:
#     print("Weekend nu este un subset al zilelor din săptămânii.")
#____________________________________________________________________________________________

#14. Afișează diferențele dintre aceste 2 seturi.
# zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
# weekend = {'sâmbăta', 'duminică'}
# print(zile_sapt.difference(weekend))
#____________________________________________________________________________________________

#15. Afișază intersecția elementelor din aceste 2 seturi.
# zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
# weekend = {'sâmbăta', 'duminică'}
# print(zile_sapt.intersection(weekend))
#____________________________________________________________________________________________

"""
Exerciții Opționale - grad de dificultate: Mediu spre greu(may need google) .
1. Ne imaginăm o echipă de fotbal pt teren sintetic.
3 Schimbări maxime admise:

● Declară o Listă cu 5 jucători
● Schimbari_efectuate = te joci tu cu valori diferite
● Schimbari_max = 3
Dacă Jucătorul x e în teren și mai avem schimbări la dispoziție
- Efectuează schimbarea

- Șterge jucătorul scos din listă
- Adaugă jucătorul intrat
- Afișaza a intra x, a ieșit y, mai ai z schimbări
Dacă jucătorul nu e în teren:
- Afișază ‘ nu se poate efectua schimbarea deoarece jucătorul x nu e în
teren’
- Afișază ‘mai ai z schimbări’
Testează codul cu diferite valori
"""
# jucatori = ['hagi','pelle','messi','mutu', 'ronaldo']
# Schimbari_efectuate = 0
# Schimbari_max = 3
#
# while Schimbari_efectuate < Schimbari_max:
#     jucator_schimbat = input('Selecteaza jucatorul care doresti sa fie schimbat')
#     noul_jucator = input("Alege un nou jucator care sa intre in teren")
#     if jucator_schimbat in jucatori:
#         jucatori.remove(jucator_schimbat)
#         jucatori.append(noul_jucator)
#         Schimbari_efectuate += 1
#         print(f'A intrat {noul_jucator}, a iesit {jucator_schimbat} si mai ai {(Schimbari_max - Schimbari_efectuate)} schimbari')
#         print(jucatori)
#     else:
#         print(f"nu se poate efectua schimbarea deoarece jucătorul {jucator_schimbat} nu e în teren")
#         print(f"mai ai {(Schimbari_max-Schimbari_efectuate)} schimbări")
# print('Nu mai ai schimbari de facut.')

#_______________________________________________________________________________________________________________________
"""
Acelasi exercitiu dar cu Dict.
Posibilitate de selectare a jucatorului pe baza pozitiei sale in teren si selectandu-se dupa numarul de pe tricou.
"""
jucatori_teren = {11: ["Hagi", "Mijlocas"], 7: ["Pelle", "Mijlocas"], 9: ["Messi", "Aparator"], 2: ["Mutu", "Portar"], 1: ["Ronaldo", "Atacant"]}
rezerve = {3: ["Marius", "Mijlocas"], 4: ["Emil", "Mijlocas"], 5: ["Eugen", "Portar"], 6: ["Alin", "Atacant"], 10: ["Petricau", "Aparator"]}
Schimbari_efectuate = 0
Schimbari_max = 3
print(f"Regulile jocului sunt simple: ai 5 oameni pe teren si 5 rezerve. poti face maxim 3 schimbari.\n"
      f" Nu poti inlocui un portar cu atacant.\n "
      f"La orice moment va trebui sa ai pe teren minim un jucator de fiecare tip : Portar, aparare, mijlocas si atacant\n"
      f"_________________________________________________________________________________________________________________")
while Schimbari_efectuate < Schimbari_max:
      print(f"Urmatorii jucatori sunt pe teren:")
      for key, value in jucatori_teren.items():
            print(key, ':', value)
      jucator_schimbat = int(input('Selecteaza jucatorul de pe teren pe care doresti sa il schimbi. Scrie numarul de pe tricou aferent jucatorului '))
      if jucator_schimbat in jucatori_teren:
            print(f"Ati selectat urmatorul jucator pe care doriti sa il scoateti de pe teren {jucatori_teren[jucator_schimbat]}")
            print('____________________________________________________________________________________________________________')
      else:
            print("Jucatorul nu se afla pe teren. Daca doresti sa rejoci jocul te rog fi atent la numarul de pe tricou")
            print('____________________________________________________________________________________________________________')
            continue

      print(f"Urmatorii jucatori sunt pe banca de rezerva:")
      for key, value in rezerve.items():
            print(key, ':', value)
      rezerva_schimbare = int(input("Alege un nou jucator din lista de rezerve care sa intre in teren. Scrie numarul de pe tricou aferent jucatorului "))
      if rezerva_schimbare in rezerve:
            print(f"Ati selectat urmatorul jucator pe care doriti sa il bagati pe teren {rezerve[rezerva_schimbare]}")
            print('____________________________________________________________________________________________________________')
            if jucatori_teren[jucator_schimbat][1] == rezerve[rezerva_schimbare][1] == "Portar":
                  print(f'Ai scos de pe teren un {jucatori_teren[jucator_schimbat][1]} si ai bagat in teren un {rezerve[rezerva_schimbare][1]}')
            elif jucatori_teren[jucator_schimbat][1] in {"Aparator", "Mijlocas"} and rezerve[rezerva_schimbare][1] in {"Aparator", "Mijlocas"}:
                  print(f'Ai scos de pe teren un {jucatori_teren[jucator_schimbat][1]} si ai bagat in teren un {rezerve[rezerva_schimbare][1]}')
            elif jucatori_teren[jucator_schimbat][1] in {"Mijlocas", "Atacant"} and rezerve[rezerva_schimbare][1] in {"Mijlocas", "Atacant"}:
                  print(f'Ai scos de pe teren un {jucatori_teren[jucator_schimbat][1]} si ai bagat in teren un {rezerve[rezerva_schimbare][1]}')
            else:
                  print(f"Ai selectat un jucator gresit si vei ramane fara o pozitie ocupata. Ai ales scos un {jucatori_teren[jucator_schimbat][1]} si ai bagat in teren un {rezerve[rezerva_schimbare][1]}. Te rog sa fii mai atent la tactica ")
                  continue
      else:
            print("Jucatorul nu se afla pe banca de rezerve. Fii atent cand alegi numarul de pe tricou")
            print('____________________________________________________________________________________________________________')
            continue
      Schimbari_efectuate += 1
      print(f'A intrat {rezerve[rezerva_schimbare]}, a iesit {jucatori_teren[jucator_schimbat]} si mai ai {(Schimbari_max - Schimbari_efectuate)} schimbari')
      print('____________________________________________________________________________________________________________')
      del jucatori_teren[jucator_schimbat]
      rez_buff = {rezerva_schimbare: rezerve[rezerva_schimbare]}
      jucatori_teren.update(rez_buff)
      del rezerve[rezerva_schimbare]

else:
      print(f"Nu mai ai mutari de facut.")

