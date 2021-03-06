from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, InputRequired, Regexp
from blog.models import User

class RegistrationForm(FlaskForm):
  username = StringField('Username',validators=[DataRequired(),Length(min=3,max=15)])
  firstname = StringField('firstname',validators=[DataRequired(),Length(min=3,max=15)])
  lastname = StringField('lastname',validators=[DataRequired(),Length(min=2,max=15)])
  email = StringField('Email',validators=[DataRequired(),Email()])
  password = PasswordField('Password',validators=[DataRequired(),Regexp('^.{6,8}$',message='Your password should be between 6 and 8 characters long.')])

  confirm_password = PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password', message='Passwords do not match.')])
  submit = SubmitField('Register')

  def validate_username(self, username):
    user = User.query.filter_by(username=username.data).first()
    if user is not None:
      raise ValidationError('Username already exist. Please choose a different one.')

  def validate_email(self,email):
    user = User.query.filter_by(email=email.data).first()
    if user is not None:
      raise ValidationError('Email address is already associated with an account.')

class LoginForm(FlaskForm):
  email = StringField('Email',validators=[DataRequired(),Email()])
  password = PasswordField('Password',validators=[DataRequired()])
  submit = SubmitField('Login')

  # def validate_email(self,email):
  #   user = User.query.filter_by(email=email.data).first()
  #   if user is not None:
  #     raise ValidationError('You need to verify your email')
  
class CommentForm(FlaskForm):
  comment = StringField('Comment',validators=[InputRequired()])
  submit = SubmitField('Post comment')
