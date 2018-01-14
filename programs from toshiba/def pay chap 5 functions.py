input = raw_input('enter hours;')
rate=raw_input("enter rate:")
fh=float(input)
fr=float(rate)
v=40
x= v*10.50
y=(fh-v)*(1.5*10.50)
def product(fh,fr):
    multi=fh*fr
    return multi
if fh<=40:
    pay=product(fh,fr)
    print pay
else:
    def p40(x,y):
        add= x+y
        return add
    pay= p40(x,y)
    print pay


    
