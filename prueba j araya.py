#Joaquin Araya Monsalve Seccion 003

def calcular_consumo_mensual(integrantes):
    consumo_total = 0
    
    for integrante in range(1, integrantes + 1):
        consumo_diario = 7.6  # Consumo del refrigerador
        print(f"Integrante {integrante}:")
        for _ in range(3):  # Máximo 3 artefactos por persona
            artefacto = input("Ingrese el artefacto utilizado (Hervidor, Microondas, Aspiradora, Secador de pelo, Lavadora/Secadora): ").lower()
            if artefacto == "hervidor":
                consumo_diario += 5.9
            elif artefacto == "microondas":
                consumo_diario += 0.8
            elif artefacto == "aspiradora":
                consumo_diario += 4.0
            elif artefacto == "secador de pelo":
                consumo_diario += 4.5
            elif artefacto == "lavadora/secadora":
                consumo_diario += 2.0
            else:
                print("Artefacto no válido. Inténtelo de nuevo.")
        
        consumo_mensual = consumo_diario * 30  # 30 días en un mes
        consumo_total += consumo_mensual
        print(f"Consumo mensual del integrante {integrante}: {consumo_mensual:.2f} kWh\n")
    
    return consumo_total

def main():
    integrantes = int(input("Ingrese el número de integrantes del grupo familiar (máximo 5): "))
    if integrantes > 5:
        print("El número máximo de integrantes es 5. Por favor, inténtelo de nuevo.")
        return
    
    consumo_total = calcular_consumo_mensual(integrantes)
    print(f"El consumo mensual total del grupo familiar es: {consumo_total:.2f} kWh")

if __name__ == "__main__":
    main()

