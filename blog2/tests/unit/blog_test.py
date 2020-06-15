from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Test title', 'Test author')

        self.assertEqual('Test title', b.title)
        self.assertEqual('Test author', b.author)
        self.assertListEqual([], b.posts)

    def test_repr(self):
        b = Blog('Test title', 'Test author')
        b.posts = ['test post']
        b2 = Blog('My Day', 'Rolf')
        b2.posts = ['test post', 'test 2']

        self.assertEqual(b.__repr__(), 'Test title by Test author (1 post )')

