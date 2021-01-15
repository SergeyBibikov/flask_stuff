from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired,DataRequired, Email, EqualTo

class RegistrationForm(FlaskForm):
    email = StringField("Email", 
        validators = [InputRequired(message="Пожалуйста, введите e-mail"),
                      Email("Некорректный формат")])
    username = StringField("Username", 
        validators = [DataRequired(message="Пожалуйста, введите имя пользователя")])
    password = PasswordField("Password", validators = [DataRequired(message="Пожалуйста, введите пароль")])
    conf_password = PasswordField("Confirm Password",
        validators = [DataRequired(),EqualTo("password",message="Пароли не совпадают")])
    submit = SubmitField("Submit")