def power_list(list1, n_power):
    powered_list=[i ** n_power for i in list1]
    return powered_list

print("---the n power of each element in a list---")
while True:
    try:
        count=(int(input("how many number you want to add?\ncount: ")))
        list1=[float(input("number: ")) for j in range(count)]
        n_power=int(input("enter power: "))
    except ValueError:
        print("count and power must be an integer! numbers can be float.")
        continue
    print("list:",list1)  
    result=power_list(list1, n_power)
    print(result)

    break