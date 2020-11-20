import multiprocessing
import random
import string
import pandas as pd
import time
import datetime
a = int(input("Enter 1st num -> "))
b = int(input("Enter 2nd num -> "))
sums = a+b
seconds =[]
values=[]
timestamp = []
a = time.monotonic()
def sender(conn, msgs):
    """
    function to send signal to other end of pipe
    """
    for msg in msgs:
        conn.send(msg)
        print("Sent the signal to p1: {}".format(msg))
    conn.close()
 
def receiver(conn):
    """
    function to print the signal received from other
    end of pipe
    """
    while 1:
        msg = conn.recv()
        msgs = random.choice(string.ascii_letters)
        if msg == ((msgs>='a' and msgs<= 'y') or (msgs>='A' and msgs<='Y')) :
                    break
        print("Received the signal to p2: {}".format(msg))
while 1:
    b = time.monotonic()
    ct = str(datetime.datetime.now())
    #ct = ct[0:19]
    msgs = random.choice(string.ascii_letters)
    if((msgs>='a' and msgs<= 'y') or (msgs>='A' and msgs<='Y')):
        sums+=1
        seconds.append(str(b-a)[0:1])
        values.append(sums)
        timestamp.append(ct)
        print(sums)
        # creating timestamp and exporting it to .xlsx
    if(msgs == 'z' or msgs == 'Z'):
        df = pd.DataFrame.from_dict({'TimeStamp':timestamp,'Sum Value':values})
        df.to_excel('exported.xlsx', header=True, index=False)
        break
        print("Received the message: {}".format(msg))
if __name__ == "__main__":
    # messages to be sent
    msgs = random.choice(string.ascii_letters)
 
    # creating a pipe
    parent_conn, child_conn = multiprocessing.Pipe()
 
    # creating new processes
    p1 = multiprocessing.Process(target=sender, args=(parent_conn,msgs))
    p2 = multiprocessing.Process(target=receiver, args=(child_conn,))
 
    # running processes
    p1.start()
    p2.start()
 
    # wait until processes finish
    p1.join()
    p2.join()
    quit()
    

