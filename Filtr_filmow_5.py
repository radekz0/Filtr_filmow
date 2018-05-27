#Pająk po popularnej stronie z rankingami i ocenami filmów.
import requests
from bs4 import BeautifulSoup


class filtr_filmow:

    def __init__(self):
        self.gatunek_filmu()
        self.source_code = requests.get(self.url)  #Pobiera caly source code strony pod tym url.
        self.plain_text = self.source_code.text  #Przerabia source code na tekst.
        self.soup = BeautifulSoup(self.plain_text,
                                  'html.parser')  #Tworzy obiekt soup i dzieki bibliotece BeautifulSoup mozemy przeszukiwac source code.

    def gatunek_filmu(self):
        self.url = ""
        Gatunki = ["Komedia", "Akcja", "Top500", "Dramat", "Wojenny", "Nowości", "Komedia romantyczna"]
        while True:
            x = input(
                "Prosze wybrac gatunek filmu(Top500, Nowości, Komedia, Komedia romantyczna, Akcja, Dramat, Wojenny): ")
            if x not in Gatunki:
                print("Prosze wpisac gatunek poprawnie")
                continue
            else:
                if x == Gatunki[0]:
                    self.url = "http://"
                elif x == Gatunki[1]:
                    self.url = "http://"
                elif x == Gatunki[2]:
                    self.url = "http://"
                elif x == Gatunki[3]:
                    self.url = "http://"
                elif x == Gatunki[4]:
                    self.url = "http://"
                elif x == Gatunki[5]:
                    self.url = "http://"
                elif x == Gatunki[6]:
                    self.url = "http://"
                break

    def glosy(self):  #Pobiera glosy z filmow w formacie np. 123 456 głosów.
        self.glosy_lista = []
        for i in self.soup.find_all('span', {'class': 'rate__count'}):
            glosy = i.string
            self.glosy_lista.append(glosy)

    def glosy_clean(self):  #Czysci glosy z niepotrzebnych znaków oraz przerabia je na format int.
        self.glosy()
        self.glosy_lista_clean = []
        for slowo in self.glosy_lista:
            symbole = "\' głosówy"
            for i in range(0, len(symbole)):
                slowo = slowo.replace(symbole[i], "")
            slowo = int(slowo)
            self.glosy_lista_clean.append(slowo)

    def filmy(
            self):  #Zmienia format oceny z np. 8,55 na 8.55, oraz tworzy dwa dictionary: {"Nazwa filmu": ocena} oraz {"Nazwa filmu": liczba glosow}.
        lista_ocen = []
        lista_filmow = []
        for link1 in self.soup.find_all('span', {'class': 'rate__value'}):
            ocena = link1.string
            ocena = list(ocena)
            ocena[1] = '.'
            ocena = "".join(ocena)
            ocena = float(ocena)
            lista_ocen.append(ocena)
        for link in self.soup.find_all('a', {'class': 'film__link'}):
            title = link.string
            lista_filmow.append(title)
        self.dictionary_ocena = dict(zip(lista_filmow, lista_ocen))
        self.glosy_clean()
        self.dictionary_glosy = dict(zip(lista_filmow, self.glosy_lista_clean))

    def filtr(
            self):  #Tworzy pojedyncze dictionary w formie {"Nazwa filmu": [ocena, liczba glosow]}, co pozwala na filtrowanie filmów uzależnione od obu parametrów jednoczesnie.
        self.filmy()
        while True:
            try:
                ocena = float(input("Prosze podac minimalna ocene filmu: "))
                liczba_glosow = int(input("Prosze podac minimalna ilosc glosow: "))
                for key, val in self.dictionary_ocena.items():
                    if key in self.dictionary_glosy:
                        self.dictionary_glosy[key] = [val, self.dictionary_glosy[key]]
                for key, val in self.dictionary_glosy.items():
                    if self.dictionary_glosy[key][0] >= ocena and self.dictionary_glosy[key][1] >= liczba_glosow:
                        print(key)
                        break
                    else:
                        print("Brak filmu spełniającego podane warunki.")
                        break
                break
            except ValueError:
                print(
                    "Upewnij się, że wpisałeś/wpisałaś liczbę w formacie x.xx dla minimalnej oceny oraz liczbę bez przecinka dla liczby głosów.")


a = filtr_filmow()
a.filtr()