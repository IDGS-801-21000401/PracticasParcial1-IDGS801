class Ejercicio1:
    # Declaración de propiedades
    numero = 0

    # Declaración del constructor de la clase
    def __init__(self, a) -> None:
        self.numero = a

    # Declaración de los métodos de la clase
    def imprimir_estrellas(self):
        for i in range(1, self.numero + 1):
            print('*' * i)


def main():
    # las estrellas
        txtNumero = int(input("Ingrese un número para hacer las estrellas: "))
        obj = Ejercicio1(txtNumero)
        obj.imprimir_estrellas()


if __name__ == "__main__":
    main()
