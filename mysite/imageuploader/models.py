from django.db import models

# Create your models here.


class ImageUpload(models.Model):
    url = models.FileField(upload_to='images/')
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)

    # def __str__(self):
    #     return self.name