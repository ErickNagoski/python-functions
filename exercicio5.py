def receiveRealNumbers(n):
    realNumbers = []

    for i in range(0,n):
        number = float(input("Informe um número real:"))
        realNumbers.append(number)
    
    return realNumbers

def sortNumbersArray(numbers):
    return sorted(numbers)

def main():
    listSize = int(input("Informe um número inteiro: "))
    realNumbers = sortNumbersArray(receiveRealNumbers(listSize))
   
    print("Maior número:",realNumbers[listSize-1])
    print("Menor número:",realNumbers[0])
    

main()