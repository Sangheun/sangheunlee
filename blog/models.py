from django.db import models
from django.core.urlresolvers import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    photo = models.ImageField()

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.pk])

class Comment(models.Model):
    post = models.ForeignKey(Post)
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.title
