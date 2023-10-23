#This exercise implies Class,Method and variables. __init__ is always used to define arguments and
# to asign them to the Self arguments variables.
#other method is defined to use the arguments of  __init__ method for the special prupose
class person:
    count=0
    def __init__(self,name,age,education):
        self.name=name
        self.age=age
        self.education=education
    def get_name(self):
        print('your name is %s' % self.name)
    def get_age(self):
        print('your age is %i' % self.age)
    def get_education(self):
        print('you have %s degree' % self.education)     

Meisam=person('Meisam',39,'MS')
Meisam.get_name()
Meisam.get_age()
Meisam.get_education()