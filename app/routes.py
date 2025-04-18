from flask import render_template, request, redirect, url_for
from app import app

users_data = []
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        user_data = {
            'city': request.form.get('city'),
            'hobby': request.form.get('hobby'),
            'age': request.form.get('age')
        }
        if name:
            users_data.append({'name': name, 'user_data': user_data})
            return redirect(url_for('index'))
    return render_template('users.html', users_data = users_data)

