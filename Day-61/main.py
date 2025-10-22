from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, Regexp
from flask_bootstrap import Bootstrap


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),  DataRequired(),
        Regexp(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",
               message="Invalid email address format.")])
    password = StringField('Password', validators=[DataRequired(), Length(min=4)])
    submit = SubmitField(label="Log In")

app = Flask(__name__)
Bootstrap(app)
app.secret_key = 'secretkey'



@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        email = form.email.data
        password = int(form.password.data)
        print(form.validate_on_submit(), email, password)

        if form.validate_on_submit() and email == 'admin@email.com' and password == 12345678:
            return render_template('success.html',  form = form)
        else:
            return render_template('denied.html',  form = form)
    return None



if __name__ == '__main__':
    app.run(debug=True)

