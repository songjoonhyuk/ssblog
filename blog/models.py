from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=100)
	content =models.TextField()
	photo = models.ImageField(blank='True')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

class Comment(models.Model):
	post = models.ForeignKey(Post)
	title = models.CharField(max_length=100)
	content = models.TextField()

	def __str__(self):
		return self.title


