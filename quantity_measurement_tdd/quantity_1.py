

class Quantity:
    def __init__(self):
        self.quantity = 0
        self.weight_1 = 0
        self.weight_2 = 0
        self.total_weight_1 = 0
        self.total_weight_2 = 0

    def get_number_of_quantity(self, quantity):
        self.quantity = quantity
        return self.quantity

    def quantity_measurement(self, weight_1, weight_2):
        self.weight_1 = weight_1
        self.weight_2 = weight_2
        self.total_weight_1 = self.quantity * self.weight_1
        self.total_weight_2 = self.quantity * self.weight_2
        print(self.total_weight_1, self.total_weight_2)
        if self.total_weight_1 != self.total_weight_2:
            print("Number of quantity is same: but measurement is diff")
            return True
        else:
            print("Number of quantity & measurement is same ")
            return True


