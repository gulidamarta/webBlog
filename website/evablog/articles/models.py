from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)

    thumb = models.ImageField(default='default.png', blank=True)
    category = models.ForeignKey('Category', null=True, on_delete=True, blank=True)
    # TODO: add in author later

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:100] + "..."
