from rest_framework import serializers
from wordsearch.models import WordCount, Url
from wordsearch.crawler import word_ocurrence


class UrlSerializer(serializers.ModelSerializer):
    number_of_words = serializers.SerializerMethodField()

    class Meta:
        model = Url
        fields = ('url', 'number_of_words')

    def get_number_of_words(self, obj):
        select_url = Url.objects.get(pk=obj.pk)
        word = select_url.wordcount_set.values()[0]['word']
        return word_ocurrence(word, obj.url)


class WordCountSerializer(serializers.ModelSerializer):
    url_list = UrlSerializer(many=True)

    class Meta:
        model = WordCount
        fields = ('id', 'word', 'url_list')

    def add_urls(self, urls, new_wordcount):
        for url in urls:
            new_url = Url.objects.create(**url)
            new_wordcount.url_list.add(new_url)

    def create(self, validated_data):
        url_list = validated_data['url_list']
        del validated_data['url_list']

        new_wordcount = WordCount.objects.create(**validated_data)
        self.add_urls(url_list, new_wordcount)

        new_wordcount.save()

        return new_wordcount
