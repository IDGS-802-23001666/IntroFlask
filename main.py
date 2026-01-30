from flask import Flask, render_template, request
from flask import flash
from flask_wtf.csrf import CSRFProtect

import forms


app=Flask(__name__)
app.secret_key = 'Clave secreta'
csrf = CSRFProtect()

@app.route('/hola')
def index():
    return "hola, hola"

@app.route('/')
def hola():
    titulo = "IDGS-802-Flask"
    lista = ['Juan', 'Karla', 'Miguel']
    return render_template('index.html', titulo=titulo, lista=lista)

@app.route("/usuarios", methods = ["GET", "POST"])
def usuarios():
    mat = 0
    nom = ''
    apa = ''
    ama = ''
    email = ''
    usuarios_class = forms.UserForm(request.form)
    if request.method == "POST" and usuarios_class.validate():
        mat = usuarios_class.matricula.data
        nom = usuarios_class.nombre.data
        apa = usuarios_class.aPaterno.data
        ama = usuarios_class.aMaterno.data
        email = usuarios_class.email.data

        mensaje = 'Bienvenido {}'.format(nom)
        flash(mensaje)
        

    return render_template('usuarios.html', form = usuarios_class, mat=mat, nom=nom, apa=apa, ama=ama, email=email) 


@app.route("/cine", methods=["GET", "POST"])
def cine():
    nom = ''
    total = 0
    error = None
    cine_form = forms.CinepolisForm(request.form)
    
    if request.method == "POST" and cine_form.validate():
        nom = cine_form.nombre.data
        comp = cine_form.compradores.data
        cant = cine_form.boletas.data
        tiene_tarjeta = cine_form.tarjeta.data == 'SI'
        
        max_permitido = comp * 7
        
        if cant > max_permitido:
            error = f"Límite excedido. Máximo {max_permitido} boletas."
        else:
            subtotal = cant * 12
            
            if cant > 5:
                subtotal *= 0.85
            elif 3 <= cant <= 5:
                subtotal *= 0.90
                
            if tiene_tarjeta:
                subtotal *= 0.90
            
            total = subtotal

    return render_template('cinepolis.html', form=cine_form, nom=nom, total=total, error=error)

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

@app.route("/operasBas", methods = ["GET", "POST"])
def operasBas():
    n1 = 0
    n2 = 0
    res = 0
    if request.method == "POST":
        n1 = float(request.form.get("num1"))
        n2 = float(request.form.get("num2"))
        res = float(n1)/float(n2)
    return render_template('operasBas.html', n1=n1, n2=n2, res=res)

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
    
@app.route("/alumnos")
def alumnos():
    return render_template('alumnos.html')

@app.route("/distancia", methods=["GET", "POST"]) 
def distancia():
    res = None 
    if request.method == "POST":
        x1 = float(request.form.get("x1"))
        y1 = float(request.form.get("y1"))
        x2 = float(request.form.get("x2"))
        y2 = float(request.form.get("y2"))
        res = ((x2-x1)**2 + (y2-y1)**2)**0.5
    
    return render_template('distancia.html', res=res)



if __name__  == '__main__':
    csrf.init_app(app)
    app.run(debug = True)

