from time import sleep
from digitador_junaeb import DigitadorJunaeb
from utilities.data_reader import get_data
from steps import LOGIN_XPATH, VALIDAR_RUT_DBD


URL = 'http://apolo.junaeb.cl:8080/xwsalud/servlet/hwhome'

data = get_data('Tamizaje Los Rios 2024.xlsx')

digitador = DigitadorJunaeb(URL)
digitador.login(**LOGIN_XPATH)
input('Press enter para continuar: ')
digitador.validate_rut(actions=VALIDAR_RUT_DBD, data_frame=data)

