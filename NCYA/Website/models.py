from django.db import models

# Create your models here.

class User(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	username = models.TextField()
	isAdmin = models.BooleanField(default=False)

	class Meta:
		ordering = ('created', )
