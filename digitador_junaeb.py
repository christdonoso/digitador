"""
documentacions de esta clase // construir
"""

from digitador import Digitador
from pandas import DataFrame
from time import sleep
from utilities import general
import steps

class DigitadorJunaeb(Digitador):
    """
    clase para poder digitar las diferentes atenciones de junaeb
    """

    def __init__(self, url:str):
        super().__init__(url)
        self.xpat_columna_normal = steps.ATENCION_COLUMNA_NORMAL
        self.xpat_columna_escoliosis = steps.ATENCION_COLUMNA_ESCOLIOSIS
        self.xpat_columna_dorsocurvo = steps.ATENCION_COLUMNA_DORSOCURVO

    def validate_rut(self, actions:list, data_frame:DataFrame):
        """
        funcion para validar si los rut estan correctos y el rbd que trae la data es el correcto.
        """
        #---FALTA TERMINAR ESTE METODO---#
        self.click('//*[@id="span_W0022_OPCIONES_0001"]/a/img')
        data_frame = data_frame
        data = general.untuple_zip(data_frame['RUT'], data_frame['RBD'])

        for idx,d in enumerate(data):
            for action in actions:
                if action[1] == 'send keys':
                    self.send_key(action[0], d[0])
                    sleep(1)

                elif action[1] == 'click':
                    self.click(action[0])
                    sleep(1)
                
                elif action[1] == 'get text':
                    rbd = self.get_text(action[0])
            
            if rbd != str(d[1]):
                data[idx][1] = rbd
                print('RBD modificado')
            else:
                print('el RBD esta correcto')

        data_frame['RUT'] = [row[0] for row in data]
        data_frame['RBD'] = [row[1] for row in data]
        print(data_frame)

    def digitar_atenciones_columna(self, actions:list, data:DataFrame):

        for indx,row in data.iterrows():
            item_row = list(row)
            for action in actions:
                print(item_row)
                if action[1] == 'send keys':
                    self.send_key(action[0], item_row[0])
                    item_row.pop(0)
                    sleep(1)
                
                elif action[1] == 'click':
                    self.click(action[0])
                    sleep(1)
                
                elif action[1] == 'click checkbox':
                    self.click_checkbox(action[0])
                    sleep(1)

                elif action[1] == 'try element':
                    self.try_click_element(action[0])
                
                elif action[1] == 'call_self_method':
                    self.digit_diagnosis(item_row[0])
            
            print(f'Estudiante numero {indx + 1} digitado')
            break

    def digit_diagnosis(self, diagnosis:str):
        if diagnosis.lower() == 'sano':
            self.columna_normal()
        elif diagnosis.lower() =='escoliosis':
            self.columna_escoliosis()
        elif diagnosis.lower() == 'dorsocurvo':
            self.columna_dorsocurvo()

    def columna_normal(self):
        for xpath in self.xpat_columna_normal:
            self.click(xpath)

    def columna_escoliosis(self):
        for xpath in self.xpat_columna_escoliosis:
            self.click(xpath)

    def columna_dorsocurvo(self):
        for xpath in self.xpat_columna_dorsocurvo:
            self.click(xpath)

    """
    optimizacion del codigo.
    # Crear un diccionario que mapee el tipo de acción a la función correspondiente
acciones_funciones = {
    'send keys': self.send_key,
    'click': self.click,
    'click checkbox': self.click_checkbox
}

for accion, parametro in acciones:
    print(accion)
    # Obtener la función correspondiente al tipo de acción del diccionario
    funcion = acciones_funciones.get(accion)
    if funcion:
        # Llamar a la función con el parámetro correspondiente
        funcion(parametro)
        sleep(1)
    else:
        print(f"No se encontró una función para la acción: {accion}")
    """