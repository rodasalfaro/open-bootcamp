import os

#Funcion clasificando numero primo o no
def esprimo(num):
    esprimosn=False
    if num>2:
        contador=2 # se inicia desde 2 ya que el 1 es parte del criterio para se numero primo
        while contador<num:         
            resultado=num % contador
            if resultado==0:
                esprimosn=False
                break
            else:
                esprimosn=True
            contador+=1       
    else:
        if num!=0:
            esprimosn=True
        else:
            esprimosn=False
    return esprimosn

os.system('clear')

opc="S"


while opc.upper()!="N":
    #Obteniendo numero a evaluar
    pnum_val=input("Ingrese el numero a evaluar:")

    pval=int(pnum_val)
    #llamando funcion de evaluacion
    esunprimo=esprimo(pval)
    
    #Imprimiendo resultado
    if esunprimo==True:
        print("El numero SI es primo")
    else:
        print("El numero NO es primo")
    
    opc=input("Evaluar otro numero:[S o N]?:")
    