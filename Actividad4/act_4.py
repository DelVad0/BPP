##Parte 1

import pdb
pdb.set_trace()

#Definimos la lista de listas
lists = [[2, 4, 1], [1,2,3,4,5,6,7,8], [100,250,43]]
max_num_list = []

'''
Usammos list comprehension para hacer una  misma operación 
sobre todas las listas dentro de la lista principal
'''
max_num_list = [max(list) for list in lists]

#Imprimos por pantalla para combrobar el resultado
print(f"Mayores numeros de cada lista: {max_num_list}")

#------------------------------------------------------------

##Parte2

list2 = [1, 2, 3, 4, 8, 5, 5, 22, 13]

def es_primo(numero):
    '''
    Función que recibe un numero y devuelve
    True o False si el numero es primo o no
    '''
    if numero <= 1:
        return False
    elif numero == 2:
        return True
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True
    
#Usamos la función filter para pasar la función a todos los elementos de la lista
primos = list(filter(es_primo, list2))
print(f"Numeros primos de la lista: {primos}")