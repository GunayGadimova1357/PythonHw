import datetime

guest_list = [
    ["Alice", 30],
    ["Bob", 25],
    ["Charlie", 35],
    ["Diana", 28]
]

def filter(func, guest_list):
    result = []
    for i in guest_list:
        if func(i):
            result.append(i)
    return result

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

def delete_byname(name):
    global guest_list
    guest_list = filter(lambda x: x[0] != name, guest_list)
    print("---------------------------")
    print(f"deleted guest: {name}")
    print("---------------------------")
    print("a new guest list:",guest_list)   

def delete_by_serial_number(by_serial_number):
    index=by_serial_number-1
    if 0 <= index < len(guest_list):
        guest_list.pop(index)  
        print("---------------------------")
        print("a new guest list: ",guest_list)  
    else:
        print("---------------------------") 
        print("invalid index. no guest found.")  


def find_by_name(name):
    found = filter(lambda x: x[0] == name, guest_list)
    if found:
        print("---------------------------")
        print(f"found guest(s) with name {name}: {found}")
        save_search_history(name=name)  
    else:
        print("---------------------------")
        print("no guest found.")    

def find_by_serial_number(serial_number):
    index=serial_number-1
    if 0 <= index < len(guest_list):
        print("---------------------------") 
        print("a guest: ", guest_list[index])
        save_search_history(serial_number=serial_number)  
    else:
        print("---------------------------") 
        print("invalid index. no guest found.")            

def find_by_age(age):
    found = filter(lambda x: x[1] == age, guest_list)
    if found:
        print("---------------------------")
        print(f"found guest(s) with age {age}: {found}")
        save_search_history(age=age) 
    else:
        print("---------------------------")
        print("no guest found.")

def save_file(path, data):
    with open(path, "a") as file:
        file.write(data)

def save_search_history(name=None, age=None, serial_number=None):
    if name != None:
        result= f"search type: name -> {name} {datetime.datetime.now()}\n"
        save_file("search_history.txt", result)
    elif age != None:
        result= f"search type: age -> {age} {datetime.datetime.now()}\n"
        save_file("search_history.txt", result)
    elif serial_number != None:
        result= f"search type: by serial number -> {serial_number} {datetime.datetime.now()}\n"
        save_file("search_history.txt", result)

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
            name=input("name: ").capitalize() 
            delete_byname(name)
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
            name=input("name: ").capitalize()
            find_by_name(name)
            save_search_history(name)
        elif option3==2:
            print("---------------------------")  
            print("---find a guest from the guest list by serial number---")
            while True:
                try:
                    serial_number=int(input("num: "))
                    break
                except ValueError:
                    print("wrong input")
                    continue
            find_by_serial_number(serial_number)
            save_search_history(serial_number)
        elif option3==3:
            print("---------------------------")  
            print("---find a guest from the guest list by age---")
            while True:
                try:
                    age=int(input("age: "))
                    break
                except ValueError:
                    print("wrong input")
                    continue
            find_by_age(age)
            save_search_history(age)
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