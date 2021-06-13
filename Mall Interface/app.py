# Flask Setup
from flask import Flask,render_template,url_for,request,redirect
app = Flask(__name__)

# MongoDB Setup
'''
from pymongo import MongoClient
cluster = MongoClient("mongodb+srv://kd100100:keerthi10@cluster0.dv2cb.mongodb.net/smartcity?retryWrites=true&w=majority")
db = cluster["smartcity"]
collection = db["data1"]
'''
# Data Fetching and Storing Py File
from operation import enter_data,last_3_data,exit_data,check,led_data
from led import led_on

data={}

# Main Route
@app.route('/', methods=['POST', 'GET'])
def home():
    red,green,blue = led_data()
    led_on(red,green,blue)
    if request.method=='POST':
        if request.form["button"]=="Enter":
            enter_data()
            return redirect(url_for("home"))
           
        if request.form["button"]=="Exit":
            data['amt']=exit_data()
            return redirect(url_for("home"))
            
        if request.form["button"]=="Check":
            check()
            return redirect(url_for("home"))

    # fetching last 3 rows
    last_3 = last_3_data()
    for i in range(3):
        if(last_3[i]["color"] == 1):
            data["red_wing"]=last_3[i]["wing"]
            data["red_slot_no"]=last_3[i]["slot"]
            data["red_reg_no"]=last_3[i]["reg_no"]
        elif(last_3[i]["color"] == 2):
            data["green_wing"]=last_3[i]["wing"]
            data["green_slot_no"]=last_3[i]["slot"]
            data["green_reg_no"]=last_3[i]["reg_no"]
        elif(last_3[i]["color"] == 3):
            data["blue_wing"]=last_3[i]["wing"]
            data["blue_slot_no"]=last_3[i]["slot"]
            data["blue_reg_no"]=last_3[i]["reg_no"]
    data["lcolor"]=last_3[0]["color"]
    data["lwing"]=last_3[0]["wing"]
    data["lslot"]=last_3[0]["slot"]
    data["lreg_no"]=last_3[0]["reg_no"]
    
    return render_template('index.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)