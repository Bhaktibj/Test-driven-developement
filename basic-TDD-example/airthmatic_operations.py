number_type=(int, float, complex)


class AirthmaticOperations:

    @staticmethod
    def valid_arguments(num1, num2):
        if not isinstance(num1, number_type) and not isinstance(num2, number_type):
            raise ValueError

    def addition(self, num1, num2):
        self.valid_arguments(num1=num1, num2=num2)
        print("Addition of two numbers is: ", num1 + num2)
        return num1 + num2

    def substraction(self, num1, num2):
        self.valid_arguments(num1=num1, num2=num2)
        print("Substraction of two numbers is: ", num1 - num2)
        return num1 - num2

    def multiplication(self, num1, num2):
        self.valid_arguments(num1=num1, num2=num2)
        print("Multiplication of two numbers is: ", num1 * num2)
        return num1 * num2

    def division(self, num1, num2):
        self.valid_arguments(num1=num1, num2=num2)
        print("Division of two numbers is: ", num1 / num2)
        return num1 / num2
