from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/OperasBas", methods=["GET", "POST"])
def operaBas():
    return render_template("OperasBas.html")

@app.route("/resultado", methods=["POST"])
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

if __name__ == "__main__":
    app.run(debug=True)
