# generator exercise for yield 
# we use yield insted of Return when we want to return unlimited number based on iterators
#yeild use memory less than return because it returns out put and remember the function
def even_elements(n):
    i=0
    while i<=n:
        yield i if i%2==0 else 'odd'
        i+=1
x=int(input('eneter a digit for the number of elements in series: '))
print(even_elements(x))
for i in even_elements(x):
    print(i)
