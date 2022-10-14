from flask import Flask,render_template,request

app = Flask(__name__,template_folder='templates')


@app.route('/')
def home():
    return render_template('index.html')
database={'nach':'123','ancy':'1234'} 


@app.route('/form_login',methods=['POST','GET'])
def gfg():
   if request.method=="POST":
       user_name= request.form.get("username")
       return "Welcome "+user_name
   return render_template("home.html")
if __name__ == '__main__':
    app.run(debug=True) 

