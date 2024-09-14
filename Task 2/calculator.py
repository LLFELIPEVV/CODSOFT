# Se define la clase Calculadora, que contiene métodos para manejar cálculos básicos.
class Calculadora:
    # El constructor inicializa la calculadora y establece sus valores iniciales.
    def __init__(self):
        # Llama al método reset para establecer los valores iniciales.
        self.reset()

    # El método reset reinicia los valores de la calculadora.
    def reset(self):
        self.num1 = None  # Primer número (inicialmente no establecido).
        self.num2 = None  # Segundo número (inicialmente no establecido).
        self.resultado = 0  # Resultado de la operación (inicialmente 0).
        # Operación actual (inicialmente no establecida).
        self.operacion = None
        # Última operación realizada (inicialmente no establecida).
        self.ultima_operacion = None
        # Indica si se está realizando una operación (inicialmente False).
        self.es_operacion = False

    # El método set_num establece el número actual en la calculadora.
    def set_num(self, num):
        # Si num1 no está establecido, se asigna a num1.
        if self.num1 is None:
            self.num1 = num
        else:
            # Si num1 ya está establecido, se asigna a num2.
            self.num2 = num

    # El método set_operacion establece la operación que se realizará.
    def set_operacion(self, operacion):
        # Si num1 está establecido, se configura la operación.
        if self.num1 is not None:
            # Si ya hay una operación previa, se calcula el resultado de esa operación.
            if self.operacion:
                self.calcular()
            # Se asigna la nueva operación.
            self.operacion = operacion
            self.es_operacion = True

    # El método calcular realiza el cálculo según la operación actual.
    def calcular(self):
        # Si hay una operación y num2 está establecido, se realiza el cálculo.
        if self.operacion and self.num2 is not None:
            # Se realiza la operación correspondiente.
            if self.operacion == '+':
                self.resultado = self.num1 + self.num2
            elif self.operacion == '-':
                self.resultado = self.num1 - self.num2
            elif self.operacion == '*':
                self.resultado = self.num1 * self.num2
            elif self.operacion == '/':
                # Si se intenta dividir por cero, se muestra un mensaje de error.
                if self.num2 == 0:
                    self.resultado = "Error: División por cero"
                else:
                    self.resultado = self.num1 / self.num2

            # Se actualiza num1 con el resultado y se prepara num2 para la próxima operación.
            self.num1 = self.resultado
            self.num2 = None
            self.operacion = None
            return self.resultado  # Se devuelve el resultado del cálculo.
        # Si no se realiza ningún cálculo, se devuelve el resultado actual.
        return self.resultado

    # El método get_resultado devuelve el resultado actual de la operación.
    def get_resultado(self):
        return self.resultado

    # El método limpiar reinicia la calculadora a su estado inicial.
    def limpiar(self):
        # Llama al método reset para restablecer todos los valores.
        self.reset()
