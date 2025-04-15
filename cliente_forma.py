from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms.fields.simple import StringField, SubmitField, HiddenField
from wtforms.fields.numeric import IntegerField

class ClienteForma(FlaskForm):
    
    nombre = StringField('Nombre', validators=[DataRequired()])
    apellido = StringField('Apellido', validators=[DataRequired()])
    membresía = IntegerField('Membresía', validators=[DataRequired()])
    guardar = SubmitField('Guardar')
    id = HiddenField('id')