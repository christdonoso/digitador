from digitador import Digitador
from utilities import general
from pandas import DataFrame
from time import sleep


class DigitadorJunaeb(Digitador):
    """
    clase para poder digitar las diferentes atenciones de junaeb
    """

    def validate_rut(self, actions:list, data_frame:DataFrame):
        """
        funcion para validar si los rut estan correctos y el rbd que trae la data es el correcto.
        """

        self.click('//*[@id="span_W0022_OPCIONES_0001"]/a/img')
        data_frame = data_frame
        data = general.untuple_zip(data_frame['RUT'], data_frame['RBD'])

        for idx,d in enumerate(data):
            for accion in actions:
                if accion[1] == 'send keys':
                    self.send_key(accion[0], d[0])
                    sleep(1)

                elif accion[1] == 'click':
                    self.click(accion[0])
                    sleep(1)
                
                elif accion[1] == 'get text':
                    rbd = self.get_text(accion[0])
            
            if rbd != str(d[1]):
                data[idx][1] = rbd
                print('RBD modificado')
            else:
                print('el RBD esta correcto')

        data_frame['RUT'] = [row[0] for row in data]
        data_frame['RBD'] = [row[1] for row in data]
        print(data_frame)
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