### Tuples ###

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (22, 1.86, "Alejandro","de Pablo", "Alejandro")
my_other_tuple = (35, 60, 11, 20, 11)
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
# print(my_tuple[4]) IndexError
# print(my_tuple[-6]) IndexError

print(my_tuple.count("Alejandro"))
print(my_tuple.index("de Pablo"))

# my_tuple[5] = 1.50 'tuple' object does not support item assignment
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple[3:6])

# Asignar nuevos valores transformando a List
my_tuple = list(my_tuple) 
print(type(my_tuple))

my_tuple[4] = "Alejandro Corp."
my_tuple.insert(1,"Papaya")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

# del my_tuple[2] TypeError: 'tuple' object doesn't support item deletion

del my_tuple
# print(my_tuple) NameError: name 'my_tuple' is not defined
