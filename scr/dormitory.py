from room import Room
from datetime import date,datetime

today = date.today()
time = datetime.now()

class Dormitory:
    def __init__(self,name):
        self.name = name
        self.room = {}
        with open(f"{self.name}.txt","r") as file:
            for dataroom in file.readlines():
                eachRoom = dataroom.strip().split("-")
                self.room.update({f"{eachRoom[0]}":Room(self.name,eachRoom[0],eachRoom[1],eachRoom[2],eachRoom[3],eachRoom[4],eachRoom[5],eachRoom[6])})

    def add(self,roomnumber,resident_name):
        if self.room[roomnumber].getStatus() == "empty":
            self.room[roomnumber].setStatus("notempty")
            self.room[roomnumber].setResident(resident_name)
            with open(f"{self.name}_add.txt","a+") as history_add:
                history_add.write(f'{resident_name}-{roomnumber}-{today.strftime("%d/%m/%Y")}')
                history_add.write('\n')          
        else:
            print("this room not empty")
    
    def delete(self,roomnumber):
        if self.room[roomnumber].getStatus() == "notempty":
            resident_name = self.room[roomnumber].getResident()
            self.room[roomnumber].setStatus("empty")
            self.room[roomnumber].setResident("empty")
            with open(f"{self.name}_delete.txt","a+") as history_delete:
                history_delete.write(f'{resident_name}-{roomnumber}-{today.strftime("%d/%m/%Y")}')
                istory_delete.write('\n')
        else:
            print("this room empty")

    def edit(self,numberroom,changeEdit,new_value):
        edit_dic = {
            "number":self.room[numberroom].setNumber,
            "floor":self.room[numberroom].setFloor,
            "price":self.room[numberroom].setPrice,
            "status":self.room[numberroom].setStatus,
            "type":self.room[numberroom].setType,
            "resident":self.room[numberroom].setResident,
            "payment":self.room[numberroom].setPayment
        }
        if changeEdit in ['floor','price','payment']:
            edit_dic[changeEdit](int(new_value))
        else:
            edit_dic[changeEdit](new_value)

    def payment(self,roomnumber,money):
        money = int(money)
        if self.room[roomnumber].getPayment() > 0:
            if money - self.room[roomnumber].getPayment() >= 0:
                change = money - self.room[roomnumber].getPayment()
                self.room[roomnumber].setPayment(0)
                print("change :",change)
            else:
                payment = self.room[roomnumber].getPayment()- money
                self.room[roomnumber].setPayment(payment)
                print("payment :",payment)
            with open(f"{self.name}_payment.txt","a+") as history_paymeny:
                payment = self.room[roomnumber].getPayment() - money if self.room[roomnumber].getPayment() > money else 0
                history_paymeny.write(f'{self.room[roomnumber].getResident()}-{roomnumber}-{today.strftime("%d/%m/%Y")}-{money}')
                history_paymeny.write('\n')
        else:
            print("this room not problem")

    def charge(self,roomnumber,money):
        money = int(money)
        payment_old = self.room[roomnumber].getPayment()
        payment_new = payment_old + money
        self.room[roomnumber].setPayment(payment_new)
        print(f"Room {roomnumber} : {payment_new}")

    def history(self,topic):
        with open(f'{self.name}_{topic}.txt','r') as Reader:
            for data in Reader.readlines():
                print(data)

    def search(self,fn):
        for i in self.room:
            if fn(self.room[i]):
                self.room[i].view()

    def view(self):
        for data in self.room:
            self.room[data].view()


    
        
                


            
            
        


