if __name__ == '__main__':
    nom=input("Proporciona el nombre")
    fecnom=" "
    match nom:
        case "Ashley":fecnom="19/01/2002"
        case "Hilario":fecnom="25/09/1976"
        case "Lourdes":fecnom="09/02/1980"
        case "Rosaura":fecnom="02/10/1935"
        case "Leobardo":fecnom="05/01/1980"
        case _:fecnom="invalido"
    print(f"La fecha de nacimiento de {nom} es {fecnom}")