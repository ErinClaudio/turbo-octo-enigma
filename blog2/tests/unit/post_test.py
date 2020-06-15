from unittest import TestCase
from posts import Post


class PostTest(TestCase):
    def test_create_post(self):
        p = Post('Test title', 'Test Content')

        self.assertEqual('Test title', p.title)
        self.assertEqual('Test Content', p.content)


