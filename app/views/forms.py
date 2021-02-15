from flask_migrate import edit
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField,BooleanField
from wtforms.fields.core import IntegerField
from wtforms.validators import InputRequired,DataRequired, Email, EqualTo, NumberRange, ValidationError
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
    submit = SubmitField("Войти")

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
    search_filter = SelectField(choices=["Начинается с","Содержит","Заканчивается на","Все"])
    manuf_name_search = StringField("Поиск производителя", validators=[InputRequired("Введите строку для поиска")])
    find = SubmitField("Найти")

class ManufacturerAddForm(FlaskForm):
    manuf_name_add = StringField("Название производителя", validators = [InputRequired("Необходимо указать название производителя")])
    manuf_legal_form = SelectField("Форма регистрации")
    add = SubmitField("Добавить")

class ManufacturerEditForm(FlaskForm):
    manuf_enter_name = StringField("Новое название")
    manuf_legal_form = SelectField("Форма регистрации (выберите либо новую, либо текущую)")
    confirm_checkbox = BooleanField("Подтвердить изменение производителя")
    confirm_delete_checkbox = BooleanField("Подтвердить удаление производителя")
    edit_manuf = SubmitField("Изменить данные производителя")
    delete_manuf = SubmitField("Удалить производителя")

class ProductSearchForm(FlaskForm):
    name = StringField("Название продукта")
    search_filter = SelectField(choices=["Начинается с",
                                        "Содержит",
                                        "Заканчивается на",
                                        "Полностью совпадает с"])
    find_product = SubmitField("Найти")

class CartEditItemForm(FlaskForm):
    product_id = IntegerField()
    current_qty=IntegerField('Количество в корзине')
    stock_qty=IntegerField()
    quantity = IntegerField('Новое количество',validators=[NumberRange(min=0)])
    edit_quantity = SubmitField('Изменить количество')
    delete_item = SubmitField('Удалить из корзины')