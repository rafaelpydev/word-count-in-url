from bs4 import BeautifulSoup
import requests


def word_ocurrence(word, url):
    try:
        request = requests.get(url)
        soup = BeautifulSoup(request.text, 'html.parser')
        page_text = soup.get_text().lower()
        wordlist = page_text.split()
        return wordlist.count(word.lower())

    except Exception as log:
        print(log)
        return log
