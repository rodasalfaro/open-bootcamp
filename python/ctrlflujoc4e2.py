numero_inicial=0
numero_final=0
num=0
imprime_impar=0
lista_impares=[]

#Pidiendo datos iniciales
numero_inicial=input("Digite el numero inicial del intervalo:")
numero_final=input("Digite el numero final del intervalo:")

#convirtiendo strings obtenidos por input a integer
ni=int(numero_inicial)
nf=int(numero_final)

#Validando congruencia de numero inicial y numero final
if ni<nf:
    num=ni
    #Evaluando intervalo de iteracion desde numero inicial hasta numero final
    while num<nf:
        #Encontrando los numeros impares del intervalo
        if (num % 2) != 0:
            #Asignando a variable simple para impresion iterativa
            imprime_impar=num
            #Asignando a lista para imprsion en formato de array
            lista_impares.append(num)
            #Imprimiendo la iteracion
            print(imprime_impar)
        #recorriendo el intervalo    
        num+=1
else:
    print("El numero inicial no puede ser menor que el numero final")    

#Imprimiendo lista de intervalo de impares obtenidos
print("Lista de impares\n", lista_impares)
