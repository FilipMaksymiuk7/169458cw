 #zad1
plik = open("nowy.txt","w+")
for x in range(31):
    x = x*2
    plik.write(str(x)+",")



plik.close()

plik = open("nowy.txt","r")

for x in plik:
    print(x)

plik.close()


with open("nowe.txt", "w") as file:
    file.write("dobry napis!")


with open("nowe.txt","r") as plik:
    for linia in plik:
        print(linia,end="")

print(" ")
class NaZakupy:

    def __init__(self,nazwa_produktu,ilosc,jednostka_miary,cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka_miary = jednostka_miary
        self.cena_jed = cena_jed
    def wyswietl_produkt(self):
        print(self.nazwa_produktu)
    def ile_produktu(self):
        print(self.ilosc,self.jednostka_miary)
    def ile_kosztuje(self):
        cena = self.cena_jed * self.ilosc
        print(cena,"zl")


o = NaZakupy("deski",5,"szt",8)
o.wyswietl_produkt()
o.ile_produktu()
o.ile_kosztuje()


class Ciagi:
    def __init__(self,x,y,r):
        self.x = x
        self.y = y
        self.r = r

    def wyswietl_dane(self):
        print("pierwszy wyraz ciagu:",self.x)
        print("ostatni wyraz ciagu:",self.y)
        print("roznica w ciagu:",self.r)

    def pobierz_parametry(self):
        self.x = int(input("podaj 1 wyraz ciagu"))
        self.y = int(input("podaj ostatni wyraz ciagu"))
        self.r = int(input("podaj roznice"))

    def pobierz_elementy(self):
        pass

    def policz_sume(self):
        suma =0
        a = self.x
        b= self.y
        c = self.r
        while(a<=b):
            suma += a
            a += c
        print(suma)
    def policz_elementy(self):
        ile =0
        a = self.x
        b= self.y
        c = self.r
        while(a<b):
            ile += 1
            a += c

        print(ile)
f = Ciagi(0,0,0)
f.pobierz_parametry()
f.wyswietl_dane()
f.policz_elementy()
f.policz_sume()



