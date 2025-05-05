def get_total(costs, items, tax_rate):
    total = 0 # total iniciando en 0
    
    # Se suma el costo de cada ítem en la lista de items
    for item in items:
        # Si el ítem existe en el diccionario de costos
        if item in costs:
            total += costs[item]
    
    # se calcula el total mas los impuestos
    total_with_tax = total + (total * tax_rate)
    
    # Redondeo a dos decimales
    return round(total_with_tax, 2)

costs = {'socks': 5, 'shoes': 60, 'sweater': 30}
total = get_total(costs, ['socks', 'shoes'], 0.09)
print(total)  # Debería imprimir: 70.85