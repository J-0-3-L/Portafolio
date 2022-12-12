from django.db import models
from django.db.models.fields import CharField , URLField
from django.db.models.fields.files import ImageField

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    foto = models.ImageField(upload_to="images",null=True)
    tag = models.CharField(max_length=100)
    url_git = models.URLField(null=True,blank=True)


    def __str__(self):
        return self.title
        