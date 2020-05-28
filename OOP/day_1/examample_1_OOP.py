# Implementacja obiektowa

class Konto:
    def __init__(self, stan_poczatkowy, imie, nazwisko, numer):
        print("Jestem metodą __init__")
        # Atrybut obiektu \/
        self.stan = stan_poczatkowy
        # Atrybut obiektu /\ o nazwie stan
        self.imie = imie
        self.nazwisko = nazwisko
        self.numer = numer

    def wplac(self, kwota):
        self.stan += kwota

    def wyplac(self, kwota):
        if self.stan >= kwota:
            self.stan -= kwota
            return kwota
        else:
            raise Exception('Nie ma wystarczajcej kwoty na koncie. ')

    def pokaz_detale(self):
        string = self.imie + " " + self.nazwisko + " " + str(self.stan) + " " + str(self.numer)
        return string

    def przelej(self, kwota, konto_odbiorcy):
        zmienna = self.wyplac(kwota)
        konto_odbiorcy.wplac(zmienna)


konto = Konto(0, 'Artur', 'Siepietowski', 123456775)
print(konto)
print(konto.pokaz_detale())
konto.wplac(100)

print(konto.pokaz_detale())

konto1 = Konto(1000, 'Kamil', 'Martynek', None)
konto.przelej(50, konto1)
print(konto.pokaz_detale())
print(konto1.pokaz_detale())
