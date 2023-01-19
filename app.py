from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)


@app.route('/index',methods=['GET','POST'])
def home():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('index.html')
    return render_template('index.html')



@app.route('/calender',methods=['GET','POST'])
def calender():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('calender.html')
    return render_template('calender.html')



@app.route('/',methods=['GET','POST'])
def about():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('about.html')
    return render_template('about.html')

@app.route('/task',methods=['GET','POST'])
def task():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('task.html')
    return render_template('task.html')

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(host='0.0.0.0', port=5000,debug=True)