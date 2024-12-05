from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from logBook.models import User

class RegisterForm(FlaskForm):
    def checkUserName(self, userNameToCheck):
        user = User.query.all(userName=userNameToCheck.data).first()
        if user:
            raise ValidationError(f'The user {user} is already used !!')
    
    userName = StringField(
        label='userName:', 
        validators=[DataRequired(), Length(min=2, max=30)])
    password1 = PasswordField(
        label='Password:',
        validators=[Length(min=6, max=80), DataRequired()])
    password2 = PasswordField(
        label='Confirm password:', 
        validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='submit')
