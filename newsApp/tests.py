from django.test import TestCase
from django.urls import reverse
from .models import Post

# Create your tests here.
class PostModelTest(TestCase):
	def setUp(self):
		Post.objects.create(title='Mavzu', text='Yangilik matni')

	def test_text_context(self):
		post = Post.objects.get(id=1)
		expected_object_title = f'{post.title}'
		expected_object_text = f'{post.text}'
		self.assertEqual(expected_object_title, 'Mavzu')
		self.assertEqual(expected_object_text, 'Yangilik matni')

class HomePageViewTest(TestCase):
	def setUp(self):
		Post.objects.create(title='Boshqa mavzu', text='Boshqa matn')

	def test_views_url_exist_at_proper_location(self):
		resp = self.client.get('/')
		self.assertEqual(resp.status_code, 200)

	def test_views_url_by_name(self):
		resp = self.client.get(reverse('home'))
		self.assertEqual(resp.status_code, 200)

	def test_views_uses_correct_template(self):
		resp = self.client.get(reverse('home'))
		self.assertEqual(resp.status_code, 200)
		self.assertTemplateUsed(resp, 'home.html')
























