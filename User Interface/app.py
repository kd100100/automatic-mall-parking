from flask import render_template,Flask,request,redirect,url_for
from prediction import free_slots
app = Flask(__name__)

# MongoDB Setup
from pymongo import MongoClient
cluster = MongoClient("mongodb+srv://kd100100:keerthi10@cluster0.dv2cb.mongodb.net/smartcity?retryWrites=true&w=majority")
db = cluster["smartcity"]
collection = db["data1"]

data_car={}

@app.route('/')
def home():
    global data_car
    data_car={}
    a=12-(collection.count_documents({"active":1}))
    return render_template('customer.html', data=a)
    
@app.route('/search', methods=['POST','GET'])
def search():
    if request.method=='POST':
        reg_no=request.form['reg_no']
        a=collection.find_one({"reg_no":reg_no, "active":1})
        if a==None:
            data_car["avail"] = 0
        else:
            data_car["avail"] = 1
            data_car["wing"] = a["wing"]
            data_car["slot"] = a["slot"]

    return render_template('search.html', data=data_car)

@app.route('/predict',methods = ['POST','GET'])
def predict_parking(data=-1):
    if(request.method == 'POST'):
        data = free_slots(request.form['eta_time'])
        return render_template('parking_left.html',data=data)
    return render_template('parking_left.html',data=data)

if __name__=='__main__':
    app.run(debug=True)