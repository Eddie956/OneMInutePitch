from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,BooleanField
from wtforms.validators import Required

class CategoryForm(FlaskForm):
    category = TextAreaField('YOUR PITCH')
    submit = SubmitField('SUBMIT')


class ContentForm(FlaskForm):
    pitch = TextAreaField('WRITE YOUR PITCH')
    submit = SubmitField('SUBMIT')

class CommentForm(FlaskForm):
    comment = TextAreaField('COMMENT')
    submit = SubmitField('SUBMIT')

class PitchForm(FlaskForm):  
    content = TextAreaField('Pitch', validators=[Required()])
    submit = SubmitField('Submit')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.', validators=[Required()])
    submit = SubmitField('Submit')
