class Calculstor:
    def show(self,x,y):
        print("overloading")
        return x+y
        
obj=Calculstor()
print(obj.show(2,3))
print(obj.show("t","s"))        
        