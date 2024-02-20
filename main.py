from flask import Flask, render_template, request
from forms import UserForm,calculadoraResistencia,Documentos,buscar
from math import sqrt
from io import open

app = Flask(__name__)

### EJERCICIO 3
### CALCULADOR

@app.route("/calculadora", methods=["POST"])
def result():
    if request.method == "POST":
        operacion = request.form.get("operacion")
        num1 = request.form.get("n1")
        num2 = request.form.get("n2")

        if operacion == "Suma":
            return "La suma de {} + {} = {}".format(num1, num2, str(int(num1) + int(num2)))
        elif operacion == "Resta":
            return "La resta de {} - {} = {}".format(num1, num2, str(int(num1) - int(num2)))
        elif operacion == "Multiplicacion":
            return "La multiplicación de {} * {} = {}".format(num1, num2, str(int(num1) * int(num2)))
        elif operacion == "Division":
            if int(num2) != 0:
                return "La división de {} / {} = {}".format(num1, num2, str(int(num1) / int(num2)))
            else:
                return "Error: División por cero"

        # Agrega un retorno por defecto en caso de que la operación no sea reconocida
        return "Operación no válida"


### EJERCICIO 4 
### DISTANCIA
    
@app.route("/distancia", methods=["GET", "POST"])
def distancia():
    ejercicio = UserForm(request.form)
    x1 = ""
    x2 = ""
    y1 = ""
    y2 = ""
    resultado = ""
    if request.method == "POST":
        x1 = ejercicio.x1.data
        y1 = ejercicio.y1.data
        x2 = ejercicio.x2.data
        y2 = ejercicio.y2.data

        resultado = sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return render_template("distancia.html",form=ejercicio,x1=x1, y1=y1, x2=x2, y2=y2, resultado = resultado)


### EXAMEN
### CALCULADORA DE RESISTENCIAS

## ORO Y PLATA
## 5%      10%
@app.route("/resistencias", methods=["GET", "POST"])
def resistencias():
    resistencia = calculadoraResistencia(request.form)
    primerBanda = ""
    segundaBanda = ""
    tercerBanda = ""
    tolerancia = ""
    resultado = ""
    colores_resistencia = ["Negro", "Café", "Rojo", "Naranja", "Amarillo", "Verde", "Azul", "Violeta", "Gris", "Blanco"]
    valores_colores = {"Negro": 0,"Café": 1,"Rojo": 2,"Naranja": 3,"Amarillo": 4,"Verde": 5,"Azul": 6,"Violeta": 7,"Gris": 8,"Blanco": 9,"oro": 0.05, "plata": 0.10}
    multiplicador = {"Negro":1,"Café":10,"Rojo":100,"Naranja":1000,"Amarillo":10000,"Verde":100000,"Azul":1000000,"Violeta":10000000,"Gris":100000000,"Blanco":1000000000}
    min_resistencia = ""
    max_resistencia = ""
    valor_resistencia = ""
    
    if request.method == "POST":
        primerBanda = resistencia.primerBanda.data
        segundaBanda = resistencia.segundaBanda.data
        tercerBanda = resistencia.tercerBanda.data
        tolerancia = resistencia.tolerancia.data

        # Calcular el valor de la resistencia
        valor_resistencia = (valores_colores[primerBanda] * 10 + valores_colores[segundaBanda]) * multiplicador[tercerBanda]
    
        # Calcular los valores máximo y mínimo con tolerancia
        min_resistencia = valor_resistencia + (valor_resistencia * valores_colores[tolerancia])
        max_resistencia = valor_resistencia - (valor_resistencia * valores_colores[tolerancia])
        
        print(max_resistencia)
        print(min_resistencia)
    return render_template("resistencias.html",form=resistencia, colores_resistencia = colores_resistencia, resultado = resultado, primerBanda = primerBanda, segundaBanda = segundaBanda, tercerBanda = tercerBanda, tolerancia=tolerancia,valor_resistencia=valor_resistencia, min_resistencia = min_resistencia, max_resistencia = max_resistencia)


######################
###### Archivos ######
######################
@app.route("/documentos", methods=["GET", "POST"])
def documentos():
    ingles = ""
    espaniol = ""
    busqueda = ""
    documentos = Documentos(request.form)
    form_busqueda = buscar(request.form)  # Crear una instancia del formulario de búsqueda
    resultado = ""
    error = ""

    if request.method == "POST":
        if "action" in request.form:  
            if request.form["action"] == "Registrar" and documentos.validate():
                ingles = documentos.ingles.data
                espaniol = documentos.espaniol.data
                archivo = open('archivo.txt','a')
                archivo.write(espaniol + "," + ingles + "\n")
                archivo.close()
                documentos.ingles.data = ""
                documentos.espaniol.data = ""
                documentos = Documentos()

            elif request.form["action"] == "Buscar" and form_busqueda.validate():  
                busqueda = form_busqueda.busqueda.data.lower()  
                resultado = ""  

                with open('archivo.txt', 'r') as archivo:
                    for linea in archivo:
                        palabras = linea.strip().split(",")  
                        print(palabras)
                        if busqueda == palabras[0].strip().lower(): 
                            resultado = palabras[1].strip() 
                            error = ""
                            break
                        elif busqueda == palabras[1].strip().lower(): 
                            resultado = palabras[0].strip()  
                            error = ""
                            break
                    
                if resultado == "":
                    resultado = "No se encontró ningún valor" 
                    error = "error"
    return render_template("documentos.html", form=documentos, form2=form_busqueda,resultado=resultado, error=error)



if __name__ == "__main__":
    app.run(debug=True)