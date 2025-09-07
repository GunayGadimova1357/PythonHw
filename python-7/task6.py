def digits_num(num: int):
    digits=0
    while num>0:
        num=num//10
        digits+=1
    return digits
        
num=int(input("enter the number: "))
digits_count=digits_num(num)
print(digits_count)
