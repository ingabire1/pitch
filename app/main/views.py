from flask import render_template,request,redirect,url_for
from . import main

from ..requests import get_news,get_newsd,search_news
from .forms import ReviewForm
from ..models import Arti

# Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    technology_news = get_news('technology')
    general_news = get_news('general')
    entertainment_news = get_news('entertainment')

    title = 'Home - Welcome to The best News Review Website Online'

    search_news = request.args.get('news_query')

    if search_news:
        return redirect(url_for('search',news_title=search_news))
    else:
        return render_template('index.html', title = title,technology = technology_news,general = general_news, entertainment = entertainment_news )

@main.route('/news/<id>')
def newsd(id):

    '''
    View news page function that returns the news details page and its data
    '''
    technology_news = get_newsd(id)

    title = 'Home - Welcome to The Articles'

    search_news = request.args.get('news_query')

    if search_news:
        return redirect(url_for('search',news_title=search_news))
    else:
        return render_template('news.html', title = title,technology = technology_news)


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
