def calculate_product(start: int, end:int):
    if start > end:
        start, end = end, start 
    product = 1
    for i in range(start, end + 1):
        product *= i
    return product

while True:
    try:
        start : int =int(input("enter the start num= "))
        end : int =int(input("enter the end num= "))        
        calculate_product(start, end)       
        result = calculate_product(start, end)
        print(result)   
        break  
    except ValueError:
      print("enter int!")
      continue 


