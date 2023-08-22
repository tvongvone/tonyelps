from flask_wtf import FlaskForm
from wtforms import TextAreaField, IntegerField
from wtforms.validators import DataRequired, Length

class ReviewForm(FlaskForm):
    review = TextAreaField('review', validators=[DataRequired(), Length(max=255, min=1)])
    stars = IntegerField('stars', validators=[DataRequired()])
