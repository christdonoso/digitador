from digitador import Digitador
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

class DigitadorJunaebAudio(Digitador):

    def digitar_audio(self,rut,rbd, fecha):
        """_summary_
        Metodo para digitar atenciones de examenes de audiometria
        Args:
            rut (_type_): _description_
            rbd (_type_): _description_
            fecha (_type_): _description_
        """                
        # self.driver.find_element(By.XPATH,'//*[@id="_BENSALRUT"]').click()
        self.driver.find_element(By.XPATH,'//*[@id="_BENSALRUT"]').send_keys(rut)
        self.driver.find_element(By.XPATH,'//*[@id="_COLCOD"]').click()
        self.driver.find_element(By.XPATH,'//*[@id="_COLCOD"]').send_keys(rbd)
        self.driver.find_element(By.XPATH,'//*[@id="TABLE2"]/tbody/tr[5]/td/span/input').click()
        self.driver.find_element(By.XPATH,'//*[@id="TABLE1"]/tbody/tr/td[2]/input').click()
        self.driver.find_element(By.XPATH,'//*[@id="span__OPCIONES_0001"]/a/img').click()

        self.driver.find_element(By.XPATH,'//*[@id="CTLFMFECIND"]').click()
        self.driver.find_element(By.XPATH,'//*[@id="CTLFMFECIND"]').send_keys(fecha)
        self.driver.find_element(By.XPATH,'//*[@id="TABLE17_0001"]/tbody/tr/td[7]/span/input').click()
        self.driver.find_element(By.XPATH,'//*[@id="TABLE7"]/tbody/tr/td[1]/input').click()

        sleep(1)
        self.driver.switch_to.alert.accept()
        sleep(3)
        self.driver.find_element(By.XPATH,'//*[@id="TABLE7"]/tbody/tr/td[2]/input').click()

if __name__ == '__main__':
    import csv
    from steps import LOGIN_XPATH

    with open('ATENCIONES MAYO.csv') as file:
        data = csv.reader(file, delimiter=';')
        data = list(data)

        URL = 'http://apolo.junaeb.cl:8080/xwsalud/servlet/hwhome'
    for i in range(110):
        data.pop(0)
 
    digitador = DigitadorJunaebAudio(URL)
    digitador.login(**LOGIN_XPATH)  

    input('press enter: ')
    for idx,value in enumerate(data):
        digitador.digitar_audio(value[1], value[6], value[0].replace('-', '/'))
        print(f'Estudiante {idx + 1} digitado')

