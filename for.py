import time
#for loops=execute block of code fixed number of times
# you can iterate over range,string,sequence
#range(start,end,step)
"""for x in range(1,10,2):
    print(x)

print("happy new year")"""
"""credit="1234-4567-43"
for x in credit:
    print(x)

for x in range(2,11):
    if x==10:
        break
    else:
        print(x)"""
#COUNTDOWN APP
my_time=int(input("enter the countdown :"))

"""for x in range(my_time,0,-1):
    seconds= x % 60
    minutes=int(x/60)%60
    hours=int(x/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("TIMES UP")"""
#nested loop=loop within another loop

"""for x in range(3):
    for y in range(1,10):
        print(y,end="")
    print()
"""
rows=int(input("enter the rows:"))
column=int(input("enter the column:"))
symbol=input("enter the symbol:")
for x in range(rows):
    for y in range(column):
        print(symbol,end="")
    print()




