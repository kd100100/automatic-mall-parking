# MongoDB Setup
from pymongo import MongoClient
cluster = MongoClient("mongodb+srv://kd100100:keerthi10@cluster0.dv2cb.mongodb.net/smartcity?retryWrites=true&w=majority")
db = cluster["smartcity"]
collection = db["data1"]

# db Format
# id,reg_no,color,wing,slot,in_time,out_time,amt,active

import random
import datetime
from ReadCard import readRFID


# Fetching Data for Display
def last_3_data():
    print('last_3_data')
    id = collection.count_documents({})
    last=[]
    last.append(collection.find_one({"_id":(id-1)}))
    last.append(collection.find_one({"_id":(id-2)}))
    last.append(collection.find_one({"_id":(id-3)}))
    return last

# Inserting Data
def enter_data():
    print('enter_data')
    id = collection.count_documents({})
    reg_no = readRFID().strip()
    print("read rfid")
    print(id)
    color = color_choice(id)
    print(color)
    wing = wing_choice(id)
    #wing = 'A'
    print(wing)  
    slot = slot_random(wing)
    #slot = 4
    print(slot)
    in_time = time()
    out_time = 'Parked!'
    amt = 0
    active = 1
    ins={"_id":id, "reg_no":reg_no, "color":color, "wing":wing, "slot":slot, "in_time":in_time, "out_time":out_time, "amt":amt, "active":active}
    print(ins)
    collection.insert_one(ins)
    print("inserted data")

def color_choice(n):
    n=int(n)
    if (n%3==0): return 3
    elif ((n+1)%3==0): return 2
    else: return 1

def wing_choice(n):
    n=int(n)
    if n%2==0: return 'B'
    else: return 'A'
    

def slot_random(wing):
    active = []
    temp_data = collection.find({"wing": wing,"active":1})
    for i in temp_data:
        active.append(i["slot"])
    a=0
    while(a==0):
        slot=random.choice([2,3,4,5,6])
        if slot not in active:
            a=1
    return slot

def time():
    return(datetime.datetime.now().strftime("%X"))

def exit_data():
    print('exit_data')
    reg_no = readRFID().strip()
    temp_data = collection.find_one({"reg_no": reg_no,"active":1})
    out_time = time()
    in_time = temp_data["in_time"]
    o_t = out_time.split(":")
    i_t = in_time.split(":")
    o_min = int(o_t[0])*60 + int(o_t[1])
    i_min = int(i_t[0])*60 + int(i_t[1])
    d_min = o_min - i_min
    amt=0
    if (d_min<=60):
        amt = 50
    else:
        amt = ((d_min//60)+1)*35+15
    collection.update_one({"reg_no":reg_no ,"active":1}, {"$set":{"amt":amt , "out_time": out_time, "active":0}})
    return amt
    
def check():
    print('check')
    reg_no = readRFID().strip()
    temp_data = collection.find_one({"reg_no": reg_no,"active":1})
    if temp_data["wing"]=="A":
        collection.update_one({"reg_no":reg_no ,"active":1}, {"$set":{"wing":"B" , "slot": slot_random("B")}})

def led_data():
    print('lled_data')
    last=last_3_data()
    red={}
    green={}
    blue={}
    for i in range(3):
        if last[i]["color"]==1:
            red["wing"]=last[i]["wing"]
            red["slot"]=last[i]["slot"]
        elif last[i]["color"]==2:
            green["wing"]=last[i]["wing"]
            green["slot"]=last[i]["slot"]
        elif last[i]["color"]==3:
            blue["wing"]=last[i]["wing"]
            blue["slot"]=last[i]["slot"]
    return red,green,blue
