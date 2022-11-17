res={"name":"dileep",
     "age":20,
      "city":"kavali"}


print("age" in res)




#slising
li=["1","2","3","4","5"]
print(li[1:3])
print(li[::-1])
print(li[::-2])
print(li[::])
print(li[-1:])
print(li[-2:])
print(li[:5:2])
print(li[:3:-2])
lis=["a1","b2","c3","d4","e5","f6","g7","h8","i9","j10"]
print(lis[2:6:-2])
print(lis[12:6:-2])
print(lis[:-5])
print(lis[-1:])
print(lis[::2])
print(lis[::-2])
print(lis[-5:6])



#palindrom
name = "test"
if(name==name[::-1]):
    print("palindrom")
else:
    print("not")

#condition for palindrom
def is_palindrom(name):
    if(name==name[::-1]):
        return("is palindrom")
    else:
        return("not palindrom")
print(is_palindrom("test"))
print(is_palindrom("lol"))
print(is_palindrom([1,2,3,2,1]))
print(is_palindrom([1,[2,3],4,[3,2],1]))
print(is_palindrom([5,5,5]))
print(is_palindrom([-1,-2,-1]))




