from django.db import models

class Post(models.Model):
    post_slug = models.SlugField(max_length=60)
    post_title = models.CharField(max_length=60)
    post_body = models.TextField()
    def __str__(self):
        return self.post_title