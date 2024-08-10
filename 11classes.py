### Classes ###

class MyEmptyPerson:
    pass # Para poner vacia la clase sin error

print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:
    def __init__(self, name, surname, alias = "Sin alias"): # Método constructor
        self.full_name = f"{name} {surname} ({alias})" # Propiedad pública
        self.__name = name # Propiedad privada
        self.__surname = surname

    def get_name(self): # Getter enmascarado en una función
        return self.__name
    def walk(self):
        print(f"{self.full_name} está caminando")

my_person = Person("Alejandro", "de Pablo")
print(my_person.full_name)
my_person.walk()

my_other_person = Person("Alejandro", "de Pablo", "Alejandro Corp")
print(my_other_person.full_name)
my_other_person.walk()

my_other_person.full_name = "Michael \"The Goat\" Jordan"
print(my_other_person.full_name)

my_other_person.full_name = 888
print(my_other_person.full_name)

print(my_other_person.get_name())