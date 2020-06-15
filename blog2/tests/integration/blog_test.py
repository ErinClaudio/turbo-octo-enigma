from unittest import TestCase
from blog import Blog
from post import Post


class BlogTest(TestCase):
    def test_create_post_in_blog(self):
        b = Blog('Test title', 'Test author')
        b.create_post('test post', 'test content ')

        self.assertEqual(len(b.posts), 1)
        self.assertEqual(b.posts[0].title, 'test post')
        self.assertEqual(b.posts[0].content, 'test content ')

    def test_json(self):
        b = Blog('Test title', 'Test author')
        b.create_post('test post', 'test content ')
        expected = {'title': 'Test title', 'author': 'Test author',
                    'posts': [{'title': 'test post',
                               'content': 'test content '}]}

        self.assertDictEqual(expected, b.json())

        expected = {
            'title': 'test title',
            'author': 'test author',
            'posts': [

            ]
        }
