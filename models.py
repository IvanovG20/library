import json


class Book():
    """Модель книги"""

    def __init__(
            self, id: int,
            title: str,
            author: str,
            year: int,
            status: str = 'в наличии'
            ):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status


class Library():
    """Класс для управления библиотекой"""

    def __init__(self, database: str = 'library_data.json'):
        self.database = database
        self.books: list[Book] = self.load_books()

    def load_books(self):
        """Загружает книги из файла с данными"""
        try:
            with open(self.database, encoding='utf-8') as data_file:
                data = json.load(data_file)
                return [
                    Book(
                        book['id'],
                        book['title'],
                        book['author'],
                        book['year'],
                        book['status'],
                    ) for book in data
                ]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_books(self):
        """Загружает книги в файл с данными"""
        with open(self.database, 'w', encoding='utf-8') as data_file:
            json.dump(
                [book.__dict__ for book in self.books],
                data_file,
                ensure_ascii=False
            )

    def add_book(self, title: str, author: str, year: int):
        """Добавляет книгу в библиотеку"""
        book_id = len(self.books)
        new_book = Book(book_id, title, author, year)
        self.books.append(new_book,)
        self.save_books()
        print(f'Книга {title} добавлена в библиотеку. Её id - {book_id}')

    def delete_book(self, book_id: int):
        """Удалить книгу из библиотеки"""
        try:
            book = self.books[book_id]
        except IndexError:
            print(f'Книга с id {book_id} не найдена')
        else:
            self.books.remove(book)
            self.save_books()
            print(f'Книга с id {book_id} удалена')

    def books_list(self, books: list[Book] = None):
        """Выводит список книг"""
        if books is None:
            books = self.books
        if books:
            for book in books:
                print(
                    f'\nid: {book.id}\n'
                    f'Название: {book.title}\n'
                    f'Автор: {book.author}\n'
                    f'Год: {book.year}\n'
                    f'Статус: {book.status}\n'
                )
        else:
            print('В библиотеке нет книг')

    def search_book(self, param: str, key: str):
        """Поиск книги в библиотеки"""
        books_list = [
            book for book in self.books if key == str(book.__dict__.get(param))
        ]
        if books_list:
            self.books_list(books_list)

    def status_update(self, book_id: int, status: str):
        """Обновляет статус книги"""
        try:
            book = self.books[book_id]
        except IndexError:
            print(f'Книга с id {book_id} не найдена')
        else:
            if status in ['в наличии', 'выдана']:
                if book.status == status:
                    return print('У книги уже такой статус')
                book.status = status
                self.save_books()
                print(f'Статус книги с id {book_id} обновлён на {status}')
            else:
                print('Неверный статус')
