class Room:
    def __init__(self,dormitory, number, floor, price, typeroom, status="empty", resident="empty",payment=0):
        self.dormitory = dormitory
        self.__data = {
            "number": number,
            "floor": int(floor),
            "price": int(price),
            "type": typeroom,
            "status": status,
            "resident": resident,
            "payment": int(payment)
        }
    def view(self):
        for i in self.__data:
            print(i, ":", self.__data[i], end='  ')
        print('\n')
        
    def setroom(edit):
        def setdata(self, value):
            dic= {"number":0,"floor":1,"price":2,"type":3,"status":4,"resident":5,"payment":6}
            with open(f'{self.dormitory}.txt','r') as room:
                file_room = [x.strip().split('-') for x in room.readlines()]
            with open(f'{self.dormitory}.txt','w') as room:
                for i in range(len(file_room)):
                    if file_room[i][dic['number']] == self.__data['number']:
                        file_room[i][dic[edit]] = str(value)
                    room.write('-'.join(file_room[i]))
                    room.write('\n')
            self.__data[edit] = value
        return setdata

    def getroom(get):   
        def getdata(self):
            return self.__data[get]
        return getdata

    setNumber = setroom("number")
    getNumber = getroom("number")
    setFloor = setroom("floor")
    getFloor = getroom("floor")
    setType = setroom("type")
    getType = getroom("type")
    setPrice = setroom("price")
    getPrice = getroom("price")
    setStatus = setroom("status")
    getStatus = getroom("status")
    setResident = setroom("resident")
    getResident = getroom("resident")
    setPayment = setroom("payment")
    getPayment = getroom("payment")

