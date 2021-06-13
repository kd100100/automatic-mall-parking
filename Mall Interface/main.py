from interface import led
i=0
while(i!=-1):
    a=int(input())
    if a==[-1]:
        break
    led(a)
