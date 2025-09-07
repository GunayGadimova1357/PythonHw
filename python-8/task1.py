def product_list(list1):
    product=1
    for i in list1:
        product*=i
    return product    

print("---the product of elements in a list---")
while True:
    try:
        count=(int(input("how many number you want to add?\ncount: ")))
        list1=[float(input("number: ")) for j in range(count)]
    except ValueError:
        print("count must be an integer! numbers can be float.")
        continue
    print("list:", list1)  
    product_list(list1)
    print(product_list(list1))
    break