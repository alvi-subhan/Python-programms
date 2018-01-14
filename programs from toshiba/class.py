class PartyAnimal:
    x=0
    def Party(self):
        self.x=self.x+1
        print 'so far',self.x
an=PartyAnimal()
print 'Type',type(an)
print dir(an)
