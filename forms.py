from wtforms import Form, StringField, IntegerField, PasswordField, EmailField, RadioField, validators

class UserForm(Form):
    matricula = IntegerField('Matricula', [
        validators.DataRequired(message="El campo es requerido"),
        validators.NumberRange(min=100, max=1000, message="Ingrese un valor valido"),
    ])
    nombre = StringField("Nombre", [
        validators.DataRequired(message="El campo es requerido"),
        validators.Length(min=3, max=10, message="Ingrese un valor valido")
    ])
    aPaterno = StringField("Apellido Paterno", [
        validators.DataRequired(message="El campo es requerido"),
    ])
    aMaterno = StringField("Apellido Materno", [
        validators.DataRequired(message="El campo es requerido"),
    ])
    email = EmailField("Correo", [
        validators.Email(message="Ingrese un correo valido"),
    ])
    password = PasswordField("Contraseña", [
        validators.DataRequired(message="El campo es requerido"),
    ])

class CinepolisForm(Form):
    nombre = StringField("Nombre", [
        validators.DataRequired(message="El campo es requerido")
    ])
    compradores = IntegerField("Cantidad Compradores", [
        validators.DataRequired(message="El campo es requerido"),
        validators.NumberRange(min=1, message="Mínimo 1 comprador")
    ])
    boletas = IntegerField("Cantidad de Boletas", [
        validators.DataRequired(message="El campo es requerido"),
        validators.NumberRange(min=1, message="Mínimo 1 boleta")
    ])
    tarjeta = RadioField('¿Tiene Tarjeta Cineco?', 
                         choices=[('SI','Sí'),('NO','No')], 
                         default='NO')