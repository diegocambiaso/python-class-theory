# classes

class Person:
    # atributos de classes
    data = "La altura es en centímetros y el peso es en kilogramos."
    count = 0
    
    # atrubutos de instancia
    def __init__(self, name, height, weight):
        # Instance attributes
        self.name = name  
        self.height = height
        self.weight = weight
        Person.count += 1

    @classmethod 
    def show(cls):
        return cls.data
    
    @staticmethod
    def info():
        return "Método estático"

    # methods (behaviours)
    def studying(self, course): # método de instancia
        return ("{} está estudiando {}".format(self.name, course))


# instnaciando clases (crenado objetos)
diego = Person("Diego", 178, 40)
mechy = Person("Mercedes", 170, 41)

print("Persons: ", Person.count)
# trabajando con métodos
print(f"{diego.name}")
print(f"Altura: {diego.height} centímetros.")
print(f"Peso: {diego.weight} kilogramos.")
print(diego.studying("Dart"))
print(diego.show(), "\n")

# trabajando con atributos de clases
Person.data = "La altura es en centímetros (cm) y el peso es en kilogramos (km)."

print(f"{mechy.name}")
print(f"Altura: {mechy.height} centimetros.")
print(f"Peso: {mechy.weight} kilogramos.")
print(mechy.studying("Python"))
print(mechy.show(), "\n")

# Silvi
silvi = Person("Silvina", 174, 42)

print("Persons: ", Person.count)
print(f"{silvi.name}")
print(f"Altura: {diego.height} centimetros.")
print(f"Peso: {silvi.weight} kilogramos.")
print(silvi.studying("Flutter"))
print(silvi.show(), "\n")
