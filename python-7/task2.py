def even(start : int,end: int):
    if start%2!=0:
            start+=1
    for i in range(start, end+1, 2):
            print(i)    
while True:
    try:
        start : int =int(input("enter the start num= "))
        end : int =int(input("enter the end num= "))        
        even(start, end)        
    except ValueError:
      print("enter int!")
      continue