from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo

class RegistrationForm(FlaskForm):
    email = StringField("Email", validators = [DataRequired(),Email()], render_kw={"placeholder":"example@example.com"})
    username = StringField("Username", validators = [DataRequired()], render_kw={"placeholder":"JohnDoe"})
    password = PasswordField("Password", validators = [DataRequired()])
    conf_password = PasswordField("Confirm Password",validators = [DataRequired(),EqualTo("password")])
    submit = SubmitField("Submit")