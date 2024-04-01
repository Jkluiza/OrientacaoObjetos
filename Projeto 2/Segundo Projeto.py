import math

class FormaGeometrica:
    def __init__(self, tipoForma, dimensao1, dimensao2):
        self.tipoForma = tipoForma
        self.dimensao1 = dimensao1
        self.dimensao2 = dimensao2

    def calcularArea(self):
        if self.tipoForma == "Retângulo":
            return self.dimensao1 * self.dimensao2
        elif self.tipoForma == "Círculo":
            return 3.14 * (self.dimensao1/2) ** 2
        elif self.tipoForma == "Triângulo":
            return (self.dimensao1 * self.dimensao2) / 2
        else:
            return "Forma não reconhecida"

    def calcularPerimetro(self):
        if self.tipoForma == "Retângulo":
            return 2 * (self.dimensao1 + self.dimensao2)
        elif self.tipoForma == "Círculo":
            return 2 * 3.14 * (self.dimensao1/2)
        elif self.tipoForma == "Triângulo":
            return self.dimensao1 + self.dimensao2 + math.sqrt(self.dimensao1**2 + self.dimensao2**2)
        else:
            return "Forma não reconhecida"

# Para usar a classe
forma1 = FormaGeometrica("Retângulo", 5, 10)
forma2 = FormaGeometrica("Círculo", 10, 0)
forma3 = FormaGeometrica("Triângulo", 5, 10)

print(forma1.calcularArea())
print(forma2.calcularPerimetro())
print(forma3.calcularArea())