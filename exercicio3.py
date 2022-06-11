def checkDivision(a,b):
    if(a%b==0):
        return 1
    
    return 0

def main():
    a = int(input("Informe A:"))
    b = int(input("Informe B:"))

    print(checkDivision(a,b))

main()