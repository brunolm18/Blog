from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.utils import timezone
from blog.models import Author, Category, Post, Tag

class ModelTests(TestCase):
    def test_author_creation_and_str(self):
        author = Author.objects.create(
            username='user123',
            first_name='John',
            last_name='Doe',
            email='user123@gmail.com',
            biography='Bio',
            experience=3
        )
        self.assertEqual(str(author), 'user123')
        self.assertGreater(author.experience, 0)

    def test_category_creation_and_str(self):
        category = Category.objects.create(name='Tech', slug='tech')
        self.assertEqual(str(category), 'Tech')

    def test_tag_creation_and_str(self):
        tag = Tag.objects.create(name='django')
        self.assertEqual(str(tag), 'django')

    def test_post_creation_and_str(self):
        author = Author.objects.create(
            username='author1',
            first_name='Jane',
            last_name='Smith',
            email='author1@gmail.com',
            biography='Bio',
            experience=5
        )
        category = Category.objects.create(name='News', slug='news')
        post = Post.objects.create(
            author=author,
            category=category,
            title='My Post',
            description='Description',
            content='Content',
            pub_date=timezone.now(),
            status=Post.Status.ACTIVE
        )
        self.assertEqual(str(post), 'My Post')
        self.assertLessEqual(post.pub_date, timezone.now())

class APITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.author = Author.objects.create(
            username='apiuser',
            first_name='Api',
            last_name='User',
            email='apiuser@gmail.com',
            biography='Bio',
            experience=2
        )
        self.category = Category.objects.create(name='Science', slug='science')
        self.tag = Tag.objects.create(name='api-tag')
        self.post = Post.objects.create(
            author=self.author,
            category=self.category,
            title='API Post',
            description='API description',
            content='API content',
            pub_date=timezone.now(),
            status=Post.Status.ACTIVE
        )
        self.post.tags.add(self.tag)

    def test_post_list(self):
        url = reverse('posts-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('API Post', str(response.data))

    def test_post_detail(self):
        url = reverse('posts-detail', kwargs={'pk': self.post.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'API Post')