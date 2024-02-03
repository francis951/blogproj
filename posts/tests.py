from django.test import TestCase
from .models import Post
from django.contrib.auth import get_user_model 
# Create your tests here.

class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username = 'test',
            email = 'test@email.com',
            password = 'tests',
        )
        cls.post = Post.objects.create(
            author = cls.user,
            title = 'Nice title',
            body = 'Nice body',
        )
    def test_posts(self):
        self.assertEqual(self.post.author.username, 'test')
        self.assertEqual(self.post.title, 'Nice title')
        self.assertEqual(self.post.body, 'Nice body')
        self.assertEqual(str(self.post), 'Nice title')