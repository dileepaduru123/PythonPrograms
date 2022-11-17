li = ['a','r','i',1,2,3,'f']
y=li.append('ox')
print(li)

li=['a','r','i',1,2,3,'f']
y=li.clear()
print(li)

li=['a','r','i',1,2,3,'f']
y=li.copy()
print(y)

li=['a','r','i',1,2,3,'f']
y=li.count('r')
print(y)

li=['a','r','i',1,2,3,'f']
y=['e','i','o','u']
z=li.extend(y)
print(li)

li=['a','r','i',1,2,3,'f']
y=li.index('r')
print(y)

li=['a','r','i',1,2,3,'f']
y=li.insert(3,'r')
print(li)

li=['a','r','i',1,2,3,'f']
y=li.pop(3)
print(li)

li=['a','r','i',1,2,3,'f']
y=li.pop(3)
print(y)

li=['a','r','i',1,2,3,'f']
y=li.remove('r')
print(li)

li=['a','r','i',1,2,3,'f']
y=li.reverse()
print(li)

li=['a','r','i','f']
y=li.sort()
print(li)


li=['a','r','i','f']
y=li.sort(reverse=True)
print(li)

li=['a','r','i','f']
y=li.sort(reverse=False)
print(li)


car={
    "brand":"ford",
    "model":"ford"
}
x=car.clear()
print(car)

car={
    "brand":"bmw",
    "model":"x3"
}
x=car.copy()
print(x)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("price", 15000)

print(x)


car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("brand")

print(x)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.keys()

print(x)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.values()

print(x)
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.items()

print(x)
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.pop("brand")

print(x)
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.popitem()

print(x)

car={
    "brand":"Audi",
    "model":"a6",
    "year":2005
}
x=car.get("brand")
print(x)

car={
    "brand":"Audi",
    "model":"A6",
    "year":2006
}
x=car.setdefault("brand")
print(x)
car={
    "brand":"Audi",
    "model":"A3",

}
x=car.update({"colour":"white"})
print(car)







