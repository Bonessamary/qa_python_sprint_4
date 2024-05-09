import pytest
from main import BooksCollector

@pytest.fixture
def names_and_genre():
    collector = BooksCollector()
    books = [
        'Фантастические приключения',
        'Ужасные приключения',
        'Детективные приключения',
        'Детские приключения',
        'Веселые приключения'
    ]
    genres = [
        'Фантастика',
        'Ужасы',
        'Детективы',
        'Мультфильмы',
        'Комедии'
    ]
    for i in range(0, len(books)):
        collector.books_genre[books[i]] = genres[i]
    return collector