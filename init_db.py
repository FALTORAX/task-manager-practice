import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('app.db')

# Создание курсора
cursor = conn.cursor()

# Создание таблицы
cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        status TEXT DEFAULT 'new'
    )
""")

# Сохранение изменений
conn.commit()

# Закрытие подключения
conn.close()

print("База данных и таблица tasks успешно созданы.")