from flask import render_template, request, redirect, url_for
from main import main
from .forms import PitchForm
from ..models import Pitch, Comment,Category

@main.route('/pitch/<pitch:id>', methods = ['GET', 'POST'])

def pitch(id):
    '''
    Function the returns pitch for comment to be added
    '''
    pitch =Pitch.query.get(id)
    comment = Comment.get_comments(pitch_id=id)

    title = f'Pitch { pitch.id }'
    return render_template('pitch.html', title=title, pitch=pitch, comment=comment)