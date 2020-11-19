import pandas as pd
import time
import datetime
import random
import string

a = int(input("Enter 1st num -> "))
b = int(input("Enter 2nd num -> "))
sums = a+b
seconds =[]
values=[]
timestamp = []
a = time.monotonic()

while(1):
    b = time.monotonic()
    ct = str(datetime.datetime.now())
    #ct = ct[0:19]
    ch = random.choice(string.ascii_letters)
    if((ch>='a' and ch<= 'y') or (ch>='A' and ch<='Y')):
        sums+=1
        seconds.append(str(b-a)[0:1])
        values.append(sums)
        timestamp.append(ct)
        print(sums)
    if(ch == 'z' or ch == 'Z'):
        df = pd.DataFrame.from_dict({'TimeStamp':timestamp,'Duration': seconds,'Sum Value':values})
        df.to_excel('exported.xlsx', header=True, index=False)
        quit()
    

