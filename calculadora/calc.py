class Calculadora():
    def __init__(self, num1, num2, operador=None):
        self.num1 = num1
        self.num2 = num2
        self.operador = operador
    
    def calcular(self):
        if self.operador=="soma":
            soma = self.num1 + self.num2
            return soma
        
        elif self.operador=="subtracao":
            subtracao = self.num1 - self.num2
            return subtracao
        
        elif self.operador=="divisao":
            divisao = self.num1/self.num2
            return divisao

        else:
            multiplicacao = self.num1 * self.num2
            return multiplicacao
