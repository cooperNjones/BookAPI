from django.db import models

# Create your models here.


class BookData(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=250)
    image = models.ImageField( upload_to='images', default='images/none/noimg.jpg')
    genre = models.CharField(max_length=50)
    rating = models.CharField(max_length=10)
    description = models.CharField(max_length=300, default='description')
