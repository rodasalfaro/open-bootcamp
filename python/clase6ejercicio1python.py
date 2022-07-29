import os

os.system('clear')



class Vehiculo:
    color= "blanco"
    noruedas= 4
    nopuertas= 5
    
    
    

class Coche(Vehiculo):
    velocidad = 60
    cilindrada = "2000cc"


primerauto = Coche()



print('Color del auto:',primerauto.color,
      '\nNo. puertas:', primerauto.nopuertas,
      '\nNo. de ruedas:', primerauto.noruedas,
      '\nCilindrada:', primerauto.cilindrada,
      '\nVelocidad :', primerauto.velocidad, 'km/h')

    
    