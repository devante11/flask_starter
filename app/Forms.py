from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField, SelectField
from wtforms.validators import InputRequired, DataRequired, Length
from flask_wtf.file import FileField, FileRequired, FileAllowed


class PropertyForm(FlaskForm):
    title = StringField('Property Title',
    validators=[DataRequired()])

    Bedrooms=StringField('No. of Rooms', 
    validators=[DataRequired()])

    Bathrooms=StringField('No. of Bathrooms',
    validators=[DataRequired()])

    Location=StringField('Location',
    validators=[DataRequired()])

    Price=StringField('Price',
    validators= [ DataRequired()])

    HouseType= SelectField('Property Type',
    choices=[('House','House'),('Apartment','Apartment')])

    Description = TextAreaField('Description',
    validators=[DataRequired()])

    Photo=FileField('Photo', 
    validators=[FileRequired(),FileAllowed(['jpg', 'png', 'jpeg', 'Image Files Only'])])