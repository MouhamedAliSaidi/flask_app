from flask import Flask, render_template, request, redirect
import datetime

app = Flask(__name__)
app.secret_key = '123' 

users = []

@app.route('/read')
def read():
    return render_template('read.html', users=users)

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/process', methods=['POST'])
def process():
    first_name = request.form['name']
    last_name = request.form['lastname']
    email = request.form['email']
    created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    user_id = len(users) + 1
    users.append({
        'id': user_id,
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'created_at': created_at
    })

    return redirect('/read')

if __name__ == "__main__":
    app.run(debug=True)
