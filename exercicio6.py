from os import system
import os


def checkDivision2(number):
    if(number%2==0):
        return True
    else:
        return False

def checkDivision3(number):
    if(number%3==0):
        return True
    else:
        return False

def receiveNumbers():
    print("Digite valores inteiros ou 0 para finalizar.\n")
    numbers = []
    n = -1
    while(n!=0):
        n = int(input("Informe um número inteiro:"))
        if(n!=0):
            numbers.append(n)

    return numbers

def checkNumbers(numbers):
    for n in numbers:
        if(checkDivision2(n)):
            print(n, "é divisivel por 2.")
        if(checkDivision3(n)):
            print(n, "é divisivel por 3.")


def main():
    numbers = receiveNumbers()
    os.system('cls')
    checkNumbers(numbers)


main()