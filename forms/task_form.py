from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class TaskForm(FlaskForm):
    content = StringField('Content', validators=[DataRequired()])
    submit = SubmitField('Submit')