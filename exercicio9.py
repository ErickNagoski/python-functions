def convertCode(stringList):
    convertedCode = [
        int(stringList[0])*2,
        int(stringList[1])*3,
        int(stringList[2])*4,
        int(stringList[3])*5,
        int(stringList[4])*6,
    ]
    return convertedCode

def generateCheckDigit(code):
    digits = convertCode(list(code))
    sum  = 0
    for i in digits:
        sum +=i

    return sum%7

def main():
    productCode = input("Informe um valor inteiro entre 10000 e 30000: ")
    checkDigit = generateCheckDigit(productCode)
    print("Digito verificador: ",checkDigit)
main()