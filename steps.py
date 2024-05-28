LOGIN_XPATH = {
    'user':'ssmh', #nombre de usuario
    'pswd':'Ssmh.2024', #contraseña usuario
    'user_xpath':'//*[@id="_USUARIO"]', 
    'pswd_xpath':'//*[@id="_CLAVE"]',
    'login_xpath':'//*[@id="TABLE2"]/tbody/tr[5]/td/input'
}

DIGITAR_ATENCION_COLUMNA = [
    ('//*[@id="_BENSALRUT"]', 'send keys'),
    ('//*[@id="_COLCOD"]', 'send keys'), 
    ('//*[@id="TABLE2"]/tbody/tr[5]/td/span/input', 'click checkbox'),
    ('//*[@id="TABLE1"]/tbody/tr/td[2]/input', 'click')
]

VALIDAR_RUT_DBD = [
    ('//*[@id="_CTEESTURUT"]', 'send keys'),
    ('//*[@id="TABLE5"]/tbody/tr/td[1]/input', 'click'),
    ('//*[@id="span_CTLCOLCOD"]', 'get text'),
    ('//*[@id="span__OPCIONES_0001"]/a/img', 'try element')
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