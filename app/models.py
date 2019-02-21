class News:
    '''
    News class to define News Objects
    '''

    def __init__(self,id,name,description,url,language,country):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.language = language
        self.country = country

class Arti:
    '''
    News class to define Articles Objects
    '''

    def __init__(self,id,name,title,poster,description,publishedAt,content,url):
        self.id = id
        self.name = name
        self.title = title
        self.poster = poster
        self.description = description
        self.publishedAt = publishedAt
        self.content = content
        self.url = url

    # def save_review(self):
    #     Review.all_reviews.append(self)
    #
    #
    # @classmethod
    # def clear_reviews(cls):
    #     Review.all_reviews.clear()
    #
    # @classmethod
    # def get_reviews(cls,id):
    #
    #     response = []
    #
    #     for review in cls.all_reviews:
    #         if review.news_id == id:
    #             response.append(review)
    #
    #     return response
    #

# class Review:
#
#     all_reviews = []
#
#     def __init__(self,news_id,title,urlToImage,review):
#         self.news_id = news_id
#         self.title = title
#         self.urlToImage = urlToImage
#         self.description = description
#
#
#     def save_review(self):
#         Review.all_reviews.append(self)
#
#
#     @classmethod
#     def clear_reviews(cls):
#         Review.all_reviews.clear()
#
#     @classmethod
#     def get_reviews(cls,id):
#
#         response = []
#
#         for review in cls.all_reviews:
#             if review.news_id == id:
#                 response.append(review)
#
#         return response
