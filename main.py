from time import sleep
from digitador import DigitadorJunaeb
from utilities import get_data
from steps import LOGIN_XPATH


URL = 'http://apolo.junaeb.cl:8080/xwsalud/servlet/hwhome'
data = get_data()

digitador = DigitadorJunaeb(URL)
digitador.login(**LOGIN_XPATH)

sleep(10)