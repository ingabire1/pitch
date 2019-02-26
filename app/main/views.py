from flask import render_template,request,redirect,url_for,abort
from ..models import User
from . import main

# from ..requests import get_news,get_newsd,search_news
from .forms import ReviewForm,UpdateProfile
from .. import db,photos
# from ..models import Arti

from flask_login import login_required,current_user
import markdown2

# Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    # technology_news = get_news('technology')
    # general_news = get_news('general')
    # entertainment_news = get_news('entertainment')

    title = 'Home - Welcome to The best News Review Website Online'

    # search_news = request.args.get('news_query')
    #
    # if search_news:
    #     return redirect(url_for('search',news_title=search_news))
    # else:
        return render_template('index.html', title = title,technology = technology_news,general = general_news, entertainment = entertainment_news )

# @main.route('/news/<id>')
# def newsd(id):
#
#     '''
#     View news page function that returns the news details page and its data
#     '''
#     technology_news = get_newsd(id)
#
#     title = 'Home - Welcome to The Articles'
#
#     search_news = request.args.get('news_query')
#
#     if search_news:
#         return redirect(url_for('search',news_title=search_news))
#     else:
#         return render_template('news.html', title = title,technology = technology_news)
#

# @main.route('/search/<news_title>')
# def search(news_title):
#     '''
#     View function to display the search results
#     '''
#     news_title_list = news_title.split(" ")
#     news_title_format = "+".join(news_title_list)
#     searched_news = search_news(news_title_format)
#     title = f'search results for {news_title}'
#
#     return render_template('search.html',news = searched_news)
#
# @main.route('/news/review/new/<id>', methods = ['GET','POST'])
# @login_required
# def new_review(id):
#     form = ReviewForm()
#     news = get_newsd(id)
#
#     if form.validate_on_submit():
#         title = form.title.data
#         review = form.review.data
#         new_review = Review(news.id,title,news.poster,review)
#         new_review.save_review()
#         return redirect(url_for('news',id = news.id ))
#
#     title = f'{news.title} review'
#     return render_template('new_review.html',title = title, review_form=form, news=news)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

# @main.route('/review/<int:id>')
# def single_review(id):
#     review=Review.query.get(id)
#     if review is None:
#         abort(404)
#     format_review = markdown2.markdown(review.movie_review,extras=["code-friendly", "fenced-code-blocks"])
#     return render_template('review.html',review = review,format_review=format_review)
