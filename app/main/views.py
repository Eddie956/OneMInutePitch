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
