import sqlite3

connection = sqlite3.connect('db_for_hmw.db')
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Products(
id INTEGER PRIMARY KEY,
title TEXT NOT NULL,
description TEXT,
price INTEGER NOT NULL
);
''')


def adder():
    for i in range(1, 5):
        cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
                       (f'Продукт {i}',
                        f'Описание {i}', f'{i * 100}'))


# adder()


def deleter():
    for to_del in range(1, 5):
        cursor.execute('DELETE FROM Products WHERE title = ?', (f'Продукт {to_del}',))


# deleter()


def get_all_products():
    cursor.execute('SELECT * FROM Products')
    users = cursor.fetchall()
    return users


print(len(get_all_products()))
for prod in get_all_products():
    print(prod)

# connection.commit()
# connection.close()
