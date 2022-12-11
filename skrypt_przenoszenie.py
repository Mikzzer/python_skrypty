import os
import time

lista_plikow = os.listdir('.')
for pliki in lista_plikow:
    if '.py' in pliki:
     os.system(f'mv {pliki} /home/mwypa/skrypty/skrypciki')