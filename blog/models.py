from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField(max_length=256)
    content = RichTextField(config_name='default')
    image = models.ImageField(upload_to='uploads')
    published_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ('-published_date',)

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.pk])

    def __str__(self):
        return self.title
