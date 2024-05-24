class Ejercicio2:
    # Declaración de propiedades
    numero = 0

    # Declaración del constructor de la clase
    def __init__(self, a) -> None:
        self.numero = a

    # Declaración de los métodos de la clase
    def ingresar_numeros(self):
        numeros = []
        for i in range(self.numero):
                num = int(input(f"Ingrese el número {i + 1}: "))
                numeros.append(num)
        return numeros

    def ejercicio2(self):
        numeros = self.ingresar_numeros()

        print("Lista de números ingresados:", numeros)

        # Obtener la cantidad de veces que se repite cada número
        repeticiones = {numero: numeros.count(numero) for numero in set(numeros)}

        # Ordenar los numeros
        ordenados = sorted(numeros)
        # Separar los números en pares
        pares = [numero for numero in numeros if numero % 2 == 0]
        # Separar los números en impares
        impares = [numero for numero in numeros if numero % 2 != 0]
        # Separar los números en repetidos
        repetidos = [numero for numero, count in repeticiones.items() if count > 1]
        

if __name__ == "__main__":
    main()
