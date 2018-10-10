from wordsearch.crawler import word_ocurrence
from tests.factories import UrlsFactory, WordCountFactory
import pytest


class TestCrawler:

    def test_crawler(self):
        zen_of_python = 'https://www.python.org/dev/peps/pep-0020/'
        assert isinstance(word_ocurrence('Better', zen_of_python), int)

    def test_crawler_error(self):
        assert isinstance(
            word_ocurrence('test_error', "www.python.org"), Exception
        )


class TestModels:

    @pytest.mark.django_db
    def test_url(self):
        create_url = UrlsFactory(url="https://www.python.org")
        assert create_url.url == "https://www.python.org"

    @pytest.mark.django_db
    def test_word_count(self):
        url_1 = UrlsFactory(url="https://www.python.org")
        url_2 = UrlsFactory(url="https://www.python.org/dev/peps/pep-0020/")

        word_count = WordCountFactory(
            url_list=[url_1, url_2]
        )

        assert word_count.url_list.count() == 2
