#dar in file lambda func ha ra dar map va filter estefadeh mikonim 
#nokteye mohem in ast ke har ja lambda func estefadeh shodeh  mishavad be jaye an func mamooli ham nevesht yani ba Def
#
#tamrin daryafte list az voroodi va joda sazi bar asase Space ba tabe@e split()
input_name=input('Enter the list of elements separate with space you want to assess: \n')
element_list=input_name.split()
print(element_list)
# tamrin map baraye shenakhte jensiat esme har element list dar 'people'
people=['mrs sofia','mrs sanaz','mr meisam','mr mehran','mrs sahar','mr hosein','mrs sara','mr mehdi']
gender=list(map(lambda x: 'Woman' if x[:3]=='mrs' else 'Man',people))
#tamrin filter baraye filter kardane mardan az list gender
just_man=list(filter(lambda x: x=='Man',gender))
print(people)
print(people[:2])
print(gender)
print(just_man)