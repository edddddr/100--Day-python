from flask import Flask, render_template, request

app = Flask(__name__)

def valid_login(username, password):
    return username == "admin" and password == "1234"

def log_the_user_in(username):
    return render_template('index.html', username = username)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    error = None
    print(request.form['password'])
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'

    return render_template('index.html', error=error)


if __name__ == '__main__':
    app.run(debug=True)