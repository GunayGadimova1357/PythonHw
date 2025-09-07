guest_list = [
    ["Alice", 30],
    ["Bob", 25],
    ["Charlie", 35],
    ["Diana", 28]
]

def print_menu():
    print("1.add guest\n"
          "2.delete guest\n"
          "3.find guest\n"
          "4.show all guests") 

def print_menu2():
    print("1.delete a guest by name\n"
          "2.delete a guest by serial number")
    
def print_menu3():
    print("1.find a guest by name\n"
          "2.find a guest by serial number\n"
          "3.find a guest by age")

def add_guest(name, age):
    guest = [name, age]
    guest_list.append(guest)
    print("---------------------------") 
    print(f"added guest: {name}, age: {age}")
    print("---------------------------") 
    print("a new guest list: ",guest_list)

def delete_byname(by_name):
    for i in guest_list:
        if i[0]==by_name:
            guest_list.remove(i)
    print("---------------------------") 
    print("a new guest list: ",guest_list)      

def delete_by_serial_number(by_serial_number):
    index=by_serial_number-1
    if 0 <= index < len(guest_list):
        guest_list.pop(index)  
        print("---------------------------")
        print("a new guest list: ",guest_list)  
    else:
        print("---------------------------") 
        print("invalid index. no guest found.")  


def find_by_name(fname):
        found=False
        for i in guest_list:
         if i[0]==fname:
            print("---------------------------") 
            print("a guest: ",i)  
            found=True
        if found==False:
            print("---------------------------") 
            print("no guest found.")       

def find_by_serial_number(fserialnumber):
    index=fserialnumber-1
    if 0 <= index < len(guest_list):
        print("---------------------------") 
        print("a guest: ", guest_list[index])
    else:
        print("---------------------------") 
        print("invalid index. no guest found.")            

def find_by_age(fage):
        found=False
        for i in guest_list:
         if i[1]==fage:
            print("---------------------------") 
            print("a guest: ",i)
            found=True
        if found==False:
            print("---------------------------") 
            print("no guest found.")  


while True:
    print("---------------------------")
    print_menu() 
    print("---------------------------")  
    while True:
        try:
            option=int(input("your choice: "))
            break
        except ValueError:
            print("wrong input")
            continue
    if option==1:
        print("---------------------------")  
        print("---add a guest to the guest list---")
        name=input("name: ").capitalize()
        while True:
            try:
                age=int(input("age: "))
                break
            except ValueError:
                print("wrong input")
                continue
        add_guest(name, age)   
    elif option==2:
        print("---------------------------")  
        print("---delete a guest from the guest list---")
        print("---------------------------")
        print_menu2()
        print("---------------------------")  
        while True:
            try:
                option2=int(input("your choice: "))
                break
            except ValueError:
                print("wrong input")
                continue
        if option2==1:
            print("---------------------------")  
            print("---delete a guest from the guest list by name---")
            by_name=input("name: ").capitalize() 
            delete_byname(by_name)
        elif option2==2:
            print("---------------------------")  
            print("---delete a guest from the guest by serial number---")
            while True:
                try:
                    by_serial_number=int(input("serial number(1,2,..): ")) 
                    break
                except ValueError:
                    print("wrong input")
                    continue
            delete_by_serial_number(by_serial_number)
        else:
            print("wrong input")
            continue
    elif option==3:
        print("---------------------------")
        print_menu3()
        print("---------------------------")  
        print("---find a guest from the guest list---")
        while True:
            try:
                option3=int(input("your choice: "))
                break
            except ValueError:
                print("wrong input")
                continue
        if option3==1:
            print("---------------------------")  
            print("---find a guest from the guest list by name---")
            fname=input("name: ").capitalize()
            find_by_name(fname)
        elif option3==2:
            print("---------------------------")  
            print("---find a guest from the guest list by serial number---")
            while True:
                try:
                    fserialnumber=int(input("num: "))
                    break
                except ValueError:
                    print("wrong input")
                    continue
            find_by_serial_number(fserialnumber)
        elif option3==3:
            print("---------------------------")  
            print("---find a guest from the guest list by age---")
            while True:
                try:
                    fage=int(input("age: "))
                    break
                except ValueError:
                    print("wrong input")
                    continue
            find_by_age(fage)
        else:
            print("wrong input")
            continue    
    elif option==4:
        print("---a guest list---")
        print(guest_list)
    else:
        print("wrong input")
        continue
    while True:
        try:
            print("do you want to continue?\n"
                  "1.yes\n"
                  "2.no\n")
            option4=int(input("your choice: "))
            break
        except ValueError:
            print("wrong input")
            continue
    if option4==1:
        continue
    elif option4==2:
        break
    else:
        print("wrong input")