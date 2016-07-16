from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

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
  return render_template('navigation.html')

if __name__ == '__main__':
  app.run(debug=True)
