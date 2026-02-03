# Basic class defination and object-oriented programming concepts in Python
# ============================================================================
# 1. BASIC CLASS DEFINITION
# ============================================================================

class person:
    #calss variable
    species = "humans"
    
    #constructor
    def __init__(self,name,age):
        self.name = name
        self.age =age
        
    #instance method
    def introdeuction(self):
        return f"hello , may name is {self.name} and i am {self.age} years old."
    
    def birthday(self):
        self.age +=1
        return f"happy birthday {self.name}! you are now {self.age} years old."

#creating object
person1 = person("anuradha",22)
person2 = person("radha",25)
    

