if __name__ == '__main__':
    dia=int(input("Proporciona un numero de la semana"))
    numdia=""
    match dia:
        case 1:numdia="Lunes"
        case 2:numdia="Martes"
        case 3:numdia="Miercoles"
        case 7:numdia="Domingo"
        case _:numdia="Dia no valido"
    print(f"El dia de la semana es {numdia}")