from django.db import models

# Create your models here.

class ImageModel(models.Model):
	imageName = models.CharField(max_length = 50)
	imageFile = models.FileField(upload_to = "img/")
	changeImageFile = models.ImageField(upload_to = 'changeImg/', default = '')

	def __str__(self):
		return self.imageName