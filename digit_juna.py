
# def sum_all(lista: list):
#     """_summary_
#     a funcion that order a list of 2 elements and returns 
#     the sum betwen them.
#     Args:
#         lista (_type_): 
#         List of 2 elements

#     Returns:
#         _type_: 
#         integer
#     """    
#     lista.sort()
#     a,b = lista
#     suma = 0
#     for i in range(a,b+1):
#         suma += i

#     return suma

# if __name__ == '__main__':
#     print(sum_all([1,4]))
#     print(sum_all([3,2]))


# """3) Write an algorithm to reverse a string. For example, if my string is 
# "uhsnamiH" then my result will be "Himanshu"."""

# string = 'Hola'
# reverse = ''
# for i in range(1,len(string)+1):
#     reverse = reverse + string[i*-1]
#     print(i*-1)

# print(reverse) 

# print(string[::-1])


class Perro:
    nombre = ''
    
    def __init__(self, raza) -> None:
        self.raza = raza

    @staticmethod
    def ladrar():
        print('GUAFF!!!')
    
    def set_nombre2(self, nombre):
        self.nombre = nombre

    @classmethod
    def set_nombre(cls, nombre):
        cls.nombre = nombre
    

lista = [Perro('kiltro'), Perro('kilterrier')]


firulais = Perro('kiltro')
roco = Perro('kilterrier')

print(firulais.nombre, roco.nombre)

firulais.set_nombre('alberto')

print(firulais.nombre, roco.nombre)

roco.set_nombre2('pepe')

print(firulais.nombre, roco.nombre)
