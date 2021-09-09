from django.test import TestCase
from django.urls import reverse

from .models import Posts

# Create your tests here.
class PostsModelTest(TestCase):

    def setUp(self):
        Posts.objects.create(text='this is test')

    def test_text_content(self):
        post = Posts.objects.get(id=1 )
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name,'this is test')

class HomePages(TestCase):

    def setUp(self):
        Posts.objects.create(text='this is another test')
    
    def test_view_urls_exit_at_correct_location(self):
        res = self.client.get('/')
        self.assertEqual(res.status_code, 200)
    
    def test_view_urls_by_name(self):
        res = self.client.get(reverse('home'))
        self.assertEqual(res.status_code, 200)
        
    def test_view_urls_use_correct_templates(self):
        res = self.client.get(reverse('home'))
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'home.html')
