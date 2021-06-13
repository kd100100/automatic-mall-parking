# MongoDB Setup
from pymongo import MongoClient
cluster = MongoClient("mongodb+srv://kd100100:keerthi10@cluster0.dv2cb.mongodb.net/smartcity?retryWrites=true&w=majority")
db = cluster["smartcity"]
collection = db["data1"]

import datetime
import random

# collection.insert_one({"_id":0, "name":"dummy"})

# def color_choice(n):
#     n=int(n)
#     if (n%3==0): return '3'
#     elif ((n+1)%3==0): return '2'
#     else: return '1'

# def wing_choice(n):
#     n=int(n)
#     if n%2==0: return 'B'
#     else: return 'A'

# def slot_random(wing):
#     active = []
#     temp_data = collection.find({"wing": wing,"active":1})
#     for i in temp_data:
#         active.append(i["slot"])
#     a=0
#     while(a==0):
#         slot=random.choice([1,2,3,4,5,6])
#         if slot not in active:
#             a=1
#     return slot

# def time():
#     return(datetime.datetime.now().strftime("%X"))

# for i in range (3):
#     id = collection.count_documents({})
#     reg_no = input("Reg no: ")
#     color = color_choice(id)
#     wing = wing_choice(id)
#     slot = slot_random(wing)
#     in_time = time()
#     out_time = wing+str(slot)
#     amt = 0
#     active = 1
#     ins={"_id":id, "reg_no":reg_no, "color":color, "wing":wing, "slot":slot, "in_time":in_time, "out_time":out_time, "amt":amt, "active":active}
#     collection.insert_one(ins)

# data=collection.find({})
# for i in data:
#     print(i)

# collection.update_one({"_id":1}, {"$set":{"color":1}})
# collection.update_one({"_id":2}, {"$set":{"color":2}})
# collection.update_one({"_id":3}, {"$set":{"color":3}})

# collection.update_one({"_id":0}, {"$set":{"entry":2}})
# collection.update_one({"_id":0}, {"$set":{"exit":2}})

# temp_data = collection.find_one({"_id":1})
# in_time = temp_data["in_time"]
# in_time = "12:15:10"
# out_time = time()
# o_t = out_time.split(":")
# i_t = in_time.split(":")
# o_min = int(o_t[0])*60 + int(o_t[1])
# i_min = int(i_t[0])*60 + int(i_t[1])
# d_min = o_min - i_min
# if (d_min<=60):
#     amt = 50
# else:
#     amt = ((d_min//60)+1)*35+15

# print(i_t)
# print(o_t)
# print(i_min)
# print(o_min)
# print(d_min)
# print(d_min//60)
# print(amt)

#print(datetime.datetime.now())
data = collection.find({"active":1})
for i in data:
    print(i['reg_no'],i['wing'],i['slot'])

# from operation import *
a=collection.count_documents({"active":1})
print(a)
