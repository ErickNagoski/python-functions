def checkInterval(min, max):
    value = int(input("Informe o valor para verificar: "))
    if(value>=min and value<=max):
        return True
    
    return False


def main():
    min  = int(input("Informe o minimo: "))
    max = int(input("Informe o máximo: "))

    if(not checkInterval(min, max)):
        print("Erro, o valor não está no intervalo!")
    else:
        print("O valor está no intervalo.")
main()