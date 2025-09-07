#hollow diamond pattern 
n=int(input())
if(n%2!=0): 
    for i in range(1, n+1, 2):
        if i==1:
            star=1
            outterspace=(n-star)//2
            print(" "*(outterspace)+"*"*(star)+" "*(outterspace))
        else:
            star=i
            space=n-star
            outterspace=(n-star)//2
            innerspace=n-space-2
            print(" "*(outterspace)+"*"+" "*(innerspace)+"*"+" "*(outterspace))
    for j in range(n, 1, -2 ):
        star1=j-2
        space1=n-star1
        outterspace1=(n-star1)//2
        innerspace1=n-space1-2
        if innerspace1<0:
             print(" "*(outterspace1)+"*"*(star1)+" "*(outterspace1))
        else:
            print(" "*(outterspace1)+"*"+" "*(innerspace1)+"*"+" "*(outterspace1))
        
