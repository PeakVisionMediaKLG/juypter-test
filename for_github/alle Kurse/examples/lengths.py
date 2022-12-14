class Length:

    __metric = {"mm" : 0.001, 
                "cm" : 0.01, 
                "m" : 1, 
                "km" : 1000,
                "in" : 0.0254, 
                "ft" : 0.3048, 
                "yd" : 0.9144,
                "mi" : 1609.344 }

    def __init__(self, value, unit="m"):
        self.value = value
        self.unit = unit

    def convert(self, target_unit="m"):
        if self.unit == target_unit:
            value = self.value
        else:
            value = self.value * Length.__metric[self.unit]
            value /= Length.__metric[target_unit]
        return value

    def __add__(self, other):
        if type(other) == int or type(other) == float:
            value = self.value + Length(other).convert(self.unit) 
        else:  
            if self.unit == other.unit:
                value = self.value + other.value
            else:
                value = self.value + other.convert(self.unit)
        return Length(value, self.unit)

    def __iadd__(self, other):
        if self.unit == other.unit:
            self.value = self.value + other.value
        else:
            self.value = self.value + other.convert(self.unit)
        return self
    
    def __radd__(self, other):
        z = self + other
        z.unit = "m"
        z.value *= Length.__metric[self.unit]
        return z


    def __str__(self):
        return str(self.value) + " " + self.unit 

    def __repr__(self):
        return 'Length(' + str(self.value) + ', "' + self.unit + '")'

    def __eq__(self, other):
        return self.value == other.value and self.unit == other.unit
