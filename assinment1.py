#reverse a str
inp="This is my python program"[::-1]

print(inp)

inp="This is my first python program"
#inc = -1
result = ""
for item in range(len(inp)-1, -1, -1):
    result = result + inp[item]
    #inc =inc -1
print(result)
print(list(range(len(inp)-1, -1, -1)))
print(inp[len(inp)-1])
print(range(len(inp)))



inb = "I studied mechanical engineering"
res = ""
for item in range(len(inb)-1,-1,-1):
    res=res+inb[item]
print(res)
print(range(len(inb)))
print(list(range(len(inb))))