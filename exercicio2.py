import math


def diametro(raio):
    return 2 * raio

def circunferencia(raio):
    return 2*math.pi*raio

def area(raio):
    return math.pi * (raio*raio)

def volume(raio):
    return math.pi * (raio*raio*raio)

def main():
    raio = float (input("Informe o raio da esfera:"))
    print('\nDiâmetro:',diametro(raio))
    print('Circunferência', circunferencia(raio))
    print('Área', area(raio))
    print('Volume', volume(raio))
main()