# 3rd party imports
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo

# Local import
from app.models import Employee


class RegistrationForm(FlaskForm):
    """
    Form for users to create new account

    For the registration form, we require users to fill in their
    email address, username, first name, last name, and their password twice


    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[
        DataRequired(),
        EqualTo('confirm_password')
    ])
    confirm_password = PasswordField('Confirm Password')
    submit = SubmitField('Register')

    def validate_email(self, field):
        """
        Validate entered email

        This function receive data field with entered email.
        If that email is used ValidationError is raised.
        """

        if Employee.query.filter_by(email=field.data).first():
            raise ValidationError('Email is already in use.')

        return None

    def validate_username(self, field):
        """
        Validate entered user's name

        This function receive data field with user's name
        If that name is used ValidationError is raised.
        """
        if Employee.query.filter_by(username=field.data).first():
            raise ValidationError('Username is already in use.')

        return None


class LoginForm(FlaskForm):
    """
    Form for users to login
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
