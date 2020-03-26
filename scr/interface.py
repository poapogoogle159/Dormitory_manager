from dormitory import Dormitory
from room import Room

def login():
    username = input("Username : ")
    password = input("Password : ")
    with open("dormitory.txt",'r') as dormitory:
        for i in dormitory.readlines():
            username_check = i.split(',')[0]
            password_check = i.split(',')[1]
            if username == username_check and password == password_check:
                name = i.split(',')[2].strip()
                return name
        else:
            print("username or password faile")
    return login()


#main

name = login()
print(f'Profile : {name}')
text = 'home'
while True:
    dorm_user = Dormitory(name)
    def fn_search(operation1,opertor,operation2):
        Operator= {
            'more':lambda x1,x2: x1 > x2,
            'less':lambda x1,x2: x1 < x2,
            'equal':lambda x1,x2: x1 == x2
        }
        if operation1 == "number":
            return dorm_user.search(lambda room: Operator[opertor](room.getNumber(),operation2))
        elif operation1 == "floor":
            return dorm_user.search(lambda room: Operator[opertor](room.getFloor(),int(operation2)))
        elif operation1 == "price":
            return dorm_user.search(lambda room: Operator[opertor](room.getPrice(),int(operation2)))
        elif operation1 == "type":
            return dorm_user.search(lambda room: Operator[opertor](room.getType(),operation2))
        elif operation1 == "status":
            return dorm_user.search(lambda room: Operator[opertor](room.getStatus(),operation2))
        elif operation1 == "resident":
            return dorm_user.search(lambda room: Operator[opertor](room.getResident(),operation2))
        elif operation1 == "payment":
            return dorm_user.search(lambda room: Operator[opertor](room.getPayment(),int(operation2)))

    Stement = {
        'home':dorm_user.view,
        'add':dorm_user.add,
        'delete':dorm_user.delete,
        'payment':dorm_user.payment,
        'charge':dorm_user.charge,
        'history':dorm_user.history,
        'edit':dorm_user.edit,
        'search':fn_search
        }
    try:
        stement = text.split()[0]
        paramiter = text.split()[1:]
        Stement[stement](*paramiter)
    except Exception:
        print("Stement false!")
    text = input("  :")
    if text == 'exit':
        break

    




             
    