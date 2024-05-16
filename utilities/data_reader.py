"""
module with utility functions
"""

import csv
import datetime
#from ..errors import WrongExtention
from openpyxl import load_workbook


month_to_str = lambda x : x if x > 10 else f'0{x}'
day_to_str = lambda x : x if x > 10 else f'0{x}'

HEADER = ['rut', 'rbd', 'peso', 'talla', 'menarquia', 'diagnostico', 'fecha evaluacion']


def validate_row(data:list|tuple, header:list) -> list:
    """
    funcion que toma la data y entrega el indice de las columnas de interes para poder extraer solo
    las columnas necesarias, necesita como argumento la data y el encabezado valido.
    """
    file_header = data[0]
    header_index = [index for index, value in enumerate(file_header) if value.lower() in header]
    return header_index


def open_csv(root, delim=',', new_line='\n')-> list:
    """
    funcion para cargar los datos desde un csv, necesita la ruta del archivo
    delimitador y nueva linea son opcionales.
    """        
    with open (root, new_line, encoding='utf-8') as file:
        data = csv.reader(file, delimiter = f'{delim}')
        lista = list(data)
    return lista        


def generate_report(header, data):
    report = {
        key:0 for key in header
    }

    for line in data:
        for index,item in enumerate(line):
            report[HEADER[index]] += 1

    return report

def validate_data(data:list, valid_index:list) -> list:
    
    valid_data = []

    for line in data:

        valid_line = []
        for index, item in enumerate(line):
            if index in valid_index:
                if isinstance(item, float) or isinstance(item, int):
                    valid_line.append(int(item))

                elif isinstance(item, str):
                    valid_line.append(item)
                elif isinstance(item, datetime.date):
                    valid_line.append(f'{item.year}{month_to_str(item.month)}{day_to_str(item.day)}')
        
        valid_data.append(valid_line)

    return valid_data


def open_excel(root:str, sheet_name:object=None):
    # Carga el archivo Excel
    wb = load_workbook(root)

    # Selecciona la hoja de Excel que quieres leer
    sheet_name = sheet_name if sheet_name else wb.sheetnames[0]
    sheet = wb[sheet_name]
    data = []

    # Itera sobre las filas y columnas del rango deseado en tu hoja de Excel
    for row in sheet.iter_rows(values_only=True):
        data.append(row)

    valid_index = validate_row(data, HEADER)
    valid_data = validate_data(data, valid_index)
    report = generate_report(HEADER, valid_data)
    print(report)
    import pandas as pd
    print(pd.DataFrame(valid_data))
    return valid_data


def get_data(root, delim=',', new_line='\n'):
    if root[-3:] == 'csv':
        return open_csv(root, delim, new_line)
    
    elif root[-4:] == 'xlsx':
        return open_excel(root)

    # else:
    #     raise WrongExtention(f'el archivo {root} tiene extension incorrecta')



if __name__ == '__main__':
    data = open_excel('Tamizaje Los Rios 2024.xlsx')


    for i in data[:10]:
        print(i)
    import pandas as p