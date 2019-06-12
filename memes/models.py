from django.db import models
from django.contrib.auth.models import User
import datetime

class Meme(models.Model):
	description = models.CharField(max_length=150, default='Moj mem')
	image = models.ImageField(upload_to='', null=False)
	author = models.CharField(max_length=100, default='anon')
	waiting = models.BooleanField(default=True)
	add_date = models.DateTimeField(default=datetime.datetime.now())
	publication_date = models.DateTimeField(default=datetime.datetime(1999, 8, 1), null=True, blank=True)
	likes = models.ManyToManyField(User, related_name="likes", blank=True)
	likes_number = models.IntegerField(default=0)
	dislikes = models.ManyToManyField(User, related_name="dislikes", blank=True)
	dislikes_number = models.IntegerField(default=0)

	def __str__(self):
		return self.description

	def __len__(self):
		# to powinno działać
		return likes.count()

	def likes_count(self):
		return likes.count()
