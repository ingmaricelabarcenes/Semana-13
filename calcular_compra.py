def calcular_total(precio, cantidad):
    total = precio * cantidad
    return total


if __name__ == "__main__":
    precio = 50
    cantidad = 12

    resultado = calcular_total(precio, cantidad)

    print("El total de la compra es:", resultado)