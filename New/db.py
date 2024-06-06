import sqlite3

# conn = sqlite3.connect("account.db")
#
# try:
#     cursor = conn.cursor()

#     Подготовленный запрос для вставки нескольких записей
#     query = "INSERT INTO `users` (`user_id`, `record`) VALUES (?, ?)"
#
#     # Список кортежей значений
#     values = [(1000, 1), (1001, 2), (1002, 3)]
#
#     # Выполнение подготовленного запроса с несколькими значениями
#     cursor.executemany(query, values)
#
#     Подтверждаем изменения
#     conn.commit()
#
#     Изменение записи в таблице
#     up = cursor.execute("UPDATE `users` SET `record` = `record` + (?) WHERE `user_id` = (?)", (1, 2039541981))
#     val = [(5, 1000)]
#
#     cursor.executemany(up, val)
#
# #     conn.commit()
#
#     # Считываем всех пользователей
#     users = cursor.execute("SELECT * FROM `users`")
#     print(users.fetchall())
#
#
#
# except sqlite3.Error as error:
#     print("Error", error)
#
# finally:
#     if conn:
#         conn.close()

class BotDB:

    def __init__(self, db_file):
        # Инициализация соединения с БД
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def user_exists(self, user_id):
        # Проверяем, есть ли пользователь в БД
        result = self.cursor.execute("SELECT `id` FROM `users` WHERE `user_id` = ?", (user_id,))
        return bool(len(result.fetchall()))

    def get_user_id(self, user_id):
        # Получаем id пользователя в базе по его user_id в телеграмме
        result = self.cursor.execute("SELECT `id` FROM `users` WHERE `user_id` = ?", (user_id,))
        return result.fetchone()[0]

    def add_user(self, user_id):
        # Добавление пользователя в БД
        self.cursor.execute("INSERT OR IGNORE INTO `users` (`user_id`, `record`) VALUES(?, ?)", (user_id, 0))
        return self.conn.commit()

    def up_record(self, user_id, record):
        # Обновление данных о рекорде
        self.cursor.execute("UPDATE `users` SET `record` = (?) WHERE `user_id` = (?)", (record, user_id))
        return self.conn.commit()

    def get_record(self, user_id):
        result = self.cursor.execute("SELECT `record` FROM `users` WHERE `user_id` = (?)", (user_id,))
        return result.fetchone()[0]

    def close(self):
        # Закрытие соединения с БД
        self.conn.close()

