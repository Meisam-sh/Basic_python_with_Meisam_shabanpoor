class device():
    count=0
    def __init__(self,name,ip,mac):
        self.name=name        
        self.ip=ip
        self.mac=mac
        device.count+=1#it means that if our init functioan(as a constractor) has been called count=count+1
        #result= ping the device #(this is sudoCode(shebheh code)) the result is not defined which can be a function
        #if result:
         #   self.status='active' #status is defiend here as an atribute
        #else:
         #   self.status='deactive'
class tv(device):
    def turn_on(self):
        # connect to self.ip and turn on
        pass #it does nothing
    def turn_off(self):
        # connect to self.ip and turn off
        pass
meisam=tv('sony','192.168.1.1','13554654884466')
