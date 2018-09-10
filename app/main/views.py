from flask import render_template, request, redirect, url_for,flash, abort
from . import main
from .forms import PitchForm, UpdateProfile,ContentForm,CommentForm
from flask_login import login_required,current_user
from ..models import  User,Pitch,Comment,Like,Dislike,PhotoProfile
from .. import db,photos
import markdown2



# from app.models import Pitch, Comment,Category

@main.route('/')
def index():
    '''
    View root page function that returns index page and the various news sources
    '''
    title = "pitch"

    return render_template("index.html", title=title)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user=user)


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

        return redirect(url_for('.update_profile', id_user=user.id, uname=user.username))
    title = 'Update Bio'
    return render_template('profile/update.html', title=title,form=form)


@main.route('/user/<uname>/update/pic', methods=['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username=uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile', uname=uname, id_user=user.id))


@main.route('/new/pitch', methods=['GET', 'POST'])
@login_required
def new_pitch():
    pitch_form = PitchForm()

    if pitch_form.validate_on_submit():
        name = pitch_form.name.data
        pitch = pitch_form.pitch.data
        category = pitch_form.category.data

        new_pitch = Pitch(pitch_form=pitch,category=category,name=name)
        new_pitch.save_pitch()

        return redirect(url_for('main.new_pitch'))

    # pitch = Pitch.pitches()

    title = 'Minute'
    return render_template('new_pitch.html', title=title, pitch_form=pitch_form)


@main.route('/new/comment/<int:pitch_id>')
@login_required
def comment(pitch_id):
    '''
    route to view new comment
    '''


@main.route('/category/<category>')
def category(cat):
    category = Pitch.get_category(category)

    title =  'category' 
    pitch_in_category = Pitch.get_pitch
    return render_template('category.html', title=title, category=category,pitches=pitch_in_category)


@main.route('/pitch/<int:id>', methods=['GET', 'POST'])
@login_required
def pitch(id):

    pitch = Pitch.query.get(id)
    comment_form = CommentForm()

    if id is None:
        abort(404)
    if comment_form.validate_on_submit():
        comment_form = comment_form.comment.data
        new_comment = Comment(comment_content=comment_data,pitch_id=id, user=users)
        new_comment.save_comment()
        return redirect(url_for('main.pitch', id=id))
    all_comments = Comment.get_comments(id)
    like = Like.get_votes(id)
    dislike = Dislike.get_downvotes(id)

    title = 'Comment'
    return render_template('pitch.html', pitch=pitch, comment_form=comment_form, comments=all_comments, title=title, like=like, dislike=dislike)



@main.route('/pitch/like/<int:pitch_id>/like')
@login_required
def like(pitch_id):
    '''
    route to view number of likes
    '''
    get_pitches = Like.get_votes(id)
    valid_string = f'{current_user.id}:{id}'

    for pitch in get_pitches:
        to_str = f'{pitch}'
        print(valid_string+" "+to_str)
        if valid_string == to_str:
            return redirect(url_for('main.pitch', id=id))
        else:
            continue

    like_pitch = Like(user=user, pitching_id=id)
    like_pitch.save_vote()

    return redirect(url_for('main.pitch', id=id))


@main.route('/pitch/dislike/<int:pitch_id>//dislike' )
@login_required
def dislike(pitch_id):
    '''
    route to view number of dislikes
    '''
    get_pitches = Dislike.get_downvotes(id)
    valid_string = f'{current_user.id}:{id}'
    for get_pitch in get_pitches:
        to_str = f'{get_pitch}'
        print(valid_string+" "+to_str)
        if valid_string == to_str:
            return redirect(url_for('main.pitch', id=id))
        else:
            continue
    dislike_pitch = Like(user=user, pitching_id=id)
    dislike_pitch.save_vote()
    return redirect(url_for('main.pitch', id=id))
