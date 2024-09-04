letters='aeiouAEIOU'
def hazf_bseda(x):
    for i in range(0,len(letters)-1):
        if letters[i] in x:
            y=x.replace(x[x.find(letters[i])],'')
            x=y
    return x
def lowercase(z):
    l=z.lower()
    return l
def insertdot(k):
    v=''
    for f in range(0,len(k)):
        v=v+'.'+k[f]
    return v
x=input()
z=hazf_bseda(x)
w=lowercase(z)
k=insertdot(w)
print(k)