from data_create import name_data, surname_data, phone_data, address_data


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате записать данные? \n \n"
    f"1 Вариант: \n"
    f"{name}\n{surname}\n{phone}\n{address}\n\n"
    f"2 Вариант: \n"
    f"{name};{surname};{phone};{address}\n"
    f"Выберите вариант: "))
    while var != 1 and var != 2:
        print("Неправильный ввод")
        var = int(input("Введите число "))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")

    if var == 2:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name};{surname};{phone};{address}\n\n")




def print_data():
    print('Вывожу данные из файла data_first_variant: \n')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first)-1:
                data_first_list.append(''.join(data_first[j:i+1]))
                j = i
        print(''.join(data_first_list))

    print('Вывожу данные из файла data_second_variant: \n')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
        data_second = f.readlines()
        print(*data_second)


def change_data():
    print('Выберите файл для внесения изменений: \n 1 - data_first_variant \n 2 - data_second_variant')
    choice = int(input("Введите число "))
    while choice != 1 and choice != 2:
        print("Неправильный ввод")
        choice = int(input("Введите число "))

    if choice == 1:
        num = int(input("Введите номер записи, которую хотите изменить "))
        with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
            data_first = f.readlines()
            data_first_new_list = []
            count = 1
            j = 0               
            for i in range(len(data_first)):
                if data_first[i] == '\n' or i == len(data_first)-1:
                    if count != num:
                        data_first_new_list.append(''.join(data_first[j:i+1]))
                    else:
                        temp = []
                        temp.append(name_data())
                        temp.append(surname_data())
                        temp.append(phone_data())
                        temp.append(address_data())
                        data_first_new_list.append('\n'.join(temp))
                    j = i
                    count += 1
            if num > len(data_first_new_list):
                print('Записи с таким номером не существует, повторите попытку')
            else:
                with open('data_first_variant.csv', 'w', encoding='utf-8') as f:
                    f.write('')
                for i in range(len(data_first_new_list)):
                    with open('data_first_variant.csv', 'a', encoding='utf-8') as f:
                        new_list = data_first_new_list[i].split('\n')
                        for k in range(len(new_list)):
                            if new_list[k] != '':
                                f.write(f"{new_list[k]}\n")
                        f.write('\n')

    if choice == 2: 
        num = int(input("Введите номер записи, которую хотите изменить "))
        with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
            data_second = f.readlines()
            data_second_new_list = []
            count = 1
            j = 0
            for i in range(len(data_second)):
                if data_second[i] == '\n' or i == len(data_second)-1:
                    if count != num:
                        data_second_new_list.append(''.join(data_second[j:i+1]))
                    else:
                        temp = []
                        temp.append(name_data())
                        temp.append(surname_data())
                        temp.append(phone_data())
                        temp.append(address_data())
                        data_second_new_list.append(';'.join(temp))
                    j = i
                    count += 1
            if num > len(data_second_new_list):
                print('Записи с таким номером не существует, повторите попытку')
            else:
                with open('data_second_variant.csv', 'w', encoding='utf-8') as f:
                    f.write('')
                for i in range(len(data_second_new_list)):
                    with open('data_second_variant.csv', 'a', encoding='utf-8') as f:

                        new_list = data_second_new_list[i].split('\n')
                        for k in range(len(new_list)):
                            if new_list[k] != '':
                                f.write(f"{new_list[k]}\n")
                        f.write('\n')
        




def delete_data():
    print('Выберите файл для внесения изменений: \n 1 - data_first_variant \n 2 - data_second_variant')
    choice = int(input("Введите число "))
    while choice != 1 and choice != 2:
        print("Неправильный ввод")
        choice = int(input("Введите число "))
    
    if choice == 1:
        num = int(input("Введите номер записи, которую хотите удалить "))
        with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
            data_first = f.readlines()
            data_first_new_list = []
            count = 1
            j = 0
            for i in range(len(data_first)):
                if data_first[i] == '\n' or i == len(data_first)-1:
                    if count != num:
                        data_first_new_list.append(''.join(data_first[j:i+1]))
                    j = i
                    count += 1
            if num > len(data_first_new_list)+1:
               print('Записи с таким номером не существует, повторите попытку')
            else:
                with open('data_first_variant.csv', 'w', encoding='utf-8') as f:
                    f.write('')
                for i in range(len(data_first_new_list)):
                    with open('data_first_variant.csv', 'a', encoding='utf-8') as f:
                        new_list = data_first_new_list[i].split('\n')
                        for k in range(len(new_list)):
                            if new_list[k] != '':
                                f.write(f"{new_list[k]}\n")
                        f.write('\n')

    if choice == 2:
        num = int(input("Введите номер записи, которую хотите удалить "))
        with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
            data_second = f.readlines()
            data_second_new_list = []
            count = 1
            j = 0
            for i in range(len(data_second)):
                if data_second[i] == '\n' or i == len(data_second)-1:
                    if count != num:
                        data_second_new_list.append(''.join(data_second[j:i+1]))
                    j = i
                    count += 1
            if num > len(data_second_new_list)+1:
                print('Записи с таким номером не существует, повторите попытку')
            else:
                with open('data_second_variant.csv', 'w', encoding='utf-8') as f:
                    f.write('')
                for i in range(len(data_second_new_list)):
                    with open('data_second_variant.csv', 'a', encoding='utf-8') as f:
                        new_list = data_second_new_list[i].split('\n')
                        for k in range(len(new_list)):
                            if new_list[k] != '':
                                f.write(f"{new_list[k]}\n")
                        f.write('\n')
