from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application.models import Users
from flask_login import current_user


class PostForm(FlaskForm):
    title = StringField('Title',
            validators = [
                DataRequired(),
                Length(min=2, max=100)
            ]
    )
    content = StringField('Content',
            validators = [
                DataRequired(),
                Length(min=2, max=1000)
            ]
    )
    submit = SubmitField('Post!')



class RegistrationForm(FlaskForm):
    first_name = StringField('First Name',
            validators = [
                DataRequired(),
                Length(min=2, max=30)
            ]
        )
    last_name = StringField('Last Name',
            validators = [
                DataRequired(),
                Length(min=2, max=30)
            ]
        )
    email = StringField('Email',
            validators = [
                DataRequired(),
                Email()
            ]
        )
    password = StringField('Password',
            validators = [
                DataRequired(),
            ]
        )
    confirm_password = StringField('Confirm Password',
            validators = [
                DataRequired(),
                EqualTo('password')
            ]
        )
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        user = Users.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError('Email already in use')


class LoginForm(FlaskForm):
    email = StringField('Email',
            validators = [
                DataRequired(),
                Email()
            ]
        )
    password = StringField('Password',
            validators = [
                DataRequired()
            ]
        )
    
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    first_name = StringField('First Name',
            validators = [
                DataRequired(),
                Length(min=2, max=30)
            ]
        )
    last_name = StringField('Last Name',
            validators = [
                DataRequired(),
                Length(min=2, max=30)
            ]
        )
    email = StringField('Email',
            validators = [
                DataRequired(),
                Email()
            ]
        )
    submit = SubmitField('Email already in use')
