class Animal:
    def __init__(self):
        self.hungry = 5
        
    def timegoby(self):
        if self.hungry > 0:
            self.hungry -= 1
    
    def manttang(self):
        self.hungry = 10



ani = Animal()
print("Animal :",ani.hungry)
ani.timegoby()
print("Animal :",ani.hungry)
ani.manttang()
print("Animal :",ani.hungry)
print()


class Human(Animal):
    def __init__(self):
        super().__init__()
        self.skill_lang = 0
        
    def momstouch(self, stroke):
        self.skill_lang += stroke
        

hum = Human()
print("Human :",hum.hungry)
print("Human :",hum.skill_lang)
hum.timegoby()
hum.momstouch(5)
print("Human :",hum.hungry)
print("Human :",hum.skill_lang)





