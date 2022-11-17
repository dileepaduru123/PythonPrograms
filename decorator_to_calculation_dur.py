import time
import math
#decorator to calculation duration
#taken by any function.
def calculate_time(func):
    # added arguments inside the inner1,
    # if funcion takes any arguments,
    # can be added like this.
    def inner1(*args,**kwargs):
        # storing time after function execution
begin =time.time()
func(*args,**kwargs)
#soring time after function execution
end=time.time()
print("Total time taken in : ",
      func._name_,end-begin)
return inner1
#this can be added to any function present,
#in this case to calculate a factorial
@calcuate_time
def factorial(num):
    # sleep 2 seconds because it takes very less time
    # so that you can see the actual diffference
    time.sleep(2)
    print(math.factorial(num))

#calling the function.
factorial(10)