class Father:
    def skills(self):
        print("gardening")
class Mother:
    def skills(self):
        print("cooking")
class Child(Father,Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
    pass
obj=Child()
obj.skills()    
#obj.skills()                