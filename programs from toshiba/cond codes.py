hours=raw_input('enter hours:')
f=float(hours)
if f<=40.0:
    rate=10.0
    pay = f*rate
    print pay
else:
    pay=(40.0*10.0)+(f-40.0)*15.0
    print pay
