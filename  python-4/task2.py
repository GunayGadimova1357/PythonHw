txt=input("a word or number to check if it is a palindrome: ")
checked=""
for i in txt:
    checked=i+checked
if txt==checked:
     print("it is a palindrome.")
else:
     print("it is not a palindrome.")
