from flask import Flask, render_template, request
from forms import UserForm
from math import sqrt

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)