import math

if __name__ == '__main__':
    Suma=lambda x,y:x+y
    print(f"La suma es {Suma(2,6)}")

    Potencia=lambda x:x**2
    resultado=Potencia(9)
    print(f"La potencia es {resultado}")

    x1=lambda a,b,c:(-b+math.sqrt(b**2 *4*a*c)/2*a)
    print(f"La formula general es {x1(3,5,9)}")

