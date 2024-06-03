LOGIN_XPATH = {
    'user':'ssmh', #nombre de usuario
    'pswd':'Ssmh.2024', #contraseña usuario
    'user_xpath':'//*[@id="_USUARIO"]', 
    'pswd_xpath':'//*[@id="_CLAVE"]',
    'login_xpath':'//*[@id="TABLE2"]/tbody/tr[5]/td/input'
}

DIGITAR_ATENCION_COLUMNA = [
    ('//*[@id="_BENSALRUT"]', 'send keys'), #ingreso de rut
    ('//*[@id="_COLCOD"]', 'send keys'),  #ingreso de rbd
    ('//*[@id="TABLE2"]/tbody/tr[5]/td/span/input', 'click checkbox'), #chequeo de urgencia
    ('//*[@id="TABLE1"]/tbody/tr/td[2]/input', 'click'), #renovar
    ('//*[@id="span__OPCIONES_0001"]/a/img', 'try element'), #chequear si el estudiante existe
    ('//*[@id="CTLFMFECIND"]', 'send keys'), #ingreso de fecha
    ('//*[@id="TABLE25"]/tbody/tr/td[4]/p/span/input', 'click'), #derivacion junaeb
    ('//*[@id="TABLE24"]/tbody/tr[1]/td[5]/span/input', 'click'), #pesquisa
    ('//*[@id="TABLE24"]/tbody/tr[2]/td[3]/p/span/input', 'click'), #escuela
    ('//*[@id="TABLE24"]/tbody/tr[4]/td[3]/p/span/input', 'click'), # componente educativo
    ('//*[@id="_CPTOSUBVLR_00010003"]', 'send keys'), #peso
    ('//*[@id="_CPTOSUBVLR_00020003"]', 'send keys'), # talla
    ('//*[@id="_CPTOSUBVLR_00030003"]', 'send keys'), #menarquia
    ('diagnosis', 'call_self_method'), #insertar diagnostico
    ('alert', 'click alert'), #click alert
    #('//*[@id="TABLE5"]/tbody/tr[3]/td/span/menu/li', 'get text')#sacar info de la digitacion
    ('//*[@id="TABLE7"]/tbody/tr/td[2]/input', 'click')
]



ATENCION_COLUMNA_NORMAL = [
    '//*[@id="TABLE10_00020002"]/tbody/tr/td[5]/span/input',
    '//*[@id="TABLE10_00020004"]/tbody/tr/td[5]/span/input',
    '//*[@id="TABLE10_00020005"]/tbody/tr/td[5]/span/input',
    '//*[@id="pagecontent"]/ul/li[2]/a',
    '//*[@id="TABLE12_00010001"]/tbody/tr/td[5]/span/input',
    '//*[@id="TABLE12_00020002"]/tbody/tr/td[5]/span/input',
    '//*[@id="TABLE7"]/tbody/tr/td[1]/input'
]

ATENCION_COLUMNA_ESCOLIOSIS = [
    '//*[@id="TABLE10_00010002"]/tbody/tr/td[5]/span/input',
    '//*[@id="TABLE10_00010004"]/tbody/tr/td[5]/span/input',
    '//*[@id="TABLE10_00020005"]/tbody/tr/td[5]/span/input',
    '//*[@id="pagecontent"]/ul/li[2]/a',
    '//*[@id="TABLE12_00020001"]/tbody/tr/td[5]/span/input',
    '//*[@id="TABLE12_00010002"]/tbody/tr/td[5]/span/input',
    '//*[@id="TABLE7"]/tbody/tr/td[1]/input'
]

ATENCION_COLUMNA_DORSOCURVO = [
    '//*[@id="TABLE10_00010002"]/tbody/tr/td[5]/span/input',
    '//*[@id="TABLE10_00020004"]/tbody/tr/td[5]/span/input',
    '//*[@id="TABLE10_00010005"]/tbody/tr/td[5]/span/input',
    '//*[@id="pagecontent"]/ul/li[2]/a',
    '//*[@id="TABLE12_00020001"]/tbody/tr/td[5]/span/input',
    '//*[@id="TABLE12_00010002"]/tbody/tr/td[5]/span/input',
    '//*[@id="TABLE7"]/tbody/tr/td[1]/input'
]

VALIDAR_RUT_DBD = [
    ('//*[@id="_CTEESTURUT"]', 'send keys'),
    ('//*[@id="TABLE5"]/tbody/tr/td[1]/input', 'click'),
    ('//*[@id="span_CTLCOLCOD"]', 'get text'),
]


'//*[@id="TABLE2"]/tbody/tr[3]/td/p/input[2]'

{   
    '8':'taste',
    '9':'knot',
    '10':'safe',
    '18':'polish',
    '23':'crime',
    '24':'canvas',
    '25':'narrow',
    '26':'door',
    '27':'news',
    '31':'seem',
    '39':'green'
}