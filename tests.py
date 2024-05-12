import pytest
import data
from main import BooksCollector


class TestBooksCollector:
    #проверка, что книга добавлена и у нее нет жанра
    def test_add_new_book_and_get_book_genre(self, collector):
        collector.add_new_book('Мариночка и приключения')
        assert len(collector.get_book_genre('Мариночка и приключения')) == 0

    #проверка, что книга не будет добавлена если такая книга уже есть и можно получить словарь books_genre
    def test_add_new_book_and_get_books_genre_notadd_book_exist(self, collector):
        collector.add_new_book('Мариночка и приключения')
        collector.add_new_book('Мариночка и приключения')
        assert len(collector.get_books_genre()) == 1

    #книга будет добавлена если имя от 1 до 40 символов
    @pytest.mark.parametrize('name', ['М', 'Ма', 'Марина', 'Мариночка и приключения только сегодня!', 'Мариночка и приключения только сегодня!!'])
    def test_add_new_book_add_less_41_symbol(self, collector, name):
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 1

    #книга не будет добавлена если имя 0 или более 40 символов
    @pytest.mark.parametrize('name', ['', 'МариночкаБ и приключения только сегодня!!!', 'МариночкаБ и приключения только сегодня здесь!!!', 'Мариночка и приключения только сегодня!!!'])
    def test_add_new_book_notadd_more_40_symbol(self, collector, name):
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 0

    # книге присваивается жанр
    def test_set_book_genre_assigned_genre(self, collector, add_one_book):
        collector.set_book_genre(data.one_book_name, collector.genre[0])
        assert collector.books_genre[data.one_book_name] == collector.genre[0]

    #можно получить список книг с определенным жанром
    #используем полный набор данных, чтобы удостовериться, что в выборку попадет только одна книга определенного жанра
    def test_get_books_with_specific_genre_received_genre(self, collector, names_and_genre):
        assert len(collector.get_books_with_specific_genre(collector.genre[0])) == 1

    #возращаем книги подходящие детям
    #используем полный набор данных, чтобы убедиться, что в выборку попадают книги для детей
    def test_get_books_for_children_fits(self, collector, names_and_genre):
        assert len(collector.get_books_for_children()) == 3

    #добавляем книги в избранное и получаем список избранных книг
    def test_add_book_in_favorites_and_get_list_of_favorites_books_add_favorites_book(self, collector, add_one_book):
        collector.add_book_in_favorites(data.one_book_name)
        assert collector.get_list_of_favorites_books() == collector.favorites

    #повторно добавить книгу в избранное нельзя
    def test_add_book_in_favorites_notadd_favorites(self, collector, add_one_book):
        collector.add_book_in_favorites(data.one_book_name)
        collector.add_book_in_favorites(data.one_book_name)
        assert len(collector.get_list_of_favorites_books()) == 1

    #удаляем книги из избранного
    def test_delete_book_from_favorites_delete(self, collector, add_one_book):
        collector.add_book_in_favorites(data.one_book_name)
        collector.delete_book_from_favorites(data.one_book_name)
        assert collector.get_list_of_favorites_books() == []





