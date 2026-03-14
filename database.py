import sqlite3 

class DB:
    def __init__(self):
        self.conn = sqlite3.connect("users.db")
        self.create_table()
        
    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )
        '''
        )
        try:
            cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', ("nigger", "1234"))
            self.conn.commit()
        except sqlite3.IntegrityError:
            pass

    def get_user(self, username, password):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
        return cursor.fetchone()
    
    def new_user(self, username, password):
        cursor = self.conn.cursor()
        pass
        
if __name__ == "__main__":
    db = DB()