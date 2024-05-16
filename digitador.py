"""
use selenium==4.20.0
"""

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class Digitador:
    """_summary_
    Clase para poder digitar las atenciones de junaeb
    """       

    def __init__(self, url:str):
        """_summary_
        funcion iniciadora que para poder digitar, se debe tener en la misma carpeta 
        el webdriver correspondiente.
        Args:
            url (_type_, optional): _description_. Defaults to URL.
        """        
        options = Options()
        options.add_experimental_option('detach', True)
        #self.driver = webdriver.Chrome() forma antigua en donde habia que bajar el chomedriver especifico de la version a utilizar
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.get(url)
        sleep(2)
   
    def login(self, user:str, user_xpath:str,
               pswd:str, pswd_xpath:str, login_xpath:str, captcha = True):
        """
        metodo que realiza accion de logeado de un usuario, si captcha es true, 
        espera 7 segundos para poder escribir el captcha
        """
        self.driver.find_element(By.XPATH, user_xpath).send_keys(user)
        self.driver.find_element(By.XPATH, pswd_xpath).send_keys(pswd)
        sleep(7) if captcha else None
        self.driver.find_element(By.XPATH, login_xpath).click()

    def click(self, xpath:str) -> None:
        """
        metodo para clickear en la instancia, debe recibir el xpath de 
        de lo que se desea clickear
        """
        self.driver.find_element(By.XPATH, xpath).click()

    def write(self, xpath:str, text:str):
        """
        metodo para escribir algun input de la instancia, debe recibir el xpath
        del input que se desea escribir y el mensaje.
        """
        self.driver.find_element(By.XPATH,xpath).send_keys(text) 

    def click_alert(self):
        """
        metodo para clickear en alerts
        """
        self.driver.switch_to.alert.accept()

    def digitar_columna(self, region=str):
        """
        Metodo que posiciona en la seccion de digitar tamizajes de columna

        Args:
            region (_type_, optional): region donde se realizaron las atenciones.
        """        
        
        self.driver.find_element(By.XPATH,'//*[@id="span_W0022_OPCIONES_0002"]/a/img').click() 
        self.driver.find_element(By.XPATH,'//*[@id="span_W0022_OPCIONES_0001"]/a/img').click() 
        self.driver.find_element(By.XPATH,'//*[@id="TABLE2"]/tbody/tr[1]/td[2]/select[1]').click() 
        sleep(1)
        self.driver.find_element(By.XPATH,'//*[@id="TABLE2"]/tbody/tr[1]/td[2]/select[1]').send_keys(region) 
        sleep(1)
        self.driver.find_element(By.XPATH,'//*[@id="TABLE2"]/tbody/tr[1]/td[2]/select[1]').send_keys(Keys.ENTER) 

        self.driver.find_element(By.XPATH,'//*[@id="TABLE2"]/tbody/tr[2]/td[2]/select').click() 
        sleep(1)
        self.driver.find_element(By.XPATH,'//*[@id="TABLE2"]/tbody/tr[2]/td[2]/select').send_keys('76797') 
        self.driver.find_element(By.XPATH,'//*[@id="TABLE2"]/tbody/tr[2]/td[2]/select').send_keys(Keys.ENTER) 

    def digitador(self):
        self.driver.find_element(By.XPATH,'//*[@id="TABLE2"]/tbody/tr[2]/td[2]/select').click()
        self.driver.find_element(By.XPATH,'//*[@id="TABLE2"]/tbody/tr[2]/td[2]/select').send_keys('tamizaje')
        sleep(1)
        self.driver.find_element(By.XPATH,'//*[@id="TABLE2"]/tbody/tr[2]/td[2]/select').send_keys(Keys.ENTER) 

        self.driver.find_element(By.XPATH,'//*[@id="TABLE2"]/tbody/tr[3]/td[2]/select').click()
        self.driver.find_element(By.XPATH,'//*[@id="TABLE2"]/tbody/tr[3]/td[2]/select').send_keys('17118602')
        sleep(1)
        self.driver.find_element(By.XPATH,'//*[@id="TABLE2"]/tbody/tr[2]/td[2]/select').send_keys(Keys.ENTER) 
        sleep(1)

        self.driver.find_element(By.XPATH,'//*[@id="TABLE1"]/tbody/tr/td[3]/input').click()


    
    def insert_atencion(self, rut,rbd, diagnostico, peso, talla):
        """
        digita los datos de cada atencion
        Args:
            rut (_type_): rut usuario
            diagnostico (_type_): diagnostico del usuario
            peso (_type_): peso en kg
            talla (_type_): talla en cm
        """        
        self.driver.find_element(By.XPATH,'//*[@id="_BENSALRUT"]').send_keys(rut) 
        self.driver.find_element(By.XPATH,'//*[@id="_COLCOD"]').click()

        self.driver.find_element(By.XPATH,'//*[@id="_COLCOD"]').send_keys(rbd) 
        # self.driver.find_element(By.XPATH,'//*[@id="TABLE2"]/tbody/tr[5]/td/span/input').click()
        
        self.driver.find_element(By.XPATH,'//*[@id="TABLE1"]/tbody/tr/td[2]/input').click()
        self.driver.find_element(By.XPATH,'//*[@id="span__OPCIONES_0001"]/a/img').click()
        
        self.driver.find_element(By.XPATH,'//*[@id="CTLFMFECIND"]').click()
        sleep(1)
        self.driver.find_element(By.XPATH,'//*[@id="CTLFMFECIND"]').send_keys('03102022')
        self.driver.find_element(By.XPATH,'//*[@id="TABLE25"]/tbody/tr/td[4]/p/span/input').click()
        self.driver.find_element(By.XPATH,'//*[@id="TABLE24"]/tbody/tr[1]/td[5]/span/input').click()
        self.driver.find_element(By.XPATH,'//*[@id="TABLE24"]/tbody/tr[2]/td[3]/p/span/input').click()
        self.driver.find_element(By.XPATH,'//*[@id="TABLE24"]/tbody/tr[4]/td[3]/p/span/input').click()
        self.driver.find_element(By.XPATH,'//*[@id="_CPTOSUBVLR_00010003"]').click()
        self.driver.find_element(By.XPATH,'//*[@id="_CPTOSUBVLR_00010003"]').send_keys(peso)
        self.driver.find_element(By.XPATH,'//*[@id="_CPTOSUBVLR_00020003"]').click() 
        self.driver.find_element(By.XPATH,'//*[@id="_CPTOSUBVLR_00020003"]').send_keys(talla)    

        # NORMAL #
        if diagnostico == 'sano':
            self.driver.find_element(By.XPATH,'//*[@id="TABLE10_00020002"]/tbody/tr/td[5]/span/input').click()
            self.driver.find_element(By.XPATH,'//*[@id="TABLE10_00020004"]/tbody/tr/td[5]/span/input').click()
            self.driver.find_element(By.XPATH,'//*[@id="TABLE10_00020005"]/tbody/tr/td[5]/span/input').click()
            self.driver.find_element(By.XPATH,'//*[@id="pagecontent"]/ul/li[2]/a').click()
            self.driver.find_element(By.XPATH,'//*[@id="TABLE12_00010001"]/tbody/tr/td[5]/span/input').click()
            self.driver.find_element(By.XPATH,'//*[@id="TABLE12_00020002"]/tbody/tr/td[5]/span/input').click()
            self.driver.find_element(By.XPATH,'//*[@id="TABLE7"]/tbody/tr/td[1]/input').click()
            sleep(1)
            self.driver.switch_to.alert.accept()
            sleep(3)
            self.driver.find_element(By.XPATH,'//*[@id="TABLE7"]/tbody/tr/td[2]/input').click()
        
        elif diagnostico == 'Escoliosis':
            self.driver.find_element(By.XPATH,'//*[@id="TABLE10_00010002"]/tbody/tr/td[5]/span/input').click()
            self.driver.find_element(By.XPATH,'//*[@id="TABLE10_00010004"]/tbody/tr/td[5]/span/input').click()
            self.driver.find_element(By.XPATH,'//*[@id="TABLE10_00020005"]/tbody/tr/td[5]/span/input').click()
            self.driver.find_element(By.XPATH,'//*[@id="pagecontent"]/ul/li[2]/a').click()
            self.driver.find_element(By.XPATH,'//*[@id="TABLE12_00020001"]/tbody/tr/td[5]/span/input').click()
            self.driver.find_element(By.XPATH,'//*[@id="TABLE12_00010002"]/tbody/tr/td[5]/span/input').click()
            self.driver.find_element(By.XPATH,'//*[@id="TABLE7"]/tbody/tr/td[1]/input').click()
            sleep(1)
            self.driver.switch_to.alert.accept()
            sleep(3)
            self.driver.find_element(By.XPATH,'//*[@id="TABLE7"]/tbody/tr/td[2]/input').click()

        elif diagnostico == 'Dorsocurvo':
            self.driver.find_element(By.XPATH,'//*[@id="TABLE10_00010002"]/tbody/tr/td[5]/span/input').click()
            self.driver.find_element(By.XPATH,'//*[@id="TABLE10_00020004"]/tbody/tr/td[5]/span/input').click()
            self.driver.find_element(By.XPATH,'//*[@id="TABLE10_00010005"]/tbody/tr/td[5]/span/input').click()
            self.driver.find_element(By.XPATH,'//*[@id="pagecontent"]/ul/li[2]/a').click()
            self.driver.find_element(By.XPATH,'//*[@id="TABLE12_00020001"]/tbody/tr/td[5]/span/input').click()
            self.driver.find_element(By.XPATH,'//*[@id="TABLE12_00010002"]/tbody/tr/td[5]/span/input').click()
            self.driver.find_element(By.XPATH,'//*[@id="TABLE7"]/tbody/tr/td[1]/input').click()
            sleep(1)
            self.driver.switch_to.alert.accept()
            sleep(3)
            self.driver.find_element(By.XPATH,'//*[@id="TABLE7"]/tbody/tr/td[2]/input').click()
                
        
        
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

    def digitar_impedancio(self,rut,rbd, fecha):
        """_summary_
        Metodo para ingresar las atenciones de impedanciometria
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
              
        
        
        


        



       

        



        
        
        


        

        

        
        
        
        
        

        
        
        

        
        
        

        

        
       
        
        
        
        
       


