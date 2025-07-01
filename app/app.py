from flask import Flask, render_template, request, redirect, url_for, session
import secrets
import firebase_admin
from firebase_admin import credentials, db
import re
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# Initialize Firebase Admin SDK
cred = credentials.Certificate('app/remembermeapp-84b23-firebase-adminsdk-fbsvc-f623890f7a.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://remembermeapp-84b23-default-rtdb.europe-west1.firebasedatabase.app/'
})

# -- Home Route --
@app.route('/')
def index():
    return render_template('index.html') 

# -- Login Route --
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        remember = request.form.get('remember')

        ref = db.reference('users')
        users = ref.get()

        if users: 
            for user_id, user_data in users.items():
                if user_data['username'] == username and check_password_hash(user_data['password'], password):
                    return redirect(url_for('index'))
                  
        return render_template('login.html', message="Invalid credentials. Please try again.")

    return render_template('login.html')

# Register Route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        # Email validation
        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(email_regex, email):
            return render_template('register.html', message="Invalid email format. Please try again.")
        
        # Passwords match
        if password != confirm_password:
            return render_template('register.html', message="Passwords do not match. Please try again.")

        # Password strength validations
        if not re.search(r'[A-Za-z]', password):
            return render_template('register.html', message="Password must contain at least one letter.")
        if not re.search(r'[0-9]', password):
            return render_template('register.html', message="Password must contain at least one number.")
        if not re.search(r'[!@#$%^&*(),.?\":{}|<>]', password):
            return render_template('register.html', message="Password must contain at least one special symbol.")

        hashed_password = generate_password_hash(password)

        ref = db.reference('users')
        ref.push({
            'username': username,
            'email': email,
            'password': hashed_password  
        })

        return redirect('login')
    
    return render_template('register.html')
           
# -- Logout Route --
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))
if __name__ == '__main__':
    app.run(debug=True)
