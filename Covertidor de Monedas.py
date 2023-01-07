#Input del usuario
colones = input("¿Cuantos colones tienes ?")
colones = float(colones)
#Declaracion de valores
valor_dolar = 594
valor_euro = 4383
valor_cake = 58800
valor_btc = 136134100
#Calculo valor dolar
dolares= colones / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
#Calculo Valor Euro
euros= colones / valor_euro
euros = round(euros, 2)
euros = str(euros)
#Calculo Cantidad de CAKE
cakes = colones / valor_cake
cakes = round(cakes, 4)
cakes = str(cakes)
#Calculo Bitcoin
btcs = colones / valor_btc
btcs = round(btcs, 9)
btcs = str(btcs)
#Prints
print("Tienes $"+ dolares + " dolares")
print("Tienes $"+ euros + " Euros")
print("Tienes: " + cakes + " CAKE")
print("Tienes: " + btcs + " Bitcoins")