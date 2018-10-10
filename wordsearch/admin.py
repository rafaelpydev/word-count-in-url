from django.contrib import admin
from .models import WordCount, Url

admin.site.register(Url)
admin.site.register(WordCount)
