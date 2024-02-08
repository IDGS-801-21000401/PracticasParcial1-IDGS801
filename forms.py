from wtforms import Form,FloatField,RadioField,SelectField


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


