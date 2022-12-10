import os
import time

##pakowaczka logów jak jest starsze niż dzień to są gzipowane##

#pobieranie sciezki#
log_directory = '/home/mwypa/skrypty/logi'

current_time = time.time()

for filename in os.listdir(log_directory):
    filepath = os.path.join(log_directory, filename)
    last_modified = os.path.getmtime(filepath)
    time_difference = current_time - last_modified
    if time_difference > 86400:
        os.system(f'gzip {filepath}')
