class solar_system:
    count=0
    def __init__(self,name,weather,atmosphere,self_brightness):
        self.name=name
        self.weeather=weather
        self.atmosphere=atmosphere
        self.self_brightness=self_brightness
    def living_possibility(self):
        ox='oxygen'
        if  ox in self.atmosphere:
            print('this planet can have the living possibility')
        else:
            print('This planet does not have the living possibility')
somthing=input('enter the set of name,weather,atmosphere,self_brightness separated by Space: ')
info=somthing.split() #Split use each word as a filed and make a list with thoes fields
solar_system_sample=solar_system(*info)  # by using *info we parse fiels of the info list with their order to the Solar system class
solar_system_sample.living_possibility()
print(info)