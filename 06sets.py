### Sets ###

my_set= set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # Inicialmente es un diccionario

my_other_set = {"Alejandro","de Pablo", 22}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("Alejandro Corp.")
print(my_other_set) # Set != ordenado

my_other_set.add("Alejandro Corp.") # Un set no admite repetidos
print(my_other_set)

print("Alejandro" in my_other_set)
print("Alejandri" in my_other_set)

my_other_set.remove("Alejandro")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set

my_set = {"Alejandro","de Pablo", 22}
my_list=list(my_set)
print(my_list)
print(my_list[0])

my_other_set ={"Kotlin","Swift","Python"}

my_new_set = my_set.union(my_other_set)
print(my_new_set.union({"JavaScript","C#"}))

print(my_new_set.difference(my_set))
print(my_new_set)
