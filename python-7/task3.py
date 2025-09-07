def square_pattern (symbol_pattern, num,option):
    if option ==True:
        for i in range (num):
           print(symbol_pattern*num)
    elif option==False:
       for i in range (num):
          if i==0 or i==num-1:
             print(symbol_pattern*num)
          else:
            print(symbol_pattern+" "*space+symbol_pattern)  

option=bool((input("what type square u want?\n1.filled, type true\n2.hollow, type false\nyour option: ")))
symbol_pattern=input("enter symbol for pattern: ")
num=int(input("enter lenght: "))
space=num-2
square_pattern(symbol_pattern, num, option)