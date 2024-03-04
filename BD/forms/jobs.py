from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class JobsForm(FlaskForm):
    title = StringField('Job Title', validators=[DataRequired()])
    leader = StringField('Team Leader id', validators=[DataRequired()])
    work_size = IntegerField('Work Size')
    collaborators = StringField('Collaborators', validators=[DataRequired()])
    is_finish = BooleanField("Is job finished?")
    submit = SubmitField('Add')
