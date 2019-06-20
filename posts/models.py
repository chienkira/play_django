from django.db import models
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=254, null=False, blank=False)
    content = models.TextField(max_length=254, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.content

    def get_absolute_url(self):
        return reverse('posts:list', kwargs={})
