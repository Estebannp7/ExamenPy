#variable  de control
contador = 0


contadorMultiplo = 0

while(contador<5):
    numero=int(input("Digite un numero: "))
    modulo = numero % 2 
    modulo2 = numero % 3

    if(modulo ==0):
        contadorMultiplo= contadorMultiplo+1
    elif(modulo2 == 0):
       contadorMultiplo= contadorMultiplo+1 

    else:
        contadorMultiplo = contadorMultiplo


    contador = contador+1    
print(f'el numero de multiplos fue  {contadorMultiplo}')  