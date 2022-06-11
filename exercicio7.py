def calculateSalary(totalHours, hourValue):
    return totalHours*hourValue


def main():
    hourValue = float(input("Informe o valor hora (R$):"))
    hoursAmount = float(input("Informe a quantidade de horas normais:"))
    extraHoursAmount = float(input("Informe a quantidade de horas extras:"))

    totalHours = hoursAmount + (extraHoursAmount*2)
    salary = calculateSalary(totalHours,hourValue)

    print("O valor a receber é R$",salary)
main()