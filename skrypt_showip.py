import os
from collections import Counter
## skrypt na szukanie w pliku ip i liczenie ile razy sie pokazalo##
## skrypt grepuje w pliku acces ip które logują sie do apacza -> przekazuje ip do pliku a potem ten plik jest odczytywany w pythonie z wynikami kto i ile razy
## szukanie w pliku##
os.system('grep -E -o "^[^^][0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}" /var/log/apache2/access.log > /home/mwypa/skrypty/wynik.txt')

logfile = '/home/mwypa/skrypty/wynik.txt'

i = 0

with open(logfile) as f:
    log = f.readlines()
    c = Counter(log)
    for logs in log:
        print(logs)
    print(f'wyniki : {c}')