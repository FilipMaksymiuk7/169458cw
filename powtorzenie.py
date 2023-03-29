import math
#zad 1
# def liczby(a,b):
#     try:
#         a != int or b != int
#     except ValueError:
#         print("To nie jest liczba calkowita")
#     else:
#         print('o')
#
# a = int(input('Podaj 1 liczbe'))
# b = int(input('Podaj 2 liczbe'))
#
# liczby(a,b)
#
# wynik = a ** 2 + a * b + b ** 2
# wynik2 = str(wynik)
# with open('zadanie1.txt','w+') as plik:
#     for x in wynik2:
#         plik.write(x)


#zad 2
# def listy(lista1=[],lista2=[]):
#     nowa = []
#     for x in lista1:
#         print(lista1[x])

#zad3
# zmienna = ''
# with open('zadanie1.txt','r',encoding='utf8') as plik:
#     for x in plik:
#             zmienna += plik.read(70)
#


# with open('zadanie1.txt','w',encoding='utf8') as plik:
#     for x in plik:
#         tekst += pli



#zad4
# lista = [1,2,3,4]
# a = 2
# nowa = [x for x in lista if a<x]
# print(nowa)
#


#zad 5
# matematyczne =(math.exp(3)+math.cos(39)**2)**(1/5) + (2/7)**3 + math.pi
# print(str(round(matematyczne, 2)))



#BBBBBBBBBBBBBBBBBBBBBBBBBBBBBB

#zad2
lista = [2,3,4.0,5.34,3,3.3,3.33]

nowa = [x for x in lista if x %1 !=0]
print(lista)
print(nowa)

#zad3



#zad4


wynik = math.sin(56)**2+ (((4**2)/25)+math.log(3,85))**(1/4)
wynik = round(wynik,2)
print(wynik)













