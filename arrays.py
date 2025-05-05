def extract_letters(words):
    # Si la lista está vacía, entonces un string vacío
    if not words:
        return ""
    
    result = ""
    
    # se recorre cada palabra en la lista
    for i, word in enumerate(words):
        # Verifico que la palabra tenga suficientes letras
        if i < len(word):
            # se añaden las letras de cada palabra a la cadena resultante
            result += word[i]
    
    return result

print(extract_letters(["yoda", "best", "has"]))  # Debería imprimir "yes"