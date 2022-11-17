class SumOfElements:
    def __init__(self):
        pass
#    def sumofelements(self, firstelement, secondelement):
 #       return firstelement+secondelement


    def sumofelements(self, firstelement, secondelement,thirdelement=0):
        return firstelement+secondelement+thirdelement




ssom=SumOfElements()
print(ssom.sumofelements(3,4))



# Python program to find sum of elements in list

total = 0

# creating a list
list1 = (11, 5, 17, 18, 23, 20)

# Iterate each element in list
# and add them in variable total
for ele in range(0, len(list1)):
    total = total + list1[ele]

# printing total value
print("Sum of all elements in given list: ", total)



list1=[11,22,44,55,77,8]
total=sum(list1)
res=total
print("total sum is",res)











