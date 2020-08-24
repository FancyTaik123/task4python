class glue:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def drink_glue(self):
        print("{} ({}) has just dranked glue!".format(self.name,self.age))

new_glue = glue()