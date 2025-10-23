from pprint import pprint

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectMultipleField, SelectField
from wtforms.validators import DataRequired
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)



class CafeForm(FlaskForm):
    cafe_name = StringField('Cafe name', validators=[DataRequired()])
    cafe_Maps = StringField('Cafe Location on Google MAPs (url) ', validators=[DataRequired()])
    cafe_open_time = StringField('Open Time eg. 8AM', validators=[DataRequired()])
    cafe_closing_time = StringField('Closing Time eg. 5:30PM', validators=[DataRequired()])

    coffee_strength = SelectField('Coffee Strength',
        choices=[
            ('✘','✘'),
            ('☕', '☕'),
            ('☕☕', '☕☕'),
            ('☕☕☕', '☕☕☕'),
            ('☕☕☕☕', '☕☕☕☕'),
            ('☕☕☕☕☕', '☕☕☕☕☕')],
            # default='✘',
        validators=[DataRequired()])


    cofe_strength_rating = SelectField(
        'Select Fruits',
        choices =[
            ('✘','✘'),
            ('💪', '💪'),
            ('💪💪', '💪💪'),
            ('💪💪💪', '💪💪💪'),
            ('💪💪💪💪', '💪💪💪💪'),
            ('💪💪💪💪💪', '💪💪💪💪💪')],
        validators=[DataRequired()]
    )

    cofe_socket_rating = SelectField(
    'Select Fruits',
    choices =[
        ('✘','✘'),
        ('🔌', '🔌'),
        ('🔌🔌', '🔌🔌'),
        ('🔌🔌🔌', '🔌🔌🔌'),
        ('🔌🔌🔌🔌', '🔌🔌🔌🔌'),
        ('🔌🔌🔌🔌🔌', '🔌🔌🔌🔌🔌')],
    validators=[DataRequired()]
    )



    submit = SubmitField('Submit')


# Exercise:
# add: Location URL, open time, closing time, coffee rating, Wi-Fi rating, power outlet rating fields
# make coffee/Wi-Fi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods= ['GET', 'POST'])
def add_cafe():
    form = CafeForm()

    if form.validate_on_submit():
        cafe_name = form.cafe_name.data
        cafe_Maps = form.cafe_Maps.data
        cafe_closing_time = form.cafe_closing_time.data
        cafe_open_time = form.cafe_open_time.data
        coffee_strength = form.coffee_strength.data
        cofe_strength_rating = form.cofe_strength_rating.data
        cofe_socket_rating = form.cofe_socket_rating.data

        new_review = [
            cafe_name,
            cafe_Maps,
            cafe_open_time,
            cafe_closing_time,
            coffee_strength,
            cofe_strength_rating,
            cofe_socket_rating
                        ]

        with open('cafe-data.csv', 'a+', encoding="utf8") as csvfile:
            csvfile.seek(0, 2)  # move to end of file
            if csvfile.tell() > 0:  # check if file is not empty
                csvfile.seek(csvfile.tell() - 1)
                last_char = csvfile.read(1)
                if last_char != '\n':
                    csvfile.write('\n')

            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(new_review)

    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding="utf8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
             list_of_rows.append(row)



    return render_template('cafes.html', cafes=list_of_rows[1:], cafes_titles = list_of_rows[0])


if __name__ == '__main__':
    app.run(debug=True)
