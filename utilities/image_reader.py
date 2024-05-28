import requests


root = 'http://apolo.junaeb.cl:8080/xwsalud/images/Captcha/20.jpg'


def get_img(root:str)-> None:
    """
    Funcion que hace un request a una direccion que contiene una imagen,
    descarga la imagen y la guarda con el nombre img.jpg
    """
    with open('img.jpg', 'wb') as file:
        image = requests.get(root)
        file.write(image.content)


if __name__ == '__main__':
    get_img(root)

