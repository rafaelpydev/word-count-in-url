from rest_framework import viewsets
from wordsearch.models import WordCount
from .serializers import WordCountSerializer


class WordCountViewSet(viewsets.ModelViewSet):
    queryset = WordCount.objects.all()
    serializer_class = WordCountSerializer
