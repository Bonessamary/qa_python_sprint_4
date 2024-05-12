import pytest
import data
from main import BooksCollector

#Возвращает экземпляр класса BooksCollector
@pytest.fixture()
def collector():
    collector = BooksCollector()
    return collector

#Создание одной книги для использования в классе
@pytest.fixture
def add_one_book(collector):
    collector.books_genre[data.one_book_name] = ''

#Создание списка книг с жанрами для использования в классе
@pytest.fixture
def names_and_genre(collector):
    collector.books_genre = data.book_names