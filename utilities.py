"""
module with utility functions
"""

import csv
from errors import WrongExtention
from openpyxl import load_workbook


def validate_row(data):
    HEADER = ['rut','peso', 'talla', 'menarquia', 'diagnostico', 'fecha']
    

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


def open_excel(root:str, sheet_name:object=None):
    # Carga el archivo Excel
    wb = load_workbook(root)

    sheet_name = sheet_name if sheet_name else wb.sheetnames[0]

    # Selecciona la hoja de Excel que quieres leer
    sheet = wb[sheet_name]

    # Inicializa una lista para almacenar los datos
    data = []

    # Itera sobre las filas y columnas del rango deseado en tu hoja de Excel
    for row in sheet.iter_rows(values_only=True):
        data.append(row)

    return data


def get_data(root, delim=',', new_line='\n'):
    if root[-3:] == 'csv':
        return open_csv(root, delim, new_line)
    
    elif root[-4:] == 'xlsx':
        return open_excel(root)

    else:
        raise WrongExtention(f'el archivo {root} tiene extension incorrecta')



if __name__ == '__main__':
    print(get_data('Tamizaje Los Rios 2024.xls'))