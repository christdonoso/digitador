from time import sleep
from digitador_junaeb_columna import DigitadorJunaebColumna
from utilities.data_reader import get_data
from steps import LOGIN_XPATH, VALIDAR_RUT_DBD, DIGITAR_ATENCION_COLUMNA


URL = 'http://apolo.junaeb.cl:8080/xwsalud/servlet/hwhome'

data = get_data('Comuna Osorno.xlsx')

digitador = DigitadorJunaebColumna(URL)
digitador.login(**LOGIN_XPATH)


data = digitador.validate_rut(actions=VALIDAR_RUT_DBD, data_frame=data)

text = input('Press enter para continuar y una tecla para digitar: ')

try:
    digitador.digitar_atenciones_columna(actions=DIGITAR_ATENCION_COLUMNA, data=data)
except:
    pass

    

