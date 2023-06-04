class MaquinaCafe:
    """
    ☕

    Atributos:
        cantidad_cafe (int): La cantidad actual de café en gramos.
        cantidad_agua (int): La cantidad actual de agua en mililitros.

    Métodos:
        hacer_cafe(): Prepara y sirve una taza de café.
        rellenar_cafe(): Rellena la máquina de café con la cantidad predeterminada de café.
        rellenar_agua(): Rellena la máquina de café con la cantidad predeterminada de agua.
    """

    def __init__(self, cantidad_cafe=100, cantidad_agua=1000):
        """
        Inicializa una nueva instancia de la clase MaquinaCafe.

        :param cantidad_cafe: La cantidad de café inicial (predeterminada: 100 gramos).
        :type cantidad_cafe: int
        :param cantidad_agua: La cantidad de agua inicial (predeterminada: 1000 mililitros).
        :type cantidad_agua: int
        """
        self.cantidad_cafe = cantidad_cafe
        self.cantidad_agua = cantidad_agua

    def hacer_cafe(self):
        """
        Prepara y sirve una taza de café.

        Returns:
            str: El mensaje indicando si el café fue servido o si no hay suficiente café o agua.
        """
        if self.cantidad_cafe >= 10 and self.cantidad_agua >= 100:
            self.cantidad_cafe -= 10
            self.cantidad_agua -= 100
            return "Café servido"
        else:
            return "No hay suficiente café o agua"

    def rellenar_cafe(self):
        """
        Rellena la máquina de café con la cantidad predeterminada de café.

        El café se rellena hasta llegar a 100 gramos.
        """
        self.cantidad_cafe = 100

    def rellenar_agua(self):
        """
        Rellena la máquina de café con la cantidad predeterminada de agua.

        El agua se rellena hasta llegar a 1000 mililitros.
        """
        self.cantidad_agua = 1000
        