def checkInterval(min, max):
    value = int(input("Informe o valor para verificar se está no intervalo: "))
    if(value>=min and value<=max):
        return True
    
    return False


def main():
    min  = int(input("Informe o minimo do intervalo: "))
    max = int(input("Informe o máximo do intervalo: "))

    if(not checkInterval(min, max)):
        print("Erro, o valor não está no intervalo!")
    else:
        print("O valor está no intervalo.")
main()