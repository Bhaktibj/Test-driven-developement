from calculation_formulas import Formulas

cal = Formulas()


class CompareVolumes:
    def __init__(self):
        self.liter = 0.0
        self.gallon = 0.0
        self.ml = 0.0

    def get_ml_liter(self, ml):
        self.ml = ml
        return self.ml

    def convert_gallons_liter(self, gallons):
        self.liter = cal.convert_gallons_into_ltr(gallons=gallons)
        return self.liter

    def convert_liters_to_ml(self, liter):
        self.ml = cal.convert_liter_into_ml(liter=liter)
        return self.ml

    def additions_of_gallon_and_ltr(self, gallon, liter2):
        liter1 = cal.convert_gallons_into_ltr(gallons=gallon)
        self.liter = cal.additions_of_two_values(var1=liter1, var2=liter2)
        return self.liter

    def additions_of_liter_and_ml(self, liter1, ml):
        liter2 = cal.convert_ml_into_liter(ml=ml)
        self.liter = cal.additions_of_two_values(var1=liter1, var2=liter2)
        return self.liter
