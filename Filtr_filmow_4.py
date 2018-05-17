# program pobierajacy filtrujacy filmy z top 500
import requests
from bs4 import BeautifulSoup

def gatunek_filmu():
    url = ""
    Gatunki = ["Komedia", "Akcja", "Top500", "Dramat", "Wojenny", "Nowości", "Komedia romantyczna"]
    while True:
        x = input("Prosze wybrac gatunek filmu(Top500, Nowości, Komedia, Komedia romantyczna, Akcja, Dramat, Wojenny): ")
        if x not in Gatunki:
            print("Prosze wpisac gatunek poprawnie")
            continue
        else:
            if x == Gatunki[0]:
                url = "http://www.filmweb.pl/ranking/film/Komedia/13"
            elif x == Gatunki[1]:
                url = "http://www.filmweb.pl/ranking/film/Akcja/28"
            elif x == Gatunki[2]:
                url = "http://www.filmweb.pl/ranking/film"
            elif x == Gatunki[3]:
                url = "http://www.filmweb.pl/ranking/film/Dramat/6"
            elif x == Gatunki[4]:
                url = "http://www.filmweb.pl/ranking/film/Wojenny/26"
            elif x == Gatunki[5]:
                url = "http://www.filmweb.pl/ranking/premiere"
            elif x == Gatunki[6]:
                url = "http://www.filmweb.pl/ranking/film/Komedia+rom./30"
            break
    return url

def oceny_filmow():    #pobiera oceny z filmow, zmienia , na . oraz zmienia string na float
    lista_ocen = []
    lista_filmow = []
    for link1 in soup.find_all('span', {'class': 'rate__value'}):
        ocena = link1.string
        ocena = list(ocena)
        ocena[1] = '.'
        ocena = "".join(ocena)
        ocena = float(ocena)
        lista_ocen.append(ocena)

    for link in soup.find_all('a', {'class': 'film__link'}):
        title = link.string
        lista_filmow.append(title)
    dictionary_ocena = dict(zip(lista_filmow, lista_ocen))
    lista_glosow = glosy(url)
    dictionary_glosy = dict(zip(lista_filmow, lista_glosow))
    return dictionary_ocena, dictionary_glosy

def glosy(url):         #pobiera glosy z filmow w formacie np. 123 456 głosów
    glosy_lista = []
    for i in soup.find_all('span', {'class':'rate__count'}):
        glosy = i.string
        glosy_lista.append(glosy)
    glosy_lista1 = glosy_clean(glosy_lista)
    return glosy_lista1

def glosy_clean(glosy_lista):   #zmienia format z def glosy na int
    glosy_lista_clean = []
    for slowo in glosy_lista:
        symbole = "\' głosówy"
        for i in range(0, len(symbole)):
            slowo = slowo.replace(symbole[i], "")
        slowo = int(slowo)
        glosy_lista_clean.append(slowo)
    return glosy_lista_clean

def filtr():
    while True:
        try:
            ocena = float(input("Prosze podac minimalna ocene filmu: "))
            liczba_glosow = int(input("Prosze podac minimalna ilosc glosow: "))
            dictionaries = oceny_filmow()
            dictionary_ocena = dictionaries[0]
            dictionary = dictionaries[1]
            for key, val in dictionary_ocena.items():
                if key in dictionary:
                    dictionary[key] = [val, dictionary[key]]
            for key, val in dictionary.items():
                if dictionary[key][0] >= ocena and dictionary[key][1] >= liczba_glosow:
                    print(key)
                else:
                    print("Brak filmu spełniającego podane warunki.")
                    break
            break
        except ValueError:
            print("Upewnij się, że wpisałeś/wpisałaś liczbę w formacie x.xx dla minimalnej oceny oraz liczbę bez przecinka dla liczby głosów.")

url = gatunek_filmu()
source_code = requests.get(url)  # pobiera caly source code strony pod tym url
plain_text = source_code.text  # przerabia source code na tekst
soup = BeautifulSoup(plain_text, 'html.parser')  # tworzy obiekt soup i dzieki bibliotece BeautifulSoup mozemy przeszukiwac source code

filtr()