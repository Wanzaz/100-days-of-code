# Inheritance

class Animal:
    def __init__(self):
        self.num_eyes = 2
    
    def breathe(self):
        print("Inhale, exhale.")

class Fish(Animal): # Inheritancing Animal
    def __init__(self):
        super().__init__() # all atributes and methods

    def breathe(self):
        super().breathe()
        print("doing this underwater")

    def swim(self):
        print("moving in water.")

nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)
