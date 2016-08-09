from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map

app = Flask(__name__)
Bootstrap(app)
GoogleMaps(app, key="AIzaSyB4tGK7l8s4VDOOXz1bZYw2Roj48n-ZQm8")

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/member1')
def member1():
  return render_template('member1.html')

@app.route('/member2')
def member2():
  return render_template('member2.html')

@app.route('/recruit')
def recruit():
  return render_template('recruit.html')

@app.route('/navigation')
def navigation():
  mymap = Map(
    identifier="view_side",
    lat=35.0305565,
    lng=126.7173055,
    zoom=16,
    style="height:300px;width:device-width;margin:0;",
    markers=[(35.0305565, 126.7173055)]
  )
  return render_template('navigation.html', mymap=mymap)

if __name__ == '__main__':
  app.run(debug=True)
