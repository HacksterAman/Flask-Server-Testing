import random
import string
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

users = {
    "user1": {"password": "password1"},
    "user2": {"password": "password2"}
}

logged_in_users = {}

def generate_secret_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if username in users and users[username]['password'] == password:
        secret_code = generate_secret_code()
        logged_in_users[username] = secret_code
        return jsonify({'message': 'Login successful!', 'secret_code': secret_code})
    else:
        return jsonify({'message': 'Login failed! Invalid username or password.'}), 401

if __name__ == '__main__':
    app.run(debug=True)
