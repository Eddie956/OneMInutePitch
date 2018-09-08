from flask import render_template, request, redirect, url_for, abort
from . import main
from .forms import PitchForm, UpdateProfile,ContentForm,CommentForm
from flask_login import login_required
from ..models import  User
from .. import db,photos



# from app.models import Pitch, Comment,Category

@main.route('/')
def index():
    '''
    View root page function that returns index page and the various news sources
    '''
    title = "pitch"

    return render_template("index.html", title=title)


@main.route('/user/<uname>/update', methods=['GET', 'POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('main.update_profile', uname=user.username))

    return render_template('profile/update.html', form=form)


@main.route('/user/<uname>/update/pic', methods=['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username=uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile', uname=uname))
@main.route('/new/pitch')
@login_required
def new_pitch():
    '''
    route to view new pitches
    '''


@main.route('/new/comment/<int:pitch_id>')
@login_required
def comment(pitch_id):
    '''
    route to view new comment
    '''


@main.route('/new/pitch/upvote/<int:pitch_id>/upvote')
@login_required
def upvote(pitch_id):
    '''
    route to upvote pitches
    '''


@main.route('/new/pitch/downvote/<int:pitch_id>//downvote' )
@login_required
def downvote(pitch_id):
    '''
    route to view new pitches
    '''
