import math

class Vector:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
    
    def __repr__(self):
        return f"Vector({self.v1}, {self.v2})"
    
    def __add__(self, other):
        return Vector(self.v1 + other.v1, self.v2 + other.v2)
    
    def __sub__(self, other):
        return Vector(self.v1 - other.v1, self.v2 - other.v2)
    
    def __mul__(self, scalar):
        return Vector(self.v1 * scalar, self.v2 * scalar)
    
    def __eq__(self, other):
        return self.v1 == other.v1 and self.v2 == other.v2
    
    def __len__(self):
        return round(math.sqrt(self.v1 ** 2 + self.v2 ** 2))
    
    def __getitem__(self, index):
        if index == 0:
            return self.v1
        elif index == 1:
            return self.v2
        else:
            raise IndexError("Index is not in range, use 0 for x and 1 for y")


v1 = Vector(7, 12)
v2 = Vector(2, 9)
print(v1)          
print(v1 + v2)     
print(v1 - v2)    
print(v1 * 3)   
print(v1 == Vector(2, 4)) 
print(len(v1))    
print(v1[0])     
print(v1[1])       
