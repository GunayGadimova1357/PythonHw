def remove_item(list1, toremove):
    if toremove in list1:
        list1.remove(toremove)
    else:
        print("not found in the list")
    return list1  

print("---remove an item from a list---")
while True:
    try:
        count=(int(input("how many items you want to add?\ncount: ")))
        list1=[input("item: ") for j in range(count)]
        toremove=input("what do you want do remove?\ninput: ")
    except ValueError:
        print("count must be an integer!")
        continue
    print("list:", list1)  
    list1=remove_item(list1, toremove)
    print(list1)
    break