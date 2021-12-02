class Temperature:
    def __init__(self, kelvin=None, celsius=None, fahrenheit=None):
        if kelvin is not None:
            self.kelvin = kelvin
        elif celsius is not None:
            self.celsius = celsius
        elif fahrenheit is not None:
            self.fahrenheit = fahrenheit
        else:
            self.kelvin = 0
            raise ValueError("Need to specify at least one unit")

    def __repr__(self):
        return f"<{self.kelvin:g}K == {self.celsius:g}°C == {self.fahrenheit:g}F"

    def __str__(self):
        return f"{self.kelvin:g}"

    


