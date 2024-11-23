# import sqlite3

# def init_db():
#     conn = sqlite3.connect('dbquanlysv.db')
#     cursor = conn.cursor()
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS sinhvien (
#             ma INTEGER PRIMARY KEY AUTOINCREMENT,
#             ho TEXT NOT NULL,
#             ten TEXT NOT NULL
#         )
#     ''')
#     conn.commit()
#     conn.close()

# if __name__ == "__main__":
#     init_db()
#     print("Database initialized!")
