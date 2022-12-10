import os
import datetime
## sprawdza czas i podaje go w normalnych wartosciach##
czas = os.path.getmtime('/home/mwypa/skrypty/wyparlo.jpg')
czas2 = datetime.datetime.fromtimestamp(czas)
czas_teraz = datetime.datetime.now()
print(czas2)
print(czas_teraz)
