from pprint import pprint

from flask import Flask, render_template, redirect, url_for, request, session
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from wtforms import StringField, SubmitField
from wtforms.fields.simple import URLField
from wtforms.validators import DataRequired
import requests

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)


API_KEY= 'ba60168ef1416338f7d61126ffa400e7'
headers = {
    "accept": "application/json",
    "Authorization": f"Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1NzE0M2QyZjJmZmMxZDQzOWEyYzE0MzRiYzdiZDJmYSIsIm5iZiI6MTcxMDI4NjI1NS40ODk5OTk4LCJzdWIiOiI2NWYwZTVhZjk5MjU5YzAxNDg1YmY5ZGMiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.evQJgQtTZiovlA-9sBFYNgLM_QUBx-25fhhABE9ZnYs"
}

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movie.db"
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

db.init_app(app)

class Movie(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    title: Mapped[str] = mapped_column(unique=True, nullable=False)
    year: Mapped[int] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    ranking: Mapped[int] = mapped_column(nullable=False)
    rating: Mapped[float] = mapped_column(nullable=False)
    review: Mapped[str] = mapped_column(nullable=False)
    img_url: Mapped[str] = mapped_column(nullable=False)


class MovieForm(FlaskForm):
    title = StringField('Add Title', validators=[DataRequired()])
    rating = StringField('Your rating of 10 e.g 7.5', validators=[DataRequired()])
    review = StringField('Rating', validators=[DataRequired()])
    submit = SubmitField('Done')




    # new_movie = Movie(
    #  title="Phone Booth",
    #  year=2002,
    #  description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
    #  rating=7.3,
    #  ranking=10,
    #  review="My favourite character was the caller.",
    #  img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
    # )
    # db.session.add(new_movie)
    # db.session.commit()
    # db.drop_all()





@app.route("/", methods=['GET', 'POST'] )
def home():
    with app.app_context():
        db.create_all()
        movies = db.session.query().order_by(Movie.rating).all()
        print(movies)
    return render_template("index.html", movies= movies)


@app.route("/edit", methods=['GET', 'POST'])
def update():
    form = MovieForm()

    print("fir :", request.args.get('id'))
    if request.method == 'POST':
        movie_rating = form.rating.data
        movie_review = form.review.data

        print("sec :", request.args.get('id'))

        movie_to_update = Movie.query.get(request.args.get('id'))
        movie_to_update.rating = movie_rating
        movie_to_update.review = movie_review
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("edit.html", form=form)


@app.route("/delete")
def delete():
   movie_to_delete =  Movie.query.get(request.args.get('id'))
   print(movie_to_delete)
   db.session.delete(movie_to_delete)
   db.session.commit()
   return redirect(url_for('home'))

@app.route("/add", methods=['GET', 'POST'])
def add():
    form = MovieForm()
    if request.method == 'POST':
        movie_title = form.title.data
        movie_list_url = f"https://api.themoviedb.org/3/search/movie?query={movie_title}&include_adult=false&language=en-US&page=1"
        movies_data = requests.get(movie_list_url, headers=headers).json()['results']

        return render_template("select.html", movie_list=movies_data)

    if request.args.get('id'):
        movie_id = request.args.get('id')
        print(movie_id)
        movie_url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"
        response = requests.get(movie_url, headers=headers).json()


        new_movie = Movie(
         title = response['title'],
         year = response['release_date'],
         description = response['overview'],
         rating = response['vote_average'],
         ranking=0,
         review="not a review because to avoid null redirecting.",
         img_url = f"https://image.tmdb.org/t/p/w500{response['poster_path']}"
        )
        db.session.add(new_movie)
        db.session.flush()
        movie_db_id = new_movie.id
        db.session.commit()

        return redirect(url_for('update', id=movie_db_id))

    return render_template("add.html", form = form)



if __name__ == '__main__':
    app.run(debug=True)
