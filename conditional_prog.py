age = 10


if age >= 8:
    print("Major")
    if age >= 60:
        print("senior citizen")
else:
    print("minor")


#  price on age

if age >= 12:
    print("Adult price :", 300)                   #print("Adult price :", 300, "allow :", 1)
elif age >= 2:
    print("Child price: ", 100)
else:
    print("Infant No price")





resi = []
for item in data:
     if item.get("st2")=="AD_IMPRESSION":
         resi.append(item.get("st2"))
     if item.get('json_data') and item["json_data"].get("publisher_revenue"):
         print(item.get('json_data'))
         if item["json_data"].get("publisher_revenue", 0)*100 == item.get("v"):
             print("true")
         else:
             print("false")

print(resi)

