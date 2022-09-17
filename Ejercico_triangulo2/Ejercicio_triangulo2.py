# determinar si un triangulo es obtuso recto o agudo

print("-------------------")
print("----triangulo -----")
print("-------------------")

#input

a = int(input("digite el angulo de a "))
b = int(input("digite el angulo de b "))
c = int(input("digite el angulo de c "))

#processing

if (a+b+c == 180):
    if (a>90 ):
        print("es un triangulo obtuso")
    if( b>90):
        print("es un triangulo obtuso")
    if (c>90):
        print("es un triangulo obtuso")
    if (a<90 and b<90 and c<90):
        print("es un triangulo agudo")
    if(a==90):
        print("es un triangulo recto")
    if(b==90):
        print("es un triangulo recto")
    if(c==90):
        print("es un triangulo recto")
else:
    print("la suma de los angulos es menor a 180")

#OUTPUT

#fin