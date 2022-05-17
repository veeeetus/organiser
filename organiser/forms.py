from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, RadioField, DateField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
from organiser.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
         user = User.query.filter_by(username=username.data).first()
         if user is not None:
             raise ValidationError('Please us a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')

class AddTask(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    body = StringField('Description', validators=[DataRequired()])
    deadline = DateField('Deadline', format=('%Y-%m-%d'), validators=[DataRequired()])
    submit = SubmitField('Add')

class DelTask(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    submit = SubmitField('Delete')

class MoveTask(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    phase = RadioField(label='Phase', choices=[('todo', 'todo'),('doing', 'doing'),('done', 'done')], validators=[DataRequired()])
    submit = SubmitField('Move')