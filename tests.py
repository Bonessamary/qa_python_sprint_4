import pytest
from main import BooksCollector


class TestBooksCollector:
    #проверка, что книга добавлена и у нее нет жанра
    def test_add_new_book_and_get_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Мариночка и приключения')
        assert len(collector.get_book_genre('Мариночка и приключения')) == 0

    #проверка, что книга не будет добавлена если такая книга уже есть и можно получить словарь books_genre
    def test_add_new_book_and_get_books_genre_notadd_book_exist(self):
        collector = BooksCollector()
        collector.add_new_book('Мариночка и приключения')
        collector.add_new_book('Мариночка и приключения')
        assert len(collector.get_books_genre()) == 1

    #книга будет добавлена если имя от 1 до 40 символов
    @pytest.mark.parametrize('name', ['М', 'Ма', 'Марина', 'Мариночка и приключения только сегодня!', 'Мариночка и приключения только сегодня!!'])
    def test_add_new_book_add_less_41_symbol(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 1

    #книга не будет добавлена если имя 0 или более 40 символов
    @pytest.mark.parametrize('name', ['', 'МариночкаБ и приключения только сегодня!!!', 'МариночкаБ и приключения только сегодня здесь!!!', 'Мариночка и приключения только сегодня!!!'])
    def test_add_new_book_notadd_more_40_symbol(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 0

    # книге присваивается жанр
    def test_set_book_genre_assigned_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Мариночка и приключения')
        collector.set_book_genre('Мариночка и приключения', 'Ужасы')
        assert (collector.get_books_genre())['Мариночка и приключения'] == 'Ужасы'

    #можно получить список книг с определенным жанром
    def test_get_books_with_specific_genre_received_genre(self, names_and_genre):
        assert names_and_genre.get_books_with_specific_genre('Ужасы') == ['Ужасные приключения']

    #возращаем книги подходящие детям
    def test_get_books_for_children_fits(self, names_and_genre):
        assert names_and_genre.get_books_for_children() == ['Фантастические приключения', 'Детские приключения','Веселые приключения']

    #добавляем книги в избранное и получаем список избранных книг
    def test_add_book_in_favorites_and_get_list_of_favorites_books_add_favorites_book(self, names_and_genre):
        names_and_genre.add_book_in_favorites('Ужасные приключения')
        assert names_and_genre.get_list_of_favorites_books() == ['Ужасные приключения']

    #повторно добавить книгу в избранное нельзя
    def test_add_book_in_favorites_notadd_favorites(self, names_and_genre):
        names_and_genre.add_book_in_favorites('Ужасные приключения')
        names_and_genre.add_book_in_favorites('Ужасные приключения')
        assert len(names_and_genre.get_list_of_favorites_books()) == 1

    #удаляем книги из избранного
    def test_delete_book_from_favorites_delete(self, names_and_genre):
        names_and_genre.add_book_in_favorites('Ужасные приключения')
        names_and_genre.delete_book_from_favorites('Ужасные приключения')
        assert names_and_genre.get_list_of_favorites_books() == []







