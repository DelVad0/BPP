class MaquinaCafe:
    def __init__(self):
        self.cantidad_cafe = 100
        self.cantidad_agua = 1000

    def hacer_cafe(self):
        if self.cantidad_cafe >= 10 and self.cantidad_agua >= 100:
            self.cantidad_cafe -= 10
            self.cantidad_agua -= 100
            return "Café servido"
        else:
            return "No hay suficiente café o agua"

    def rellenar_cafe(self):
        self.cantidad_cafe = 100

    def rellenar_agua(self):
        self.cantidad_agua = 1000
        