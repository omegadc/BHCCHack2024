from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
  return 'Hello from Flask!'


@app.route('/home_test')
def home_test():
  return render_template('home_test.html')


@app.route('/home')
def home():
  return render_template('home.html')


@app.route('/directory_test')
def directory_test():
  return render_template('directory_test.html')


@app.route('/directory')
def directory():
  return render_template('directory.html')


@app.route('/test_file')
def test_file():
  return render_template('test_file.html')


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)
  '''
 Datebase Solution
  PostgresSql- paid
  Replit DB- free
  '''
