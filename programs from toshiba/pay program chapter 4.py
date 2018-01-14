hours=raw_input('enter hours:')
rate=raw_input('enter rate:')
fhours=float(hours)
frate=float(rate)
def product(fhours,frate):
    if fhours<=40:
        pay=fhours*frate
	return pay
        pay=product(fhours,frate)
        print pay
    else:
        pay=(40.0*frate)+(frate*1.5*(fhours-40))
        return pay
        print pay
