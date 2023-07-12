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





if __name__=="__main__":    
    app.run(debug=True)  