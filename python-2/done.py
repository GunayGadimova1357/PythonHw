import string
text =(input("input text: "))
print("choose a method: 1.upper() 2.lower() 3.replace()")
choose=int(input())
if choose==1:
    uppercase_text = ""
    for i in range(len(text)):
        if text[i] in string.ascii_lowercase:
            uppercase_text += string.ascii_uppercase[string.ascii_lowercase.index(text[i])]
        else:
            uppercase_text += text[i]
    print(uppercase_text) 
elif choose==2:
    lowercase_text = ""
    for i in range(len(text)):
        if text[i] in string.ascii_uppercase:
            lowercase_text += string.ascii_lowercase[string.ascii_uppercase.index(text[i])]
        else:
            lowercase_text += text[i]
    print(lowercase_text) 
else:
    old_substring =input('input old substring: ')
    new_substring =input("input new substring:")
    parts = text.split(old_substring)
    output_string = new_substring.join(parts)
    print(output_string)