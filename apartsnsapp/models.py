from django.db import models

# Create your models here.
class ApartsnsModel(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.CharField(max_length=50)
    images = models.ImageField(upload_to='',null=True,blank=True)
    good = models.IntegerField(null=True, blank=True, default=0)
    read = models.IntegerField(null=True, blank=True, default=0)
    readtext = models.CharField(max_length=100, null=True, blank=True, default='a')
    def __str__(self):
        return self.title