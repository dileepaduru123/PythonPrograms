#recursive function to return gcd of a and b
def gcd(a,b):
#Everything divides 0
  if(a == 0):
    return b
  if(b == 0):
     return a
#base case
  if (a == b):
    return a
#a is greater
  if(a>b):
    return gcd(a-b,b)
  return gcd(a,b-a)
#driver program to test above function
a=93
b=57
if(gcd(a,b)):
    print("GCD of", a, "and", b, "is", gcd(a, b))
else:
    print("not found")

#To find H.C.F of two numbers
def cp_hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x%i==0)and(y%i==0)):
            hcf = i
    return hcf
num1=52
num2=22
print("THE H.C.F is",cp_hcf(num1,num2))



