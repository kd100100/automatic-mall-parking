import pickle
import datetime
#print(datetime.datetime.today().weekday()) #5
# 12:32

def free_slots(data):
    Hours = int(data[:data.find(':')])
    Minutes = int(data[data.find(':')+1:])
    z = datetime.datetime.today().weekday()
    if(z==6):
        day = 1
    else:
        day = z + 2
    regr = pickle.load(open('1model.pkl','rb'))
    output = regr.predict([[Hours,Minutes,day]])
    return round(float(output)/12 * 100,2)

