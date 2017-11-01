from ..models import User
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,ValidationError,BooleanField
from wtforms.validators import Required,Email,EqualTo


class RegistrationForm(FlaskForm):
     email=StringField('Your Email Address',validators=[Required(),Email()])
     username=StringField('Enter your username', validators=[Required()])
     password=PasswordField('Password',validators=[Required(),
     EqualTo('password_confirm',message='passwords must match')])
     password_confirm=PasswordField('Confirm Password',validators=[Required()])
     submit=SubmitField('Sign Up')

     def validator_email(self,data_field):
          if User.query.filter_by(email=data_field.data).first():
               raise ValidationError('There is an account with that email')

     def validator_username(self,data_field):
          if User.query.filter_by(username=data_field.data).first():
               raise ValidationError('The username is taken')


class LoginForm(FlaskForm):
     email=StringField('Your Email Address', validators=[Required(),Email()])
     password=PasswordField('Password',validators=[Required()])
     remember=BooleanField('Remember me')
     submit=SubmitField('Sign In')