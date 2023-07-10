from data_create import input_user_data


def input_data():
    name, surname, phone, address = input_user_data()

    var = int(input(f'\nВ каком виде записать данные? \n'
                    f'1 вариант: \n'
                    f'{name} \n'
                    f'{surname} \n'
                    f'{phone} \n'
                    f'{address} \n\n'
                    f'2 вариант: \n'
                    f'{name};{surname};{phone};{address} \n\n'
                    f'Ваш выбор: '))
    
    while var < 1 or var > 2:
        var = int(input('Ошибка! Попробуйте еще раз! Ваш выбор: '))
    
    if var == 1:
        with open('data_first_variant.csv', "r", encoding= 'utf-8') as data:
            tel_file = data.read()
            num = len(tel_file.split('\n\n'))
        with open('data_first_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{num} \n'
                       f'{name} \n'
                       f'{surname} \n'
                       f'{phone} \n'
                       f'{address} \n\n')
    else:
        with open('data_second_variant.csv', "r", encoding= 'utf-8') as data:
            tel_file = data.read()
            num = len(tel_file.split('\n\n'))
        with open('data_second_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{num} | {name};{surname};{phone};{address} \n\n')

    print(f'Данные добавлены в {var} файл')
    



def print_data():
    
    show = int(input(f'\nВ каком виде вывести данные? \n'
                    f'1 вариант: \n'
                    f'Имя \n'
                    f'Фамилия \n'
                    f'Телефон \n'
                    f'Адрес \n\n'
                    f'2 вариант: \n'
                    f'Имя;Фамилия;Телефон;Адрес \n\n'
                    f'Ваш выбор: '))
    
    while show < 1 or show > 2:
        show = int(input('Ошибка! Попробуйте еще раз! Ваш выбор: '))

    if show == 1:
        print('1 файл: ')
        with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
            data = file.readlines()
            data_list = list()
            j = 0 # идем с начала списка
            for i in range(len(data)):
                if data[i] == '\n':
                    data_list.append(''.join(data[j:i]))
                    j = i
            print(''.join(data_list))
    else:
        print('2 файл: ')
        with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
            data = list(file.readlines())
            print(''.join(data))





def delete_data():
    print("\n№ | Имя;Фамилия;Телефон;Адрес")

    show = int(input(f'\nВ каком файле удалить данные? \n'
                    f'1 вариант: \n'
                    f'Имя \n'
                    f'Фамилия \n'
                    f'Телефон \n'
                    f'Адрес \n\n'
                    f'2 вариант: \n'
                    f'Имя;Фамилия;Телефон;Адрес \n\n'
                    f'Ваш выбор: '))
    
    while show < 1 or show > 2:
        show = int(input('Ошибка! Попробуйте еще раз! Ваш выбор: '))
    
    if show == 1:
        print('1 файл: ')
        with open('data_first_variant.csv', "r", encoding='utf-8') as data:
            tel_book = data.read()
            print(tel_book)
            print("")
            index_delete_data = int(input("Введите номер строки для удаления: ")) - 1
            tel_book_lines = tel_book.split("\n\n")
            del_tel_book_lines = tel_book_lines[index_delete_data]
            tel_book_lines.pop(index_delete_data)
            print(f"Удалена запись: {del_tel_book_lines}\n")
        with open('data_first_variant.csv', "w", encoding='utf-8') as data:
            data.write('\n\n'.join(tel_book_lines))
            print("")
    else:
        print('2 файл: ')
        with open('data_second_variant.csv', "r", encoding='utf-8') as data:
            tel_book = data.read()
            print(tel_book)
            print("")
            index_delete_data = int(input("Введите номер строки для удаления: ")) - 1
            tel_book_lines = tel_book.split("\n\n")
            del_tel_book_lines = tel_book_lines[index_delete_data]
            tel_book_lines.pop(index_delete_data)
            print(f"Удалена запись: {del_tel_book_lines}\n")
        with open('data_second_variant.csv', "w", encoding='utf-8') as data:
            data.write('\n\n'.join(tel_book_lines))
            print("")
    
