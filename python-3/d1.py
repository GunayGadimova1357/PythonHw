#full diamond pattern 
n=int(input())
if(n%2!=0): 
    for i in range(1, n+1, 2):
        if i==1:
            star=1
            outterspace=(n-star)//2
            print(" "*(outterspace)+"*"*(star)+" "*(outterspace))
        else:
            star=i
            outterspace=(n-star)//2
            print(" "*(outterspace)+"*"*(star)+" "*(outterspace))
    for j in range(n, 1, -2 ):
        star1=j-2
        outterspace1=(n-star1)//2
        print(" "*(outterspace1)+"*"*(star1)+" "*(outterspace1))