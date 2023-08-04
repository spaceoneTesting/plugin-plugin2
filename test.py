




class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age




    def __del__(self):
        print(f'Object is being deconstructed!')



    def add(self, a, b):
        return a + b










p = Person("Mike", 25)
del p
