class staff():
    count=0
    def __init__(self,firstname,lastname,unit,level): # this method is constractor
        staff.count+=1
        self.fname=firstname
        self.lname=lastname
        self.unit=unit
        self.level=level
    def position(self):
        return 'Manager' if self.level=='1' else 'Expert'
    def __del__(self):  #this method is deconstractor
        staff.count-=1
    class FullTimeStaff(staff):
        def sal(self):
            pass
        print('%s salary is %i Dollar',self)
emp=input('enter the list of firstname,lastname,unit,level separated by Space: ')
employment=emp.split()
employee=staff(*employment)
print(employment)
print(employee.position())
Meisam=Full