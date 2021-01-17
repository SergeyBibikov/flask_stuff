from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired,DataRequired, Email, EqualTo, ValidationError
from ..models import User
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
        if User.query.filter_by(username=self.username.data).first():
            raise ValidationError("Пользователь с таким именем уже существует")

    def validate_email(self,email):
        if User.query.filter_by(email=self.email.data).first():
            raise ValidationError("Пользователь с таким адресом электронной почты уже существует")

class LoginForm(FlaskForm):
    username = StringField("Username", 
        validators = [DataRequired(message="Пожалуйста, введите имя пользователя")])
    password = PasswordField("Password",
        validators = [DataRequired(message="Пожалуйста, введите пароль")])
    submit = SubmitField("Log in")

    def validate_username(self,irrelevant):
        if not User.query.filter_by(username=self.username.data).first():
            raise ValidationError("Некорректное имя пользователя или пароль")

    def validate_password(self,irrelevant):
        try:
            password = User.query.filter_by(username=self.username.data).first().password
        except:
            raise ValidationError("Некорректное имя пользователя или пароль")
        if not is_passw_correct(password,self.password.data):
            raise ValidationError("Некорректное имя пользователя или пароль")

class ManufacturerSearchForm(FlaskForm):
    manuf_name_search = StringField("Manufacturer search", validators = [DataRequired("Необходимо указать название производителя")])
    find = SubmitField("Find")
    edit = SubmitField("Edit")
    delete = SubmitField("Delete")

class ManufacturerAddForm(FlaskForm):
    manuf_name_add = StringField("Add manufacturer", validators = [DataRequired("Необходимо указать название производителя")])
    add = SubmitField("Add")