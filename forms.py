from wtforms import validators,Form,FloatField,RadioField,SelectField,StringField


class UserForm(Form):
    x1 = FloatField("x1")
    y1 = FloatField("y1")
    x2 = FloatField("x2")
    y2 = FloatField("y2")


class calculadoraResistencia(Form):
    primerBanda =  SelectField("primerBanda", choices=[("Negro", "Negro"), ("Café", "Café"), ("Rojo", "Rojo"), ("Naranja", "Naranja"), ("Amarillo", "Amarillo"), ("Verde", "Verde"), ("Azul", "Azul"), ("Violeta", "Violeta"), ("Gris", "Gris"), ("Blanco", "Blanco")])
    segundaBanda = SelectField("segundaBanda", choices=[("Negro", "Negro"), ("Café", "Café"), ("Rojo", "Rojo"), ("Naranja", "Naranja"), ("Amarillo", "Amarillo"), ("Verde", "Verde"), ("Azul", "Azul"), ("Violeta", "Violeta"), ("Gris", "Gris"), ("Blanco", "Blanco")])
    tercerBanda = SelectField("tercerBanda", choices=[("Negro", "Negro"), ("Café", "Café"), ("Rojo", "Rojo"), ("Naranja", "Naranja"), ("Amarillo", "Amarillo"), ("Verde", "Verde"), ("Azul", "Azul"), ("Violeta", "Violeta"), ("Gris", "Gris"), ("Blanco", "Blanco")])
    tolerancia = RadioField("Tolerancia", choices=[("oro", "Oro"), ("plata", "Plata")])


class Documentos(Form):
    ingles = StringField("ingles",[
        validators.DataRequired(message='El campo es requerido.'),
        validators.length(min=2,max=10,message='El minimo es 4 y el máximo es 10'),
    ])
    espaniol = StringField("español",[
        validators.DataRequired(message='El campo es requerido.'),
        validators.length(min=2,max=10,message='El minimo es 4 y el máximo es 10'),
    ])
    
class buscar(Form):
    idiomas = RadioField("", choices=[("espanio", "Español"), ("ingles", "Inglés")])
    busqueda = StringField("",[
        validators.DataRequired(message='El campo es requerido.'),
        validators.length(min=2,max=10,message='El minimo es 4 y el máximo es 10'),
    ])
    