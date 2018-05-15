# program pobierajacy filtrujacy filmy z top 500
import requests
from bs4 import BeautifulSoup

url = "http://"
source_code = requests.get(url)  # pobiera caly source code strony pod tym url
plain_text = source_code.text  # przerabia source code na tekst
soup = BeautifulSoup(plain_text, 'html.parser')  # tworzy obiekt soup i dzieki bibliotece BeautifulSoup mozemy przeszukiwac source code


def filmy():
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
    dictionary = dict(zip(lista_filmow, lista_ocen))
    return dictionary

def filtr():
    ocena = float(input("Prosze podac minimalna ocene filmu: "))
    dictionary = filmy()
    dictionary = dict((k,v) for k, v in dictionary.items() if v >= ocena)
    print(dictionary)


filtr()