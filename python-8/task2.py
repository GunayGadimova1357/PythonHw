def min_list(list1):
    smallest=list1[0]
    for i in range(1, len(list1)):
        if list1[i]<smallest:
            smallest=list1[i]
    return smallest   

print("---the min element of a list---")
while True:
    try:
        count=(int(input("how many number you want to add?\ncount: ")))
        list1=[float(input("number: ")) for j in range(count)]
    except ValueError:
        print("count must be an integer! numbers can be float.")
        continue
    print("list:",list1)  
    min_list(list1)
    print(min_list(list1))
    break