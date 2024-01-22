#  не сделана
# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

def read_file_to_dict(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    headers = ['Фамилия', 'Имя', 'Номер телефона']
    contact_list = []
    for line in lines:
        line = line.strip().split()
        contact_list.append(dict(zip(headers, line)))
    return contact_list

def print_contacts(contact_list: list):
    for contact in contact_list:
        for key, value in contact.items():
            print(f'{key}: {value:12}', end='')
        print()

def show_phonebook(file_name):
    list_of_contacts = sorted(read_file_to_dict(file_name), key=lambda x: x['Фамилия'])
    print_contacts(list_of_contacts)
    print()
    return list_of_contacts

def read_file_to_dict(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    headers = ['Фамилия', 'Имя', 'Номер телефона']
    contact_list = []
    for line in lines:
        line = line.strip().split()
        contact_list.append(dict(zip(headers, line)))
    return contact_list


def write_txt(filename , phone_book):
    with open('phonebook.txt','w', encoding = 'utf-8') as phout:
        for i in range(len(phone_book)):
            s=''
            for v in phone_book[i].values():
                s+=v+','
            phout.write(f'{s[:-1]}\n')


def read_txt(filename):
    phone_book=[]
    fields=['Фамилия', 'Имя','Телефон','Описание']

    with open(filename,'r', encoding ='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.split(',')))
            dict(((фамилия,Иванов),(имя,Точка),(номер,8928)))
        phone_book.append(record)
    return phone_book

def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник в текстовом формате\n"
          "5. Изменить данные абонента\n"
          "6. Сохранить справочник в текстовом формате\n"
          "7. Закончить работу"  )

    choice = int(input())
    return choice

def work_with_phonebook():
    choice = show_menu()
   # phone_book= read_txt('Phonebook.txt') 
    phone_book= 'Phonebook.txt' 
    while True:
        if choice ==1:
           # print_result(phone_book)
            show_phonebook(phone_book)
        elif choice ==2:
            last_name = input('lastname ')
            print(fild_by_lastname(phone_book,last_name))
        elif choice ==3:
            last_name = input('lastname ')
            new_number=input('new number')
            print(change_number(phone_book,last_name,new_number))    
        elif choice ==4:
            last_name = input('lastname ')
            print(delete_by_lastname(phone_book,last_name))  
        elif choice ==5:
            number = input('number ')
            print(fild_by_lastname(phone_book,number))  
        elif choice ==6:
           user_data = input('new data ')
           add_user(phone_book,user_data)
           write_txt('phonebook.txt', phone_book)  
        elif choice ==7:
            print('До свидания!')   
            break
        else:
            print('Неправильно выбрана команда!')
            break
        choice = show_menu() 

work_with_phonebook()

