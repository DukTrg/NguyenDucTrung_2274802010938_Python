import sqlite3

class Database:
    def __init__(self, db_name="dbquanlysv.db"):
        self.db_name = db_name
        self.connect()
        self.create_table()

    def connect(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cur = self.conn.cursor()

    def create_table(self):
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS sinhvien (
                ma INTEGER PRIMARY KEY,
                ho TEXT NOT NULL,
                ten TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def insert(self, ma, ho, ten):
        self.cur.execute("INSERT INTO sinhvien (ma, ho, ten) VALUES (?, ?, ?)", (ma, ho, ten))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM sinhvien")
        return self.cur.fetchall()

    def delete(self, ma):
        self.cur.execute("DELETE FROM sinhvien WHERE ma = ?", (ma,))
        self.conn.commit()

    def update(self, ma, ho, ten):
        self.cur.execute("UPDATE sinhvien SET ho = ?, ten = ? WHERE ma = ?", (ho, ten, ma))
        self.conn.commit()

    def close(self):
        self.conn.close()

# # Usage:
# db = Database()
# db.insert(1, "Nguyen", "An")
# print(db.view())
