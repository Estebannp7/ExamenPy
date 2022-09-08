LIMITADOR = 2
fruta={}
frutas=[]
cont = 0

while(cont <LIMITADOR):
    fruta ["nombre"]=(input("Digite nombre"))
    fruta [ "color"] = (input("digite color"))
    fruta ["precio"]= int(input("digite precio"))
    frutas.append(fruta)
    cont += 1

frutas.reverse()
print(frutas)