import sqlite3

connection = sqlite3.connect('not_telegram.bd')
cursor = connection.cursor()

cursor.execute('SELECT COUNT(*) FROM Users')
total_users = cursor.fetchone()[0]

cursor.execute('SELECT SUM(balance) FROM Users')
all_balances = cursor.fetchone()[0]

if total_users > 0:
    print(all_balances / total_users)
else:
    print('Нет пользователей в базе данных.')

connection.close()