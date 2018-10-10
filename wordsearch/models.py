from django.db import models


class Url(models.Model):
    url = models.URLField()

    def __str__(self):
        return self.url


class WordCount(models.Model):
    word = models.CharField(max_length=20)
    url_list = models.ManyToManyField(Url)

    def __str__(self):
        return self.word
