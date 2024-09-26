"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    import csv


    dicts_list = [
        { 
            "name":"John", "age": 50, "job": "teacher"
        },
        {
            "name":"Luis", "age": 25, "job": "software engineer"
        },
        {
            "name":"Peter", "age": 44, "job": "manager"
        },
        {
            "name":"Jesica", "age": 30, "job": "sales manager"
        }
    ]
    print(dicts_list)
    with open ('export.csv', 'w', encoding='utf-8', newline='') as f:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(f, fields, delimiter=';')
        writer.writeheader()
        for user in dicts_list:
            writer.writerow(user)


if __name__ == "__main__":
    main()
