from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired,DataRequired, Email, EqualTo, ValidationError
from ..models import Users
from ..utils.passw_hash import is_passw_correct

class RegistrationForm(FlaskForm):
    email = StringField("Email", 
        validators = [InputRequired(message="Пожалуйста, введите e-mail"),
                      Email("Некорректный формат")])
    username = StringField("Username", 
        validators = [DataRequired(message="Пожалуйста, введите имя пользователя")])
    password = PasswordField("Password",
        validators = [DataRequired(message="Пожалуйста, введите пароль")])
    conf_password = PasswordField("Confirm Password",
        validators = [DataRequired(message="Пожалуйста, подтвердите пароль"),EqualTo("password",message="Пароли не совпадают")])
    submit = SubmitField("Submit")

    def validate_username(self,username):
        if Users.query.filter_by(username=self.username.data).first():
            raise ValidationError("Пользователь с таким именем уже существует")

    def validate_email(self,email):
        if Users.query.filter_by(email=self.email.data).first():
            raise ValidationError("Пользователь с таким адресом электронной почты уже существует")

class LoginForm(FlaskForm):
    username = StringField("Username", 
        validators = [DataRequired(message="Пожалуйста, введите имя пользователя")])
    password = PasswordField("Password",
        validators = [DataRequired(message="Пожалуйста, введите пароль")])
    submit = SubmitField("Log in")

    def validate_username(self,irrelevant):
        if not Users.query.filter_by(username=self.username.data).first():
            raise ValidationError("Некорректное имя пользователя или пароль")

    def validate_password(self,irrelevant):
        try:
            password = Users.query.filter_by(username=self.username.data).first().password
        except:
            raise ValidationError("Некорректное имя пользователя или пароль")
        if not is_passw_correct(password,self.password.data):
            raise ValidationError("Некорректное имя пользователя или пароль")
   