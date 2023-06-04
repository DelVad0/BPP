##Parte 1##

class MiExcepcion(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        
    def __str__(self):
        return "Error con el numero introducido -> {}".format(self.mensaje)

maximo = 10

def pedir_numero():
    while True:
        try:
            numero = int(input("Introduce un número entero: "))
            if numero > maximo:
                raise MiExcepcion("El número es mayor que {}".format(maximo))
            return numero
        except ValueError:
            print("Error: Debes introducir un número entero.")
        except MiExcepcion as e:
            print(f"Error: {str(e)}")
            

##Parte 2##

def abrir_archivo(fichero):
    try:
        archivo = open(fichero, "r")
    except FileNotFoundError:
        print(f"Error: El archivo '{fichero}' no existe.")
    except IOError:
        print(f"Error: No se pudo abrir el archivo '{fichero}'.")
    except Exception as e:
        print(f"Error inesperado: {str(e)}")
    finally:
        try:
            archivo.close()
        except NameError:
            pass
        
pedir_numero()
abrir_archivo('archivo.txt')