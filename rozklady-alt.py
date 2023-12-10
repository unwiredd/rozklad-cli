import requests
from bs4 import BeautifulSoup
import re
import lxml

def usuwanko(the_list, val):
   return [value for value in the_list if value != val]

print("Wybierz rodzaj rozkładu:")
print("Tramwaje <1>")
print("Autobusy pośpieszne <2>")
print("Autobusy normalne i strefowe<3>")
print("Autobusy nocne <4>")
print("Autobusy strefowe <5>")

rodzaj = int(input())

if rodzaj == 1:

    print("Podaj numer linii <1-23>")
    linia_t = int(input())

    tramwaje = requests.get(f"http://komunikacja-wroclaw.com/komunikacja-miejska/tramwaje/tramwaj-{linia_t}-wroclaw-rozklad-jazdy")

    zupka_t = BeautifulSoup(tramwaje.content, 'lxml')
    podstawa_t = (zupka_t.find("table", class_="table table-bordered table-schedule hide-to-print").text)


    wynik_t = podstawa_t.split()
    wynik_t.remove('Tramwaj')
    wynik_t.remove('normalny')
    wynik_t.remove('Przesiadki')
    wynik_t.remove('Czas')
    wynik_t.remove('Przystanek')
    wynik_t.remove('(węzeł)')
    print('\n'.join(wynik_t))


elif rodzaj == 2:
    print("Podaj numer linii <A,D,K,N>")
    linia_p = input()
    linia_p = linia_p.lower()
    pospieszne = requests.get(f"http://komunikacja-wroclaw.com/komunikacja-miejska/autobusy/autobus-{linia_p}-wroclaw-rozklad")
    zupka_p = BeautifulSoup(pospieszne.content, 'lxml')
    podstawa_p = (zupka_p.find("table", class_="table table-bordered table-schedule hide-to-print").text)
    wynik_p = podstawa_p.split()
    print('\n'.join(wynik_p))
elif rodzaj == 3:
    print("Podaj numer linii <100-773>")
    linia_n = int(input())
    normalne = requests.get(f"http://komunikacja-wroclaw.com/komunikacja-miejska/autobusy/autobus-{linia_n}-wroclaw-rozklad-jazdy")
    zupka_n = BeautifulSoup(normalne.content, 'lxml')
    podstawa_n = (zupka_n.find("div", class_="uk-article").text)
    wynik_n = podstawa_n.split()

    wynik_n.remove("Autobus")
    wynik_n.remove("Wrocław")
    wynik_n.remove("rozkład")
    wynik_n.remove("jazdy")
    wynik_n.remove("-")
    wynik_n.remove("Comments")
    wynik_n.remove("powered")
    wynik_n.remove("by")
    wynik_n.remove("CComment")
    wynik_n = usuwanko(wynik_n, "Sprawdź")
    wynik_n = usuwanko(wynik_n, "proponowane")
    wynik_n = usuwanko(wynik_n, "przesiadki")
    wynik_n = usuwanko(wynik_n, "na")
    wynik_n = usuwanko(wynik_n, "inne")
    wynik_n = usuwanko(wynik_n, "linie")
    wynik_n = usuwanko(wynik_n, "przystanek")
    wynik_n = usuwanko(wynik_n, "Przystanek")
    wynik_n = usuwanko(wynik_n, "życzenie")




    print('\n'.join(wynik_n))
    #else:
     #   print('\n'.join(wynik_n))
elif rodzaj == 4:
    print("Podaj numer linii <206-259>")
    linia_no = int(input())
    nocne = requests.get(f"http://komunikacja-wroclaw.com/komunikacja-miejska/autobusy/autobus-nocny-{linia_no}-wroclaw-rozklad-jazdy")
    zupka_no = BeautifulSoup(nocne.content, 'lxml')
    podstawa_no = (zupka_no.find("div", class_="uk-article").text)
    wynik_no = podstawa_no.split()

    wynik_no.remove("Autobus")
    wynik_no.remove("Wrocław")
    wynik_no.remove("rozkład")
    wynik_no.remove("jazdy")
    wynik_no.remove("-")
    wynik_no.remove("Comments")
    wynik_no.remove("powered")
    wynik_no.remove("by")
    wynik_no.remove("CComment")
    wynik_no = usuwanko(wynik_no, "Sprawdź")
    wynik_no = usuwanko(wynik_no, "proponowane")
    wynik_no = usuwanko(wynik_no, "przesiadki")
    wynik_no = usuwanko(wynik_no, "na")
    wynik_no = usuwanko(wynik_no, "inne")
    wynik_no = usuwanko(wynik_no, "linie")
    wynik_no = usuwanko(wynik_no, "przystanek")
    wynik_n = usuwanko(wynik_n, "Przystanek")
    wynik_n = usuwanko(wynik_n, "życzenie")


    print('\n'.join(wynik_no))
else:
    print("Nie wybrałeś żadnej z dostępnych opcji.")
    exit()
    
