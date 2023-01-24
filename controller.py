import add_contakt as ac
import interfase as ui
import phone_num as cpn
import surname as cs
import kontakt_delete as dc
import view as vac
# import export_in_file as eif


def user_choice():

    choice_num = ui.menu()
    if choice_num < 0 or choice_num > 7:
        print('\nОшибка ввода!\n\nЧисло должно соответствовать пункту меню!\n')
        user_choice()
    elif choice_num == 0:
        ac.create_json()
    elif choice_num == 1:
        ac.add_to_json()
    elif choice_num == 2:
        cpn.phone_num()
    elif choice_num == 3:
        cs.change_surname()
    elif choice_num == 4:
        dc.delete_contact()
    elif choice_num == 5:
        vac.view_all_contacts()
    # elif choice_num == 6:
    #     eif.export_txt()
    elif choice_num == 6:
        print('\nСпасибо что пользовались нашим приложением!\n\nДо новых встреч!')
        exit()