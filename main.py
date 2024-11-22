from models import Library


def main():
    library = Library()
    print(
        '\nВведите номер команды для ее выполнения:\n',
        '\n1 - Добавить книгу\n'
        '2 - Удалить книгу\n'
        '3 - Найти книги\n'
        '4 - Список всех книг\n'
        '5 - Изменить статус книги\n'
        '6 - Выход\n'
    )

    num = input('Номер: ')

    if num == '1':
        title = input('Название книги: ')
        author = input('Автор книги: ')
        year = int(input('Год издания : '))
        library.add_book(title, author, int(year))

    elif num == '2':
        book_id = int(input('Введите id книги: '))
        library.delete_book(book_id)

    elif num == '3':
        param = input(
            'Для поиска по названию введите - title\n'
            'Для поиска по автору введите - author\n'
            'Для поиска по году введите - year\n'
        ).strip()
        if param in ['title', 'author', 'year']:
            value = input('Введите значение: \n')
            library.search_book(param, value)
        else:
            print('Неккоретное поле для поиска')

    elif num == '4':
        library.books_list()

    elif num == '5':
        book_id = int(input('Введите id книги: '))
        status = input(
            'Введите новый статус книги:\n'
            'в наличии\n'
            'выдана\n'
        ).lower().strip()
        library.status_update(book_id, status)

    elif num == '6':
        print('Завершить работу')

    else:
        print('Неккоректный номер программы')


if __name__ == '__main__':
    main()
