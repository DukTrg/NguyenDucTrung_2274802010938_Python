from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'f%#y8HBSGHSEBGBG42 '

# Configurations
DB_NAME = 'dbquanlysv.db'

# Login route
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == '123':
            session['logged_in'] = True
            return redirect(url_for('index'))
        return render_template('login.html', error='Invalid credentials')
    return render_template('login.html')

# Logout route
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

# Index route
@app.route('/index')
def index():
    if 'logged_in' not in session:
        return redirect(url_for('login'))
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sinhvien")
    students = cursor.fetchall()
    conn.close()
    return render_template('index.html', students=students)

# Add student route
@app.route('/add', methods=['GET', 'POST'])
def add():
    if 'logged_in' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        ho = request.form['ho']
        ten = request.form['ten']
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO sinhvien (ho, ten) VALUES (?, ?)", (ho, ten))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add.html')

# Edit student route
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    if 'logged_in' not in session:
        return redirect(url_for('login'))
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    if request.method == 'POST':
        ho = request.form['ho']
        ten = request.form['ten']
        cursor.execute("UPDATE sinhvien SET ho = ?, ten = ? WHERE ma = ?", (ho, ten, id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    cursor.execute("SELECT * FROM sinhvien WHERE ma = ?", (id,))
    student = cursor.fetchone()
    conn.close()
    return render_template('edit.html', student=student)

# Delete student route
@app.route('/delete/<int:id>')
def delete(id):
    if 'logged_in' not in session:
        return redirect(url_for('login'))
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM sinhvien WHERE ma = ?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True , port= 8080)
