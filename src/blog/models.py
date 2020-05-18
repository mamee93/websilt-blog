from django.db import models
 
from django.utils.timezone import datetime
# Create your models here.

class Post(models.Model):

	title   = models.CharField(max_length=50)
	content = models.TextField()
	created = models.DateTimeField(default=datetime.now, blank=True)



	def __str__(self):
		 
		return self.title
