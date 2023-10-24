# Obligatorio: Generar una tabla usando Python con TODOS los ficheros (recursivamente) del workspace que contenga el nombre del fichero, el peso REAL y la última fecha de modificación.
# Opcional: Hacer lo mismo que en la línea anterior pero en Bash Scripting y exportando un CSV
import os
import time
import pandas as pd

#actual rute
dir = os.getcwd()

#files list

files = os.listdir(dir)

#function size

def get_size(x):
    return os.path.getsize(x)

#function time

def get_time(x):
    return time.ctime(os.path.getmtime(x))

#size files list
size = [get_size(file) for file in files]

#last modification files list
time_ = [get_time(file) for file in files]

#covert lists in DataFrame
data_dir = pd.DataFrame({'files': files,'size': size,'time': time_})

#generate csv
data_dir.to_csv('table_files.csv', index=False)
