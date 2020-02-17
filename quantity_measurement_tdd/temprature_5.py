from calculation_formulas import Formulas

cal = Formulas()


class TemprConversion:
    def __init__(self):
        self.fara = 0.0
        self.cel = 0.0

    def convert_cel_into_fara(self, cel):
        self.fara = cal.convert_temp_into_fahrenheit(temp=cel)
        return self.fara

    def convert_fara_into_celcius(self, fara):
        self.cel = cal.convert_temp_into_celcius(fara=fara)
        return self.cel