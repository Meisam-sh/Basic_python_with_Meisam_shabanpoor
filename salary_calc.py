def salary(s):
    x=s/12
    y=s/365
    z=s/365/7.3
    bime_1=x*0.3
    bime_2=x*0.07
    bime_3=bime_1-bime_2
    print('your mounthly income=',x,'your daily income=',y,z,bime_1,bime_2,bime_3)
#main program
sal=int(input('enter your anual agreement as income: '))
salary(sal)