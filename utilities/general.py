"""
funcones que realizan tareas generales
"""

from typing import Iterable


def untuple_zip(iter1:Iterable, iter2:Iterable)-> list[list]:
    """
    Esta funcion toma 2 iterables y os zipea, y lo empaqueta en una lista,
    luego la tupla que devuelve el zipeo lo transforma en lista.
    retorna una lista de listas del zip. 
    """
    return [list(item) for item in zip(iter1, iter2)]





if __name__ == '__main__':
    ...