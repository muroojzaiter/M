from database import Database
import pymysql
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Define some sample data for demonstration purposes
users = {
    'user1': 'password1',
    'user2': 'password2',
    'user3': 'password3',
    'user4': 'password4',
    'user5': 'password5'
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            # Redirect to a dashboard or profile page after successful login
            return redirect(url_for('dashboard'))
        else:
            # Show error message for invalid credentials
            return render_template('login.html', error=True)
    return render_template('login.html', error=False)

@app.route('/dashboard')
def dashboard():
    # Render the dashboard page
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
