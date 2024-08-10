### Lists ###

my_list = list()
my_other_list = [] # También es una lista

print(len(my_list))

my_list = [35, 24, 65, 30, 30, 16]

print(my_list)
print(len(my_list))

my_other_list = [22, 1.86, "Alejandro", "de Pablo"]

print(type(my_list))
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])
print(my_list.count(30))


#ERROR age, height, name = my_other_list
age, height, name, surname = my_other_list 
print(name)

print(my_other_list + my_list)
#print(my_other_list - my_list)

my_other_list.append("Alejandro Corp.")
print(my_other_list)

my_other_list.insert(1,"Mango")
print(my_other_list)

my_other_list[1] = "Papaya"
print(my_other_list)

my_other_list.remove("Papaya") # Elimina por valor y primer valor encontrado
print(my_other_list)

my_list.remove(30)
print(my_list)

my_pop_element = my_list.pop(2) # Elimina por indice o el último de la lista
print(my_pop_element)
print(my_list)

del my_list[2] # No retorna el valor
print(my_list)

my_new_list = my_list.copy()

my_list.clear()
print(my_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

print(my_new_list[1:3])

my_list = "Hola Python"
print(my_list)
print(type(my_list))
