import sqlite3

def init_db():
    conn = sqlite3.connect('favorites.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reminders (
            user_id INTEGER,
            anime_name TEXT,
            remind_time TEXT,
            PRIMARY KEY (user_id, anime_name, remind_time)
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            last_interaction TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS favorites (
            user_id INTEGER,
            anime_name TEXT,
            PRIMARY KEY (user_id, anime_name)
        )
    ''')
    conn.commit()
    conn.close()

def init_welcome_db():
    try:
        conn = sqlite3.connect('welcome.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS welcome_status (
                user_id INTEGER PRIMARY KEY,
                last_welcome_date TEXT
            )
        ''')
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")

# Add other database helper functions here
