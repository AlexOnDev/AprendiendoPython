### Error Types ###

# Syntax Error
#print "Aloo" # Descomentar para Error
print("Aloo")

# Name Error
language = "Spanish" # Comentar para Error
print(language)

# Index Error
my_list = ["Python", "Swift", "Kotlin", "Dart", "JavaScript"]
print(my_list[0])
print(my_list[4])
print(my_list[-1])
#print(my_list[5]) # Descomentar para Error

# ModuleNotFoundError
#import maths # Descomentar para Error
import math

# AttributeError
#print(math.PI) # Descomentar para Error
print(math.pi)

# KeyError
my_dict = {"Nombre":"Alejandro", "Apellido":"de Pablo","Edad":22, 1:"Python"}
print(my_dict["Edad"])
#print(my_dict["Apelido"]) # Descomentar para Error

# TypeError
#print(my_list["1"]) # Descomentar para Error
print(my_list[1])
print(my_list[False]) # 0
print(my_list[True]) # 1

# ImportError
#from math import PI # Descomentar para Error
from math import pi
print(pi)

# ValueError
#my_int = int("10 Años") # Descomentar para Error
my_int = int("10")
print(type(my_int))

# ZeroDivisionError
#print(10/0) # Dividiendo por 0, espabila niño
