### Variables ###

my_string_variable = "My String Variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_bool_variable = False
print(my_bool_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

# Concatenación de variables en un print
print(my_string_variable,my_int_variable, my_bool_variable)
print(type(print(my_string_variable,my_int_variable, my_bool_variable))) # print = NoneType
print("Est es el valor de: ", my_bool_variable)

# Algunas funciones del sistema
print(len(my_string_variable))

# Variables en una sola línea (esto deberia de ser ilegal)
name, surname, alias, age= "Alejandro", "de Pablo", "AlexOnDev", 22
print(name, surname, alias, age)

# Inputs
# name = input("¿Cual es tu nombre? ")
# age = input("¿Cuantos años tienes? ")
# print(name)
# print(age)

# ¿Forzamos el tipo?
address: str = "Mi direccion"
address = 32
print(type(address))