def contar_a(texto):
    texto = texto.lower()
    return texto.count('a')



def mostrar_cuadrado():
    numero = int(input("Ingrese un número entero: "))
    print(f"El cuadrado de {numero} es {numero ** 2}")


def mostrar_producto():
    valor1 = float(input("Ingrese el primer valor: "))
    valor2 = float(input("Ingrese el segundo valor: "))
    print(f"El producto de {valor1} y {valor2} es {valor1 * valor2}")


if __name__ == "__main__":
    mostrar_cuadrado()
    mostrar_producto()
