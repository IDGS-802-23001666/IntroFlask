from flask import Flask, render_template, request


app=Flask(__name__)

@app.route('/hola')
def index():
    return "hola, hola"

@app.route('/')
def hola():
    titulo = "IDGS-802-Flask"
    lista = ['Juan', 'Karla', 'Miguel']
    return render_template('index.html', titulo=titulo, lista=lista)

@app.route('/formularios')
def formularios():
    return render_template('formularios.html')


@app.route('/reportes')
def reportes():
    return render_template('reportes.html')


@app.route('/user/<string:user>')
def user(user):
    return "Hola " + user

@app.route('/numero/<int:n>')
def numero(n):
    return "Numero: {}".format(n)

@app.route('/user/<int:id>/<string:username>')
def username(id, username):
    return "ID: {} Nombre: {}".format(id, username)

@app.route('/suma/<float:n1>/<float:n2>')
def suma(n1, n2):
    return "La suma es: {}".format(n1+n2)

@app.route('/default')
@app.route('/default/<string:param>')
def func(param="juan"):
    return f"<h1> !Hola, {param}!</h1>"

@app.route("/operas")
def operas():
    return '''
        <form>
        <label for = "name">Name:</label>
        <input type = "text" id = "name" name = "name" required>
        <br>
        <br>
        <label for = "name">A_Paterno:</label>
        <input type = "text" id = "apaterno" name = "apaterno" required>
        </form>
    '''

@app.route("/operasBas")
def operasBas():
    return render_template('operasBas.html')

@app.route("/resultado", methods=["GET", "POST"])
def resultado():
    if request.method == "POST":
        n1 = float(request.form.get("num1"))
        n2 = float(request.form.get("num2"))
        op = request.form.get("operacion")
        
        res = 0
        texto_op = ""

        if op == "suma":
            res = n1 + n2
            texto_op = "suma"
        elif op == "resta":
            res = n1 - n2
            texto_op = "resta"
        elif op == "multi":
            res = n1 * n2
            texto_op = "multiplicación"
        elif op == "divi":
            if n2 != 0:
                res = n1 / n2
                texto_op = "división"
            else:
                return "Error: No se puede dividir entre cero."

        return f"El resultado de la {texto_op} es: {res}"
    

if __name__  == '__main__':
    app.run(debug = True)

