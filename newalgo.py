import threading 		
import time

semaphore = threading.Semaphore(1)

def run_process(process):
    semaphore.acquire()
    print(f'Starting {process}')
    time.sleep(1)
    print(f'Finished {process}')
    semaphore.release()

List=[["p1",1,10],["p2",0,28],["p3",1,78],["p4",0,100],["p5",1,45],["p6",0,78]]
threads = []

sjf_list = sorted(List, key=lambda x: x[2])


h=[]
l=[]
for items in sjf_list:
    if((items[1])==1):
        h.append(items[0])
    else:
        l.append(items[0])   
        
print("high priority",h)
print("low priority",l)  
for process in h:
    thread = threading.Thread(target=run_process, args=(process,))
    threads.append(thread)
for process in l:
    thread = threading.Thread(target=run_process, args=(process,))
    threads.append(thread)    
    
    
for thread in h:
    run_process(thread)  
    
for thread in l:
    run_process(thread)      

print('All processes finished.')        
