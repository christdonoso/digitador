"""
module with utility functions
"""

import csv


def open_csv(root, delim=',', new_line='\n')-> list:
    """_summary_
    metodo para cargar los datos desde un csv
    Args:
        root (str): ruta del archivo
        delim (str): simbolo de delimitacion del archivo
    Returns:
        _type_: _description_
    """        

    with open (root, new_line, encoding='utf-8') as file:
        data = csv.reader(file, delimiter = f'{delim}')
        lista = list(data)
    return lista        


def get_data(root, delim=',', new_line='\n'):
    if root[-3:] == 'csv':
        open_csv(root, delim, new_line)