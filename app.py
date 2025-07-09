from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import os
from datetime import datetime

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this'

DATABASE = 'justfix.db'

def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # Users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Complaints table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS complaints (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            service_type TEXT NOT NULL,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            phone TEXT NOT NULL,
            address TEXT NOT NULL,
            status TEXT DEFAULT 'pending',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')

    conn.commit()
    conn.close()

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('SELECT id, username, password_hash FROM users WHERE username = ?', (username,))
        user = cursor.fetchone()
        conn.close()

        if user and check_password_hash(user[2], password):
            session['user_id'] = user[0]
            session['username'] = user[1]
            flash('Login successful!', 'success')
            return redirect(url_for('homepage'))
        else:
            flash('Invalid username or password!', 'error')

    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            flash('Passwords do not match!', 'error')
            return render_template('signup.html')

        password_hash = generate_password_hash(password)

        try:
            conn = sqlite3.connect(DATABASE)
            cursor = conn.cursor()
            cursor.execute('INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)',
                         (username, email, password_hash))
            conn.commit()
            conn.close()
            flash('Account created successfully! Please login.', 'success')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('Username or email already exists!', 'error')

    return render_template('signup.html')

@app.route('/complaint', methods=['GET', 'POST'])
def complaint():
    if 'user_id' not in session:
        flash('Please login to submit a complaint.', 'error')
        return redirect(url_for('login'))

    if request.method == 'POST':
        service_type = request.form['service_type']
        title = request.form['title']
        description = request.form['description']
        phone = request.form['phone']
        address = request.form['address']

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO complaints
                         (user_id, service_type, title, description, phone, address)
                         VALUES (?, ?, ?, ?, ?, ?)''',
                      (session['user_id'], service_type, title, description, phone, address))
        conn.commit()
        conn.close()

        flash('Complaint submitted successfully! We will contact you soon.', 'success')
        return redirect(url_for('homepage'))

    return render_template('complaint.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('homepage'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0', port=5000)
