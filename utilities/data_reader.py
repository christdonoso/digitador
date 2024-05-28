"""
module with utility functions to import data
"""

import csv
import datetime
#from errors.data_errors import WrongExtention
import pandas as pd
from openpyxl import load_workbook


month_to_str = lambda x : x if x > 10 else f'0{x}'
day_to_str = lambda x : x if x > 10 else f'0{x}'

HEADER = ['rut', 'rbd', 'peso', 'talla', 'menarquia', 'diagnostico', 'fecha evaluacion']
UPPER_HEADER = [word.upper() for word in HEADER]


def open_csv(root, delim=',', new_line='\n')-> list:
    """
    funcion para cargar los datos desde un csv, necesita la ruta del archivo
    delimitador y nueva linea son opcionales.
    """        
    with open (root, new_line, encoding='utf-8') as file:
        data = csv.reader(file, delimiter = f'{delim}')
        lista = list(data)
    return lista        


def validate_data(data:list) -> list:
    """
    funcion que toma la data y valida los datos, y los deja en formato de entero
    y de fechas como strings
    """
    valid_data = []

    for row in data:

        valid_row = []
        for item in row:
            if isinstance(item, float) or isinstance(item, int):
                valid_row.append(int(item))

            elif isinstance(item, str):
                valid_row.append(item)

            elif isinstance(item, datetime.date):
                valid_row.append(f'{item.year}{month_to_str(item.month)}{day_to_str(item.day)}')
            else:
                valid_row.append(item)
        
        valid_data.append(valid_row)

    return valid_data


def validate_dataframe(valid_data:list, header=HEADER, upper_header=UPPER_HEADER)-> pd.DataFrame:
    """
    Funcion que recibe una lista con la data valida como lista y devuelve un dataframe 
    validado
    """
    valid_header = header if header in valid_data[0] else upper_header
    df = pd.DataFrame(valid_data[1:], columns=valid_data[0])[valid_header]

    return df


def open_excel(root:str, sheet_name:object=None):
    wb = load_workbook(root)

    sheet_name = sheet_name if sheet_name else wb.sheetnames[0]
    #sheet_name = sheet_name if sheet_name else [sheet_name for sheet_name in wb.sheetnames]
    
    sheet = wb[sheet_name]
    data = []

    # Itera sobre las filas y columnas del rango deseado en tu hoja de Excel
    for row in sheet.iter_rows(values_only=True):
        data.append(row)

    valid_data = validate_data(data)
    valid_dataframe = validate_dataframe(valid_data)

    return valid_dataframe.head()


def get_data(root, delim=',', new_line='\n'):
    """
    Funcion para cargar la data, esta puede venir en formato CSV o 
    en un XLSX, de lo contratio, da un error
    """
    if root[-3:] == 'csv':
        return open_csv(root, delim, new_line)
    
    elif root[-4:] == 'xlsx':
        return open_excel(root)

#    else:
#        raise WrongExtention(f'el archivo {root} tiene extension incorrecta')


if __name__ == '__main__':
    data = open_excel('Tamizaje Los Rios 2024.xlsx')
    print(data)