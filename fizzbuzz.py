size=4
numbers=['L','D','D','L']
count=0
for each in range(size):
    if numbers[each]=='D':
        numbers[each]='L'
        if each+2<=size:
            numbers[each+1],numbers[each+2]=numbers[each+2],numbers[each+1]
            count+=1
    print(count)
inp=[12,2,15,14]
"FIZZBUZZ"
for num in inp:

    if num%3 == 0 and num%5 == 0:
        print("FIZZBUZZ")
    elif num%5 == 0:
        print("BUZZ")
    elif num%3 == 0:
        print("FIZZ")

