from wtforms import Form,FloatField


class UserForm(Form):
    x1 = FloatField("x1")
    y1 = FloatField("y1")
    x2 = FloatField("x2")
    y2 = FloatField("y2")