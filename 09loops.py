### Loops ###

# While

my_condition = 0
while my_condition < 10:
    print(my_condition)
    my_condition+=2
else: # Es opcional
    print("Mi condición es mayor o igual que 10")
    my_condition = 0 # No lo hace infinito, el bucle ya ha finalizado
print("Fuera while")

while my_condition < 20:
    my_condition+=1
    if(my_condition == 15):
        print("Es igual a 15")
        break
    print(my_condition)
print("Fuera del while 2")

# For

my_list = [35, 24, 65, 30, 30, 16]
my_tuple = (22, 1.86, "Alejandro","de Pablo", "Alejandro")
my_other_set = {"Alejandro","de Pablo", 22}
my_other_dict = {"Nombre":"Alejandro", "Apellido":"de Pablo","Edad":22, 1:"Python"}


for element in my_list:
    print(element)
for element in my_tuple:
    print(element)
for element in my_other_set:
    print(element)
for element in my_other_dict:
    print(element)
    if element == "Edad":
        continue
    print("elemento " + str(element))
else:
    print("El bucle for para dict ha finalizado")