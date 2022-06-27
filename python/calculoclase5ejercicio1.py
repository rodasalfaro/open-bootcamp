import os

#Funcion calculo area de triangulo
def atriangulo(base, altura):
    areat=base*altura
    return areat

#Funcion calculo area de circulo
def acirculo(radio):
    areac=(radio**2)*3.1416
    return areac

os.system('clear')

opc=9
respuesta=0
#Impresion de menu

while opc!=0:
    os.system('clear')
    print("***************************************************")    
    print("1- Calcular area de un triangulo")
    print("2- Calcular area de un circulo")
    print("3- Salir")
    print("***************************************************")
    opc=input("Ingrese numero de opcion:")

        
    match int(opc):
        case 1:
            base_val=input("Ingrese base del triangulo:")
            altura_val=input("Ingrese altura del triangulo:") 
            #conversion numerica de valor obtenido de input
            bv=float(base_val) 
            av=float(altura_val) 
            resultado=atriangulo(bv,av)
            respuesta="El area del triangulo es : "
        case 2:
            radio_val=input("Ingrese radio del circulo:")
            ac=float(radio_val)
            resultado=acirculo(ac)
            respuesta="El area del circulo es : "        
        case 3:
            opc=0
        
    if int(opc)!=0:
        print("***************************************************")    
        print(respuesta +" ", resultado)
        print("***************************************************")
        input("presione Enter para continuar...")







    
    