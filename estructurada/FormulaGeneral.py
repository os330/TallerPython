class FormulaGeneral:
    def __init__(self, v1,v2,v3):
        self.a=v1
        self.b=v2
        self.c=v3

    def potencia (self)->float:
        return self.b * self.b

    def multi (self)->float:
        return 4*self.a*self.c

    def resta (self)->float:
        return potencia()-multi()

    def raiz (self)->float:
        return sqrt(resta)

    def multi2 (self)->float:
        return 2*self.a

    def fg1 (self)->float:
        return (-self.b+raiz()/multi2())

    def fg2(self) -> float:
        return (-self.b-raiz() / multi2())

if __name__ == '__main__':
    resultado = Operaciones(8.0,9.0,10.0)
    print(resultado.fg1())
    print(resultado.fg2())