def more_to_one(list1, list2):
    list3=[]
    list3.extend(list1)
    list3.extend(list2)
    return list3

print("---new list with items of two previous lists---")
while True:
    try:
        count=(int(input("how many items you want to add for the first list?\ncount: ")))
        list1=[input("item: ") for i in range(count)]
        count1=(int(input("how many items you want to add for the second list?\ncount: ")))
        list2=[input("item: ") for j in range(count1)]
    except ValueError:
        print("count must be an integer!")
        continue
    print("lists:", list1, "and", list2)  
    list3=more_to_one(list1, list2)
    print("new list with items of two prev lists: ", list3)
    break