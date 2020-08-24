class Himan:
    def __init__(self,age,name):
        self.age = age
        self.name = name
    
    def loo(self):
        print(self.age,self.name)
    
    def died(self):
        print(self.name,"has died")
        self

new_himan = Himan(11,"Himanshu")
new_himan.loo()
new_himan.died()
