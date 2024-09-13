class Calculadora:
    _instance = None

    def __new__(cls, num1=0):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.set_num1(num1)
        return cls._instance

    def __init__(self, num1=0):
        if not hasattr(self, '_initialized'):
            self.num1 = num1
            self.resultado = num1
            self._initialized = True

    def set_num1(self, num1):
        self.num1 = num1
        self.resultado = num1

    def get_resultado(self):
        return self.resultado

    def limpiar(self):
        self.resultado = 0
        self.num1 = 0

    def suma(self, num2):
        self.resultado += num2
        self.num1 = self.resultado
        return self.resultado

    def resta(self, num2):
        self.resultado -= num2
        self.num1 = self.resultado
        return self.resultado

    def multiplicacion(self, num2):
        self.resultado *= num2
        self.num1 = self.resultado
        return self.resultado

    def division(self, num2):
        if num2 == 0:
            return "Error: División por cero"
        self.resultado /= num2
        self.num1 = self.resultado
        return self.resultado
