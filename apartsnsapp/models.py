from django.db import models
from django.utils import timezone

# Create your models here.
class ApartsnsModel(models.Model):
    """listの投稿"""
    name = models.CharField( max_length=50,default="")
    title = models.CharField(max_length=50)
    content = models.TextField()
    def __str__(self):
        return self.title

class CommentModel(models.Model):
    """listへのコメント"""
    name = models.CharField('投稿者' , max_length=50)
    text = models.TextField('本文')
    post = models.ForeignKey(ApartsnsModel, verbose_name='コメント', on_delete=models.PROTECT)
    created_at = models.DateTimeField('作成日', default=timezone.now)
    def __str__(self):
        return self.text[:10]
