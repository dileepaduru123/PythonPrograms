#string

txt="dileep"
x=txt.capitalize()
print(x)


txt="dileep"
x=txt.upper()
print(x)


txt="This is dileep and dileep is a good person"
x=txt.rfind("dileep")
print(x)

txt="This is dileep and dileep is a good person"
x=txt.replace("dileep","siva",1)
print(x)


txt="This is dileep and dileep is a good person"
x=txt.split("dileep")
print(x)


txt="This is dileep and dileep is a good person"
x=txt.replace("is","was")
print(x)


txt="dileep"
x=txt.ljust(10)
print(x)

txt="dileep"
x=txt.zfill(20)
print(x)




z="This is my book and the book is white colour"
x=z.rsplit("book")
print(x)


z="This is my book and the book is white colour"
x=z.split("book")
print(x)

q="hello welcome to my world"
v=q.rsplit("o")
print(v)

q="hello welcome to my world"
v=q.rfind("o")
print(v)


q="hello welcome to my world"
v=q.find("o")
print(v)

q="hello welcome to my world"
v=q.startswith("o",4,15)
print(v)

q="hello welcome to my world"
v=q.partition("o")
print(v)

q="hello welcome to my world"
v=q.rindex("o")
print(v)

q="hello welcome to my world"
v=q.index("l")
print(v)

q="hello welcome to my world,HELLO WELCOME TO MY WORLD"
v=q.casefold()
print(v)

q="hello welcome to my world"
v=q.swapcase()
print(v)

q="hello welcome to my world"
v=q.upper()
print(v)

q="hello welcome to my world"
c=q.zfill(40)
print(c)

q="hello"," welcome", "to"," my"," world"
b="@".join(q)
print(b)


q=["hello to my"]
x=["world"]
z=q.extend(x)
print(q)

q=['hello to my']
x=['world']
z=q.append(x)
print(q)

q=['hello to my']
y=q.copy()
print(q)

q=['hello', ' my', 'world']
z=q.insert(1,'to')
print(q)
q=['hello','to','to','my','world']
z=q.pop(2)
print(q)

q=['hello','to','to','my','world']
z=q.pop(2)
print(z)

q=['hello','to','to','my','world']
z=q.count('to')
print(z)
