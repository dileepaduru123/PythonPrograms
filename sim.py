"""


def a(i, Is=[]):
    Is.append(i)
    return Is
print(a(10))
print(a(12, []))
print(a(13))
def MissingNo(arr):
    n = len(arr):
    total=(n+1)*(n+2)/2
    arr_sum=sum(arr)
    return total-arr_sum
print(MissingNo([1,2,3,4,5,6,7,8,9,10]))
"""



#GCD of more than two (or array)numbers
#Function implements the Euclidean
#algorithm to find H.C.F. of two numbers

def find_gcd(x,y):
    while (y):
        x,y=y,x % y
    return x
#Driver code
1=[3,5,7]
num1=1[0]
num2=1[1]
gcd=find_gcd(num1,num2)
for i in range(2,len(1)):