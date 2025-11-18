from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, URL

class SiteForm(FlaskForm):
    nome = StringField("Nome do Site", validators=[
        DataRequired(message="Nome obrigatório"),
        Length(min=3, max=100, message="Nome deve ter entre 3 e 100 caracteres")
    ])

    url = StringField("URL do Site", validators=[
        DataRequired(message="URL obrigatória"),
        URL(message="Informe uma URL válida")
    ])

    submit = SubmitField("Cadastrar")
