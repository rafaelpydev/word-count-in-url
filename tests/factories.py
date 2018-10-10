from wordsearch.models import Url, WordCount
import factory


class UrlsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Url
        django_get_or_create = ('url',)


class WordCountFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = WordCount

    word = factory.Sequence(lambda n: 'word_{}'.format(n))

    @factory.post_generation
    def url_list(self, create, extracted):
        if not create:
            return

        if extracted:
            for i in extracted:
                self.url_list.add(i)
