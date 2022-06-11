from random import randint


def ramdomNumbers(n):
    numbers = []
    for i in range(0,n):
        ramdom = randint(1,50)
        print("valor",i+1,"gerado = ",ramdom)
        numbers.append(ramdom)
    
    return numbers

def calculateNumbers(numbers):
    sum = 0

    for n in numbers:
        sum +=n

    return sum

def main():
    n = int(input("Informe um número inteiro:"))

    ramdomNumbersList = ramdomNumbers(n)

    print("\nSoma dos valores", calculateNumbers(ramdomNumbersList))
main()