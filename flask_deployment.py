from flask import Flask, request

app=Flask(__name__)

@app.route('/add',methods = ['POST', 'GET'])
def add():
    a=int(request.form['a'])
    b=int(request.form['b'])
    return str(a+b)




@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      a=request.args.get('a')
      b=request.args.get('b')
      return int(a)+int(b)
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

if __name__=='__main__':
    app.run()