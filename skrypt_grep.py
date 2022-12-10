import os

zmienna = input("Podaj ścieżke pliku: ")
ilosc_wierszy = int(input("Liczba wierszy w dwie strony: "))
patern = input("Patern: ")
lokalizacja_zapisu = input("Podaj gdzie sie ma zapisywac: ")
pakowanie = input("Czy chcesz pakowac : tak/nie")
if pakowanie == 'tak':
    os.system(f'grep -C {ilosc_wierszy} {patern} {zmienna} > {lokalizacja_zapisu}')
    lokalizacja_zapisu = lokalizacja_zapisu
    os.system(f'gzip {lokalizacja_zapisu}')
else:
    os.system(f'grep -C {ilosc_wierszy} {patern} {zmienna} > {lokalizacja_zapisu}')
