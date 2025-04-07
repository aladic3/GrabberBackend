from django.db import models
from markdownx.models import MarkdownxField

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)  # заголовок поста
    content = MarkdownxField()           # тело поста
    created_at = models.DateTimeField(auto_now_add=True)  # дата создания

    def __str__(self):
        return self.title
