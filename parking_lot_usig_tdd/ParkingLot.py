import Vehicle


class ParkingLot:
    def __init__(self):
        self.capacity=0
        self.slot_id=0
        self.occupied_slot=0

    def create_parking_lot(self, capacity):
        self.slots=[-1] * capacity
        self.capacity=capacity
        return self.capacity

    def get_empty_slot(self):
        for i in range(len(self.slots)):
            if self.slots[i] == -1:
                return i

    def park(self, regno, color):
        if self.occupied_slot < self.capacity:
            slot_id=self.get_empty_slot()
            self.slots[slot_id]=Vehicle.Bike(regno, color)
            self.slot_id=self.slot_id + 1
            self.occupied_slot=self.occupied_slot + 1
            return slot_id + 1
        else:
            return -1

    def leave_slot(self, slot_id):
        if self.occupied_slot > 0 and self.slots[slot_id - 1] != -1:
            self.slots[slot_id - 1]=-1
            self.occupied_slot=self.occupied_slot - 1
            return True
        else:
            return False

    def check_status(self):
        print("Slot No \tRegistration No \tColor")
        for i in range(len(self.slots)):
            if self.slots[i] != -1:
                print(str(i + 1) + "\t" + str(self.slots[i].regno) + "\t" + str(self.slots[i].color))
            else:
                continue

    def show(self, line):
        if line.startswith('create_parking_lot'):
            n=int(line.split(' ')[1])
            res=self.create_parking_lot(n)
            print('Created a parking lot with ' + str(res) + ' slots')

        elif line.startswith('park'):
            regno=line.split(' ')[1]
            color=line.split(' ')[2]
            res=self.park(regno, color)
            if res == -1:
                print("parking lot is full")
            else:
                print('Allocated slot number: ' + str(res))
        elif line.startswith('leave_slot'):
            leave_slot_id=int(line.split(' ')[1])
            status=self.leave_slot(leave_slot_id)
            if status:
                print('slot number' + str(leave_slot_id) + 'is free')

        elif line.startswith('status'):
            self.check_status()


def main():
    parkinglot=ParkingLot()
    while True:
        line=input("$ ")
        parkinglot.show(line)


if __name__ == '__main__':
    main()
