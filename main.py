#!/usr/bin/env python2

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask import Flask, render_template
import googlemaps

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

gmaps = googlemaps.Client(key='AIzaSyBV6lsdmG78rZGq5GCml7tidoPs-LYjUl0')

destinations = ["RAAF Amberley", "City4051 CrossFit", "55 Curzon St, Tennyson QLD 4105", "University of Queensland"]

class RequestForm(FlaskForm):
    start_location = StringField("Start Location", validators=[DataRequired()])
    submit = SubmitField('Calculate')

@app.route('/', methods=["GET", "POST"])
def homepage():
    form = RequestForm()
    if form.validate_on_submit():
        print("calc from" + form.start_location.data)
        mat = gmaps.distance_matrix([form.start_location.data], destinations)
        return "\n".join(["<p>" + y + ", " + x['duration']['text'] + "</p>" for x,y in zip(mat["rows"][0]['elements'], destinations)])
    return render_template('request.html', title='Distance Calculator', form=form)

if __name__ == "__main__":
    app.run()

