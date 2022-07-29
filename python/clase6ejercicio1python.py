import os

os.system('clear')



class Vehiculo():
    #inicializamos los atributos
    def __init__(self, color, noruedas, nopuertas):

        self.color= color
        self.noruedas= noruedas
        self.nopuertas= nopuertas
    
    def __str__(self):
        return "Color del auto: {}, No. de ruedas: {}, No. de puertas {}".format(self.color, self.noruedas, self.nopuertas)
    

class Coche(Vehiculo):
    
    def __init__(self, color, noruedas, nopuertas, velocidad, cilindrada):
        self.color = color
        self.noruedas = noruedas
        self.nopuertas = nopuertas
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    
    def __str__(self):
        return "Color del auto :{}\nNo. de ruedas :{}\nNo. de puertas :{}\nVelocidad :{}km/h\nCilindrada :{}cc".format(self.color, self.noruedas, self.nopuertas, self.velocidad, self.cilindrada)
    


primerauto = Coche("azul", 4, 4, 160, 2000)

print(primerauto)


    
    