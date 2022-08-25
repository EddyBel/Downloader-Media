from tabulate import tabulate
from unicodedata import normalize
import os
import re


class TOOLS:
    # tabla de video de youtube
    def printDataVideo(array):
        print(tabulate(array, headers=[
            'ID', 'ITAG', 'TYPE', 'RESOLUTION', 'FPS', 'PROGRESSIVE'],
            tablefmt='fancy_grid',
            stralign='center',
            floatfmt='.0f'))
        return True

    # Tabla general
    def printTabulate(array, header=[]):
        print(tabulate(array, headers=header,
                       tablefmt='fancy_grid',
                       stralign='center',
                       floatfmt='.0f'))

    # Validacion de datos
    def validationID(array, valueInput, value):
        validation = False
        while (True):
            for i in array:
                if i[0] == int(valueInput):
                    validation = True
            if validation:
                break
            else:
                valueInput = input(value)
        return valueInput

    # Obtejer objeto seleccionado
    def getObject(array, valueInput):
        for i in array:
            if i[0] == int(valueInput):
                return i

    # Direccion actual
    def dirname():
        return os.path.abspath(os.getcwd())

    # Limpia los caracteres
    def newString(string):
        new_string = re.sub(r"[^a-zA-Z0-9 áéíóú!]", "", string)
        if new_string == '':
            new_string = 'Titulo'
        return new_string


if __name__ == '__main__':
    newString = TOOLS.newString(
        "Qué pasa si China invade Taiwán | ¿Cómo afectará la tecnología y LATAM?")

    print(newString)
