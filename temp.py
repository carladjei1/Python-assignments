class Tempreture:
    def __init__(self,value):
        self.tempreture = value
    def Celsius_to_Farenheit(self):
        print( (self.tempreture-32)*5/9 )

    def Farenheit_to_Celsius(self):
        print( (self.tempreture*9/5)+32 )

c= Tempreture(100)

c.Farenheit_to_Celsius()
    
