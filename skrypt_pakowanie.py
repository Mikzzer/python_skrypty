import os, sys
from pathlib import Path

##sciezka = input("Podaj sciezke pliku")

##sprawdza wielkosc pliku/folderu/
file_size = os.path.getsize('/home/mwypa/skrypty/WYPARLO1.jpg')
print("File Size is :", file_size, "bytes")
wielkosc = file_size * 0.000001
print(f"wielkosc {wielkosc} Mb")
if wielkosc > 2:
    os.system(f'gzip /home/mwypa/skrypty/WYPARLO1.jpg')
    print("Plik byl za duzy! spakowano!")