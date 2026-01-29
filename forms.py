from wtforms import Form
from wtforms import StringField, IntegerField, PasswordField, EmailField
from wtforms import validators

class UserForm(Form):
    matricula = IntegerField('Matricula', [
        validators.DataRequired(message = "El campo es requido"),
        validators.NumberRange(min = 100, max = 1000, message="Ingrese un valor valido"),
    ])
    nombre = StringField("Nombre",  [
        validators.DataRequired(message = "El campo es requido"),
        validators.Length(min = 3, max = 10, message="Ingrese un valor valido")
    ])
    aPaterno = StringField("Apellido Paterno",  [
        validators.DataRequired(message = "El campo es requido"),
    ])
    aMaterno = StringField("Apellido Materno",  [
        validators.DataRequired(message = "El campo es requido"),
    ])
    email = EmailField("Correo",  [
        validators.Email(message = "Ingrese un correo valido"),
    ])
    password = PasswordField("Contraseña",  [
        validators.DataRequired(message = "El campo es requido"),
    ])
