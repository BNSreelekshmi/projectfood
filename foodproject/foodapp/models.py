from django.db import models

# Create your models here.
class foodtab(models.Model):
    name = models.CharField(max_length=250)
    ingre = models.TextField()
    desc = models.TextField()
    image = models.ImageField(upload_to='photos')

    def __str__(self):
        return self.name