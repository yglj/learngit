from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
     return '<h1 style="align:center;">home page</h1>'

@app.route('/login',methods=['GET'])
def login():
     return '''
               <form method="POST">
                    <p>user:    <input type="text" name="user"></p>
                    <p>password:<input type="password" name="password"></p>
                    <p><button type="submit">sign in</button></p>
               </form>
          '''

@app.route('/login',methods=["POST"])
def login_pass():
     if request.form['user'] == 'admin' and request.form['password'] == '123':
          return b'<h3>welcome ,enter this page</h3>'
     return  '<h3>bad user or password</h3>'

if __name__ == '__main__':
     app.run()
