# 使用模板,模拟用户登录，未使数据库
from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
     return render_template(r'home.html')

@app.route('/sign',methods=['GET'])
def sign_form():
     return render_template('form.html')

@app.route('/sign',methods=['POST'])
def sign():
     username = request.form['username']
     password = request.form['password']
     if username == 'admin' and password == '123':
          return render_template('sign.html',username = username)
          #return render_template('baidu.html')
     return render_template('form.html',message='bad username or password',username = username)

if __name__ == '__main__':
     app.run()


'''
#home.html
<html>
<head>
     <title>Home</title>
</head>
<body>
     <h1><i>Home</i></h1>
</body>
</html>


#form.html
<html>
<head>
     <title>Please Sign In</title>
</head>
<body>
     {% if message %}
     <p style="color:red"> {{message}}</p>
     {% endif %}
     <form action="/sign" method="post>
          <legend>please sign in:</legend>
          <p><input name="username" placeholder="username" value="{{username}}"></p>
          <p><input name="password" placeholdr="password" type="password"></p>
          <p><button type="submit"> sign in</button></p>
     </form>
</body>
</html>

#sign.html
<html>
<head><title>welcome,{{username}}</title></head>
<body>
     <p>Welcome, {{username}} !</p>
</body>
</html>
'''
