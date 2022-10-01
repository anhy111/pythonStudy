class Byden:
    def __init__(self):
        self.ac = 10
        
    def makewar(self):
        self.ac -= 1
        
class Putin:
    def __init__(self):
        self.nuclear = 6660
    
    def altzheimer(self):
        self.nuclear -= 1
        
class Mugun(Byden, Putin):
    def __init__(self):
        Byden.__init__(self)
        Putin.__init__(self)
        self.bibitan = 100
    
    
        
mu = Mugun()

print("ac : ",mu.ac)
print("nuclear : ",mu.nuclear)
mu.makewar()
mu.altzheimer()
print("ac : ",mu.ac)
print("nuclear : ",mu.nuclear)