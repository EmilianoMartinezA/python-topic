#!/usr/bin/env python3
"""
Clase Dictionary con validación de entradas repetidas.
"""

class Dictionary:
    def __init__(self):
        self._data = {}

    def newentry(self, word, entry):
        """
        Agrega una nueva palabra al diccionario.
        Si la palabra ya existe, no la sobreescribe y avisa por consola.
        """
        if word in self._data:
            print(f'La palabra "{word}" ya existe en el diccionario.')
        else:
            self._data[word] = entry
            print(f'Entrada agregada: {word} -> "{entry}"')

    def look(self, word):
        """
        Busca la palabra en el diccionario.
        Devuelve la definición o un mensaje de error.
        """
        if word in self._data:
            return self._data[word]
        else:
            return f"Can't find entry for {word}"


if __name__ == "__main__":
    d = Dictionary()
    # Primer intento: se agrega
    d.newentry('Apple', 'A fruit that grows on trees')
    # Segundo: ya existe
    d.newentry('Apple', 'Otra definición')
    # Búsquedas
    print(d.look('Apple'))   # A fruit that grows on trees
    print(d.look('Banana'))  # Can't find entry for Banana
