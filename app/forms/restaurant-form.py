from flask_wtf import FlaskForm
from wtforms import TextAreaField, IntegerField
from wtforms.validators import DataRequired, Length

class RestaurantForm(FlaskForm):
    name = TextAreaField('name', validators=[DataRequired(), Length(max=255, min=1)])
    city = TextAreaField('city', validators=[DataRequired(), Length(max=255, min=1)])
    state = TextAreaField('state', validators=[DataRequired(), Length(max=255, min=1)])
    price_range = IntegerField('price_range', validators=[DataRequired()])
