from calculation_formulas import Formulas

cal = Formulas()


class CompareWeights:
    def __init__(self):
        self.grams = 0.0
        self.kg = 0.0
        self.tonne = 0.0

    def convert_kg_into_grams(self, kg):
        self.grams = cal.convert_kg_into_grams(kg=kg)
        return self.grams

    def convert_grams_into_kg(self, grams):
        self.kg = cal.convert_grams_into_kg(grams=grams)
        return self.kg

    def convert_tonne_into_kg(self, tonne):
        self.tonne = cal.convert_tonne_into_kg(tonne=tonne)
        return self.tonne

    def add_tonne_into_grams_get_kg(self, tonne, gram):
        kg1 = cal.convert_tonne_into_kg(tonne=tonne)
        kg2 = cal.convert_grams_into_kg(grams=gram)
        self.kg = cal.additions_of_two_values(var1=kg1, var2=kg2)
        print(self.kg)
        return self.kg
