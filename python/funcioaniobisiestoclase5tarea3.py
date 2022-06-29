import os

#Funcion calculando anio bisiesto
#Para que un anio sea bisiesto deben cumplirse los siguientes criterios
# Es multiplo de 4?     Es multiplo de 100    es multiplo de 400     True/False  True=Bisiesto False=No bisiesto
#       NO                      NO                  NO                  False
#       SI                      NO                  SI                  True
#       SI                      SI                  NO                  False
#       SI                      SI                  SI                  True

def esbisiesto(anio):
    m4=1
    m100=1
    m400=1
    esbisiestosn=False
    
    #Calculamos si son multiplos o no
    m4=anio%4
    m100=anio%100
    m400=anio%400
    
    #Luego evaluamos los criterios correspondientes   
    if m4==0 and m100==0 and m400==0:
        esbisiestosn=True
    elif m4==0 and m100!=0 and m400!=0:
        esbisiestosn=True
        
    '''Necesario si no se declara esbisiestosn como False
    
    else:
        esbisiestosn=False
    
    '''
    
    return esbisiestosn

os.system('clear')

opc="S"


while opc.upper()!="N":
    #Obteniendo anio a evaluar
    anum_val=input("Ingrese el anio a evaluar:")

    aval=int(anum_val)
    #llamando funcion de evaluacion
    esunbisiesto=esbisiesto(aval)
    
    #Imprimiendo resultado
    if esunbisiesto==True:
        print("El anio SI es bisiesto")
    else:
        print("El anio NO es bisiesto")
    
    opc=input("Evaluar otro anio:[S o N]?:")