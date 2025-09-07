import random
num=[]
n=int(input("input count of numbers for a list: "))
a=int(input("start of random numbers: "))
b=int(input("end of random numbers: "))
for i in range(n):
    num.append(random.randint(a,b))
print(num)
while True:
    print("\nchoose a function: ")
    print(" 1.max\n 2.min\n 3.average\n 4.multiply everything by 2\n 5.exit\n")
    choice=int(input("your choice: "))
    if choice==1:
        largest=num[0]
        for i in range(1, len(num)):
            if num[i]>largest:
                largest=num[i]
        print(f"output: {largest}")
    elif choice==2:
        smallest=num[0]
        for i in range(1, len(num)):
            if num[i]<smallest:
                smallest=num[i]
        print(f"output: {smallest}")
    elif choice==3:
        sum=0
        average=0
        for i in range(len(num)):
            sum=sum+num[i]
        average=sum/2
        print(f"output: {average}")    
    elif choice==4:
        product=0
        l1=[]
        for i in range(len(num)):
            product=num[i]*2
            l1.append(product)
        print(f"output: {l1}")    
    elif choice==5:
        print("exit")
        break
    else:
        print("wrong input")
        continue