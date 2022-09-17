# dado 3 numeros a,b,c verificar si pueden formar los lados de un triangulo

print("------TRIANGULO------")
print("---------------------")

#input
a = int(input("digite el valor de a"))
b = int(input("digite el valor de b"))
c = int(input("digite el valor de c"))

#processing

if (a+b<c):
   print("si es un triangulo")
else:
   print("no es un triangulo")
if (b+c<a):
   print("si es un triangulo")
else:
   print("no es un triangulo")
if (c+a<b):
   print("si es un triangulo")
else:
   print("no es un triangulo")
