from flask import Flask, render_template, request, redirect, session

app = Flask(__name__) 
app.secret_key = "Vollstin"
from user_modal import Users


# table_name/id/action
@app.route('/users')
def all_users():
    all_users = Users.get_all()
    return render_template('index.html', all_users=all_users)

@app.route('/users/new') #route to display new user form
def new_user():
    return render_template('user_new.html')

@app.route('/users/create', methods = ['POST'])
def create_user():
    print(request.form)
    Users.create(request.form)
    return redirect('/users')

@app.route('/users/<int:id>/view')
def view_one_user(id):
    data = {
        'id': id
    }
    one_user = Users.get_one(data)
    return render_template("user_one.html", one_user=one_user)

@app.route('/users/<int:id>/edit')
def edit_user_form(id):
    data = {
        'id': id
    }
    one_user = Users.get_one(data)
    return render_template('user_edit.html', one_user=one_user)

@app.route('/users/<int:id>/update', methods=['POST'])
def update_user(id):
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'id': id
    }
    Users.update(data)
    return redirect('/users')

@app.route('/users/<int:id>/delete')
def delete_user(id):
    data = {
        'id': id
    }
    Users.delete(data)
    return redirect('/users')





if __name__=="__main__":    
    app.run(debug=True)  