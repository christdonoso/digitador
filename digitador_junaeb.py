from time import sleep
from digitador import Digitador
from steps import LOGIN_XPATH

class DigitadorJunaeb(Digitador):
    """
    Objeto que trae los metodos genericos para digitar atenciones
    """
    URL = 'http://apolo.junaeb.cl:8080/xwsalud/servlet/hwhome'

    def __init__(self, url:str = URL):
        super().__init__(url)

    def digitar_tamizaje(self):
        self.click('//*[@id="span_W0022_OPCIONES_0002"]/a/img')
        sleep(1)
        self.click('//*[@id="span_W0022_OPCIONES_0001"]/a/img')
        sleep(1)
        self.select('//*[@id="TABLE2"]/tbody/tr[1]/td[2]/select[1]')
        sleep(1)
        self.select('//*[@id="TABLE2"]/tbody/tr[2]/td[2]/select')
        sleep(1)



if __name__ == '__main__':
    d = DigitadorJunaeb()
    d.login(**LOGIN_XPATH)
    input('')
    d.digitar_tamizaje()
