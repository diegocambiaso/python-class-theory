# classes

class Person:
    # class attributes
    data = "Height is centimeters and weight is in kilograms."
    count = 0
    
    # session attributes
    def __init__(self, name, height, weight):
        # Instance attributes
        self.name = name  
        self.height = height
        self.weight = weight
        Person.counter += 1

    @classmethod 
    def show(cls):
        return cls.data
    
    @staticmethod
    def info():
        return "Static method"

    # methods (behaviours)
    def studying(self, course): # instance method
        return ("{} is stydying {}".format(self.name, course))


# instancing class (creating objects)
diego = Person("Diego", 178, 40)
mechy = Person("Mercedes", 170, 41)

print("Persons: ", Person.counter)
# working with methods
print(f"{diego.name}")
print(f"Height: {diego.height} centimeters.")
print(f"Weight: {diego.weight} kilograms.")
print(diego.studying("Dart"))
print(diego.show(), "\n")

# workin with class attributes
Person.data = "Height is centimeters (cm) and weight is in kilograms (kg)."

print(f"{mechy.name}")
print(f"Height: {mechy.height} centimeters.")
print(f"Weight: {mechy.weight} kilograms.")
print(mechy.studying("Python"))
print(mechy.show(), "\n")

# Silvi person
silvi = Person("Silvina", 174, 42)

print("Persons: ", Person.counter)
print(f"{silvi.name}")
print(f"Height: {diego.height} centimeters.")
print(f"Weight: {silvi.weight} kilograms.")
print(silvi.studying("Flutter"))
print(silvi.show(), "\n")
