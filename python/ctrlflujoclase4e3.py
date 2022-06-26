import os

num=0
num_final=100
num100_inverso1=[]
num100_inverso2=[]

os.system('clear')
#del 100 al 1 usando range
print("************************************************")
for num in range(100,0,-1):
    print(num)
    num100_inverso1.append(num)
#del 100 al 1 usando while
print("************************************************")
while num_final>=1:
    print(num_final)
    num100_inverso2.append(num_final)
    num_final-=1
    
#imprimiendo listas obtenidas
print("Para lista obtenida con for y range\n",num100_inverso1)
print("Para lista obtenida con while\n",num100_inverso2)