from calculation_formulas import Formulas

cal = Formulas()


class ComapareLengths:
    def __init__(self):
        self.feet = 0.0
        self.yards = 0.0
        self.inch = 0.0
        self.cm = 0.0

    def convert_feet_into_inch(self, feet):
        self.feet = feet
        self.inch = cal.convert_feet_into_in(feet=self.feet)
        return self.inch

    def convert_feet_into_yards(self, feet):
        self.feet = feet
        self.yards = cal.convert_feet_into_yd(feet=self.feet)
        return self.yards

    def convert_inch_into_feet(self, inch):
        self.inch = inch
        self.feet = cal.convert_inch_into_ft(inch=self.inch)
        return self.inch

    def convert_inch_into_yards(self, inch):
        self.inch = inch
        self.yards = cal.convert_inch_into_yd(inch=self.inch)
        return self.yards

    def convert_yards_into_inch(self, yards):
        self.yards = yards
        self.inch = cal.convert_yards_into_in(yards=self.yards)
        return self.inch

    def convert_yards_into_feet(self, yards):
        self.yards = yards
        self.feet = cal.convert_yards_into_ft(yards=self.yards)
        return self.feet

    def convert_inch_into_cm(self, inch):
        self.inch = inch
        self.cm = cal.convert_inch_into_cm(inch=self.inch)
        return self.cm

    def add_inches(self, inch1, inch2):
        self.inch = cal.additions_of_two_values(var1=inch1, var2=inch2)
        return self.inch

    def add_feet_and_inch(self, feet, inch):
        in_result = cal.convert_feet_into_in(feet=feet)
        self.inch = cal.additions_of_two_values(var1=in_result,var2=inch)
        return self.inch

    def add_feet_and_get_inch(self, feet1, feet2):
        self.inch = cal.convert_feet_into_inch_add(feet1=feet1, feet2=feet2)
        return self.inch

    def add_inch_and_cm_get_inch(self, inch, cm):
        in_result = cal.convert_cm_into_inch(cm=cm)
        self.inch = cal.additions_of_two_values(var1=inch, var2=in_result)
        return self.inch
