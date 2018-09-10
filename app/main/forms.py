from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,BooleanField
from wtforms.validators import Required

class ContentForm(FlaskForm):
    content = TextAreaField('YOUR PITCH')
    submit = SubmitField('SUBMIT')

class CommentForm(FlaskForm):
    comment_id = TextAreaField('WRITE COMMENT')
    submit = SubmitField('SUBMIT')

class PitchForm(FlaskForm):  # create a class that inherits from FlaskForm class
    name = StringField('Authors Name', validators=[Required()])
    category = TextAreaField('Category', validators=[Required()])
    pitch = TextAreaField('Pitch', validators=[Required()])
    submit = SubmitField('Submit')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.', validators=[Required()])
    submit = SubmitField('Submit')
