class Formulas:

    # common method
    @staticmethod
    def additions_of_two_values(var1, var2):
        in_sum = var1 + var2
        return in_sum

    @staticmethod
    def convert_feet_into_in(feet):
        in_result = feet * 12
        return in_result

    @staticmethod
    def convert_feet_into_yd(feet):
        yd_result = feet / 3
        return yd_result

    @staticmethod
    def convert_inch_into_ft(inch):
        ft_result = inch / 12
        return ft_result

    @staticmethod
    def convert_inch_into_yd(inch):
        ft_result = inch / 12
        yd_result = ft_result / 3
        return yd_result

    @staticmethod
    def convert_yards_into_in(yards):
        in_result = yards * 3 * 12
        return in_result

    @staticmethod
    def convert_yards_into_ft(yards):
        ft_result = yards * 3
        return ft_result

    @staticmethod
    def convert_inch_into_cm(inch):
        cm_result = inch / 0.39370
        return cm_result

    @staticmethod
    def convert_cm_into_inch(cm):
        in_result = cm * 0.39370
        return in_result

    @staticmethod
    def convert_feet_into_inch_add(feet1, feet2):
        in_sum = (feet1 * 12) + (feet2 * 12)
        return in_sum

    # volumes formulas ********************************************

    @staticmethod
    def convert_gallons_into_ltr(gallons):
        liters = gallons * 3.78
        return liters

    @staticmethod
    def convert_liter_into_ml(liter):
        ml = liter * 1000
        return ml

    @staticmethod
    def convert_ml_into_liter(ml):
        liter = ml / 1000
        return liter

    # weights formulas ********************************************

    @staticmethod
    def convert_kg_into_grams(kg):
        grams = kg * 1000
        return grams

    @staticmethod
    def convert_grams_into_kg(grams):
        kgs = grams / 1000
        return kgs

    @staticmethod
    def convert_tonne_into_kg(tonne):
        kgs = tonne * 1000
        return kgs

    # Temprature conversion

    @staticmethod
    def convert_temp_into_fahrenheit(temp):
        fahrenheit = (temp * 9 / 5) + 32
        print(fahrenheit)
        return fahrenheit

    @staticmethod
    def convert_temp_into_celcius(fara):
        celcius = (fara - 32) * 5 / 9
        return celcius
