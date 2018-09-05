from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,BooleanField
from wtfforms.validators import Required

class ContentForm(FlaskForm):
    content = TextAreaField('YOUR PITCH')
    submit = SubmitField('SUBMIT')

Class CommentForm(FlaskForm):
    comment_id = TextAreaField('WRITE COMMENT')