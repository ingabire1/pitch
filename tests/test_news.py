import unittest
from app.models import News

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News('abc-news-au','ABC News (AU)','Australia s most trusted source of local, national and world news. Comprehensive, independent, in-depth analysis, the latest business, sport, weather and more.','"http://www.abc.net.au/news','en','au')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))
