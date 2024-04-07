from django.db import models
from ckeditor.fields import RichTextField

class Article(models.Model):
    title = models.CharField(max_length=255)
    snippet = models.CharField(max_length=1000, null=True)
    text = RichTextField()
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title