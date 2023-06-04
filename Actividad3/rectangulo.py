class Rectangulo:
    """
    Clase que representa un rectángulo.

    Atributos:
        base (float): La base del rectángulo.
        altura (float): La altura del rectángulo.

    Métodos:
        calcular_area(): Calcula y devuelve el área del rectángulo.
        calcular_perimetro(): Calcula y devuelve el perímetro del rectángulo.
    """

    def __init__(self, base, altura):
        """
        Inicializa una nueva instancia de la clase Rectangulo.

        :param base: La base del rectángulo.
        :type base: float
        :param altura: La altura del rectángulo.
        :type altura: float
        """
        self.base = base
        self.altura = altura

    def calcular_area(self):
        """
        Calcula y devuelve el área del rectángulo.

        :return: El área del rectángulo.
        :rtype: float
        """
        return self.base * self.altura

    def calcular_perimetro(self):
        """
        Calcula y devuelve el perímetro del rectángulo.

        :return: El perímetro del rectángulo.
        :rtype: float
        """
        return 2 * (self.base + self.altura)