from flask import Flask,render_template,request
app=Flask(__name__)


@app.route("/OperasBas",methods=["GET","POST"])
def operaBas():
    return render_template("OperasBas.html")

@app.route("/resultado",methods=["GET","POST"])
def result():
    if request.method == "POST":
        suma = request.form.get("btnSuma")
        resta = request.form.get("btnResta")
        multiplicacion = request.form.get("btnMultiplicacion")
        division = request.form.get("btnDivision")
        num1 = request.form.get("n1")
        num2 = request.form.get("n2")
    
        if multiplicacion == "on":
            return "La multiplicación de {} y {} = {}".format(num1, num2, str(int(num1)* int(num2)))   
        if suma == "on":
            return "La suma de {} y {} = {}".format(num1, num2, str(int(num1)+int(num2)))
        if resta == "on":
            return "La resta de {} y {} = {}".format(num1, num2, str(int(num1)-int(num2)))
        if division == "on":
            return "La division de {} y {} = {}".format(num1, num2, str(int(num1)/int(num2)))
        
        

       

if __name__ == "__main__":
    app.run(debug=True)