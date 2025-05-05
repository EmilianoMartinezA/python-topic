class Dictionary:
    def __init__(self):
        self.entries = {} # Creacion de un diccionario vacio
    
    def newentry(self, word, definition):
        # Se añade una nueva entrada al diccionario
        self.entries[word] = definition
    
    def look(self, word): 
        # Se busca una palabra en el diccionario
        if word in self.entries:
            return self.entries[word]
        else:
            return f"Can't find entry for {word}"

# Pruebas del ejemplo
d = Dictionary()
d.newentry('Apple', 'A fruit that grows on trees')
print(d.look('Apple'))  # Debería imprimir: A fruit that grows on trees
print(d.look('Banana'))  # Debería imprimir: Can't find entry for Banana