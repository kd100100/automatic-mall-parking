'''
{
  "Find": "Find", 
  "eta_time": "17:19"
}

hours : minutes : day
'''
import random
f = open('data.txt','w')
weeks = 100
start_time = 9
end_time = 22
total_slots = 1000
for i in range(weeks):
    for day in range(1,8): #1 = Sunday ..etc
        for j in range(start_time,end_time):
            for k in range(60):
                if(day==1):
                    free_slots = random.randint(0,3)
                elif(day==2):
                    free_slots = random.randint(0,10)
                elif(day==7):
                    free_slots = random.randint(1,5)
                else:
                    free_slots = random.randint(3,10)
                x = str(j)+","+str(k)+","+str(day)+","+str(free_slots)+"\n"
                f.write(x)
f.close()