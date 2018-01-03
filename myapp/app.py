from flask import Flask,render_template,url_for,redirect,request

app = Flask(__name__)

@app.route('/')
def index():
  return "index page"


@app.route('/login', methods=['POST', 'GET'])
def login():
   error = None
   if request.method == 'POST':
        if valid_login(request.form['username'],request.form['password']):
           return redirect(url_for('welcome', username=request.form.get('username')))
        else:
           error = "Incorrect username and password"
   return render_template('login.html',error=error)


@app.route('/welcome/<username>')
def welcome(username):
       return render_template('welcome.html',username=username)

       
def valid_login(username, password):
    if username == password:
        return True
    else:
        return False

@app.route('/error')
def errorpage():
	return render_template('error.html')


if __name__ == '__main__':
    app.run(debug=True)
