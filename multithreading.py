import threading
import time 


#indicates some task being done 
def func(seconds):
    print(f"sleeeping for {seconds} seconds")
    time.sleep(seconds)

func (4)    
func (2)    
func (1)    
    

# t1 = threading. Thread(target=func, args=[4])
# t2 = threading. Thread(target=func, args=[2])
# t3 = threading. Thread(target=func, args=[1])
 
# t1.start()
# t2.start()
# t3.start()