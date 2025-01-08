from flask import Flask, render_template, request, redirect

import datetime

app = Flask(__name__)
app.secret_key = '123' 

users = []

@app.route('/')
def home():
    return redirect('/read')

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

@app.route('/edit/<int:user_id>')
def edit(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if not user:
        return "User not found", 404
    return render_template('edit.html', user=user)

@app.route('/update/<int:user_id>', methods=['POST'])
def update(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if not user:
        return "User not found", 404
    
    user['first_name'] = request.form['name']
    user['last_name'] = request.form['lastname']
    user['email'] = request.form['email']
    user['updated_at'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return redirect('/read')

@app.route('/delete/<int:user_id>')
def delete(user_id):
    global users
    users = [u for u in users if u['id'] != user_id]
    return redirect('/read')

@app.route('/user/<int:user_id>')    ##enhanced with ai
def user_details(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if not user:
        return "User not found", 404
    return render_template('user.html', user=user)


if __name__ == '__main__':
    app.run(debug=True)
