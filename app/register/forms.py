from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired, Length


class ClientForm(FlaskForm):
    """Client Form."""
    greeting = StringField('Saludo', id='greeting', validators=[DataRequired()])  # noqa
    first_name = StringField('Nombres', id='first_name', validators=[DataRequired()])  # noqa
    last_name = StringField('Apellidos', id='last_name', validators=[DataRequired()])  # noqa
    company = StringField('Organización', id='company', validators=[DataRequired()])  # noqa
    position = StringField('Cargo', id='position', validators=[DataRequired()])  # noqa
    address = StringField('Dirección', id='address', validators=[DataRequired()])  # noqa
    phone = StringField('Teléfono', id='phone', validators=[DataRequired()])  # noqa
    email = StringField('E-mail', id='email', validators=[DataRequired()])  # noqa
