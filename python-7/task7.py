def palindrome(txt):
    checked=""
    for i in txt:
        checked=i+checked
    if txt==checked:
        print(True)    
    else:
        print(False)
txt=input("a word or number to check if it is a palindrome: ") 
palindrome(txt) 