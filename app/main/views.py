from flask import render_template,request,redirect,url_for
from . import main

from ..requests import get_news,get_newsd,search_news
from .forms import ReviewForm
from ..models import News
from ..models import Arti
# from ..models import Review

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

# @main.route('/news/<news_id>')
# def news(news_id):
#     '''
#     View news page function that returns the news details page and its data
#     '''
#
#     return render_template('news.html',id = news_id)

@main.route('/news/<id>')
def newsd(id):
    '''
    View news page function that returns the articles page and its data
    '''
    news = get_news('technology')
    news = get_news('general')
    news = get_news('entertainment')
    arti = get_newsd('news.name')
    # title = f'{arti.title}'
    # reviews = Review.get_reviews(arti.id)

    # if News.name.click():
    # title = arti.title
    # description = arti.description.data
    # new_arti = Arti(arti.id,title,arti.poster,description)
    # new_arti.save_review()
        # return redirect(url_for('news',id = news.id ))
    #
    title = 'Home - Welcome to The Articles'
    #     return render_template('new_review.html',title = title, review_form=form, news=news)
    search_arti = request.args.get('arti_query')

    if search_arti:
        return redirect(url_for('search',arti_title=search_arti))
    else:
        return render_template('news.html',title = title,arti = arti,news=news)


@main.route('/news/<descr>')
def descr(id):
    '''
    View news page function that returns the articles descriptions
    '''
    news = get_news('technology')
    news = get_news('general')
    news = get_news('entertainment')
    arti = get_newsd('news.name')

    title = 'Home - Welcome to The Articles descriptions'
    return render_template('descr.html',title = title,arti = arti,news=news)

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
