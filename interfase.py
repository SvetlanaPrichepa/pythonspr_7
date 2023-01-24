import check



def start():
    greetings = 'Это телефонная книга(уж какая удалась))'

    print(f'{greetings}\n')

def menu():
    what_to_do = 'Выберите ту цифру в меню, что планируете делать:'
    new_book = '0. Создать новую книгу'
    new_contact = '1. Добавить новый контакт'
    change_number = '2. Изменить номер телефона'
    change_surname = '3. Изменить фамилию'
    delete_contact = '4. Удалить контакт'
    view_all_contact = '5. Показать все контакты'
    to_exit = '6. Выход'
    print(f'{what_to_do}\n\n{new_book}\n{new_contact}\n{change_number}\n{change_surname}\n{delete_contact}\n{view_all_contact}\n{to_exit}')
    return check.digit_check()


