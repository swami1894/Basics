class Temperature:

    temp_in_fahrenheit = None

    def __init__(self, fahrenheit:float) -> None:

        self.__class__.temp_in_fahrenheit = fahrenheit


    @classmethod
    def to_celcius(Temperature):
        celcius = ((Temperature.temp_in_fahrenheit - 32)*5)/9
        return round(celcius, 2)
    

temp = Temperature(31)

print(temp.to_celcius())
