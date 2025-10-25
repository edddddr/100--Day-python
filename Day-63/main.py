from flask import Flask, render_template, request, redirect, url_for, session, current_app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, mapped_collection
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///book.db"
db.init_app(app)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

class Book(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True, nullable=True)
    author: Mapped[str] = mapped_column(nullable=True)
    rate: Mapped[int] = mapped_column(nullable=True)



with app.app_context():
     db.create_all()
     book = Book.query.all()


print()

@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == 'POST':
        current_book_id = int(session['id'])
        book_to_update = Book.query.get(current_book_id)
        print('before', book_to_update.rate)
        book_to_update.rate = request.form['rating']

    return render_template('index.html', books=book)



@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        book = Book(
            title=request.form["title"],
            author=request.form["author"],
            rate=request.form["rating"],
        )
        db.session.add(book)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template('add.html')


@app.route("/edit", methods=['GET', 'POST'])
def edit():
    book_id = request.args.get('id')
    book_to_update = Book.query.get(book_id)
    session['id'] = book_id
    return   render_template('edit.html',  book=book_to_update)

@app.route("/delete")
def delete():
    book_id = request.args.get('id')
    book_to_delete = Book.query.get(book_id)
    print(book_to_delete)
    db.session.delete(book_to_delete)
    db.session.commit()

    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

