from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, TextAreaField, SelectField
from wtforms.validators import InputRequired, Optional, NumberRange, URL, Length

class AddPetForm(FlaskForm):
    """Form for adding a pet"""
    name = StringField("Pet name", 
                        validators=[InputRequired()])

    species = SelectField("Species", choices = [("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")])
                  
    photo_url = StringField("Photo", validators=[Optional(), URL()])

    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30, message="Age should be between 0 and 30")])

    notes = TextAreaField("Comments", validators=[Optional(), Length(min=10)])

    available = BooleanField("Available?")


class EditPetForm(FlaskForm):
    """Form for editing existing pet"""

    photo_url = StringField("Photo", validators=[Optional(), URL()])

    notes = TextAreaField("Comments", validators=[Optional(), Length(min=10)])

    available = BooleanField("Available?")


