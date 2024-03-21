from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	title = models.CharField(max_length=200)
	text = models.TextField()

	def __str__(self):
		return self.title
