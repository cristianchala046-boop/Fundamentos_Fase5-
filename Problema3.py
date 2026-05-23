# =====================================================================
# CURSO: Fundamentos de Programación (Código: 213022)
# FASE 5: Evaluación Final POA - Problema 3
# PARADIGMA: Programación Estructurada
# =====================================================================

def calcular_cantidad_a_pedir(stock_actual, stock_minimo):
    """
    Módulo (función) encargado de calcular la cantidad exacta a pedir 
    para un artículo con base en la lógica de negocio.
    """
    if stock_actual < stock_minimo:
        # Si el stock actual es menor al mínimo, se pide la diferencia
        cantidad_a_pedir = stock_minimo - stock_actual
    else:
        # Si el stock actual es suficiente, no se solicita nada
        cantidad_a_pedir = 0
        
    return cantidad_a_pedir


def generar_informe_auditoria(inventario):
    """
    Módulo encargado de procesar la matriz de inventario e imprimir 
    la lista final de pedidos requerida.
    """
    print("\n=============================================")
    print("      INFORME DE PEDIDOS DE REABASTECIMIENTO  ")
    print("=============================================")
    print(f"{'ARTÍCULO':<20} | {'CANTIDAD SOLICITADA':<15}")
    print("---------------------------------------------")
    
    # Recorrido de la matriz fila por fila
    for articulo in inventario:
        codigo = articulo[0]
        nombre = articulo[1]
        stock_actual = articulo[2]
        stock_minimo = articulo[3]
        
        # Llamado al módulo de cálculo
        cantidad_final = calcular_cantidad_a_pedir(stock_actual, stock_minimo)
        
        # Salida en pantalla
        print(f"{nombre:<20} | {cantidad_final:<15}")
    
    print("=============================================\n")


def main():
    """
    Función principal que actúa como punto de entrada del programa.
    """
    # Matriz inicial de datos con al menos 5 artículos:
    # Formato: [Código Artículo, Nombre, Stock Actual, Stock Mínimo Requerido]
    inventario_matriz = [
        ["ART001", "Teclado Mecánico", 12, 15],
        ["ART002", "Mouse Ergonómico", 30, 20],
        ["ART003", "Monitor 24' Full HD", 3, 8],
        ["ART004", "Auriculares Gamer", 5, 5],
        ["ART005", "Memoria RAM 16GB", 2, 10]
    ]
    
    # Ejecución del reporte
    generar_informe_auditoria(inventario_matriz)


# Ejecución del programa estructurado
if __name__ == "__main__":
    main()
