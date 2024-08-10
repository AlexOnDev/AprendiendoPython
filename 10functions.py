### Functions ###

def my_function():
    print("Hola, esto es una función")

my_function()

def sum_two_values(a : int, b): # : int es para aconsejar al programador
    print(a + b)

sum_two_values(2,3)
sum_two_values("2","3")
sum_two_values(2.56,8.43)

def sum_two_values_with_return(a : int, b):
    my_sum = a + b
    return my_sum

my_result = sum_two_values_with_return(8,4)
print(my_result)
my_result = sum_two_values(8,5)
print(my_result)

def print_name(name, surname):
    print(f"{name} {surname}")

print_name(surname = "de Pablo", name = "Alejandro")

def print_name_with_default(name, surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Alejandro", "de Pablo")
print_name_with_default("Alejandro", "de Pablo", "Alejandro Corp.")

def print_texts(*texts):
    print(type(texts))
    for text in texts:
        print(text.upper())

print_texts("Hola", "eeee", "suuuu","aloh", "presidente")
print_texts("Hola")