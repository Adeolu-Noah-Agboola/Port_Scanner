from flask import Flask, request, make_response, render_template, url_for, redirect, request
app=Flask(__name__,template_folder='templates')


@app.route('/login', methods=['GET','POST'])
def index():
#form that allows for entering a username and password
    if request.method== 'GET':
        return render_template('index.html')
    elif request.method == "POST":
        username = request.form.get['username']
        password = request.form.get['password']
        if username == "adeolu" and password == 'cool':
            return "Success"
        else:
            return "Failure"



#Automatically upload and Display port_scan textfile
@app.route('/', methods=['GET','POST'])
def upload():
     
     with open("log_file.txt", 'r') as f:
          text=f.readlines()
          return text

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)