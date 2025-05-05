#!/usr/bin/env python3

def nth_letters(words):
    """
    words: lista de strings
    """
    result = []
    for i, w in enumerate(words):
        if len(w) > i:
            result.append(w[i])
        else:
            print(f'La palabra "{w}" no es válida: longitud ({len(w)}) '
                  f'menor que su posición (i={i}).')
    return ''.join(result)


if __name__ == "__main__":
    # Caso válido
    print("Resultado:", nth_letters(["yoda", "best", "has"]))  # "yes"
    # Caso con palabra demasiado corta
    print("Resultado:", nth_letters(["uno", "dos", "hi"]))     
    # Avisará que "hi" no es válida (len=2 <= i=2) y devolverá "ud"
