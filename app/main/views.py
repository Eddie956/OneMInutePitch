from flask import render_template, request, redirect, url_for
from . import main
from .forms import PitchForm
from flask_login import login_required

# from app.models import Pitch, Comment,Category

@main.route('/')
def index():
    '''
    View root page function that returns index page and the various news sources
    '''
    title = "pitch"

    return render_template("index.html", title=title)

@main.route('/pitch/<pitch:id>', methods = ['GET', 'POST'])
def pitch(id):
    '''
    Function the returns pitch for comment to be added
    '''
    pitch =Pitch.query.get(id)
    comment = Comment.get_comments(pitch_id=id)
    
    if id is None:
        abort(404)

    if comment_form.validate_on_submit():
        comment_list = comment_form.comment.data
        new_comment = Comment(comment_content = comment_list, pitch_id = id, user = current_user)
        new_comment.save_comment()


    title = f'Pitch { pitch.id }'
    return render_template('pitch.html', title=title, pitch=pitch, my_comment=my_comment, )



@main.route('/new/pitch/comment/<''>)
@login_required

def comment():
