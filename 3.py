opcion = 100

print("***producto  ***")
print("1. Agregar productos")
print("2.Mostar")
print("0. Salir")

productos=[]

while(opcion !=0):

    #DICCIONARIO
    producto={}
    #Pedimos la opcion deseada
    opcion= int(input("Digite la opcion deseada: "))
    #Caminos del menu
    if(opcion==1):
        producto['codigo'] = input("digite su codigo: ")
        producto['nombre']= input("Digite su nombre: ")
        producto['precio']= input("Digite  su precio: ")
        productos.append(producto)
        
    elif(opcion==0):
        break
    elif(opcion==2):    
        print(productos)
    elif(opcion==3):
        codigoAbuscar = input("digite el codigo: ")
        for producto in productos:
            if(producto["codigo"]==codigoAbuscar):
                print(f"cliente encontrado:{producto['codigo']}")
                cambiar = int(input("digite precio:"))
                producto['precio'] = cambiar

    
               
                
                
            else:
                print ("Usuario no encontrado")           
      
    else:
        print("Digite una opcion valida")   