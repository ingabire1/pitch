import unittest
from app.models import Arti

class ArtiTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Articles class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_arti = Arti('the-next-web','The Next Web','Here are the 5 hottest startups in Poland','https://66.media.tumblr.com/e6d09a7e7f079ec25df98bde327d95e5/tumblr_pn7vsr5SvK1qejjfeo1_1280.jpg','Here are the 5 hottest startups in Poland','2019-02-20T09:02:51Z','Here are the 5 hottest startups in Poland')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_arti,Arti))
