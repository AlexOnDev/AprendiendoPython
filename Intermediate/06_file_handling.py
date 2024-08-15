### File Handling ###
import os
# .txt file

txt_file = open("Intermediate/my_file.txt","w+") # r+ para leer y escribir. Si w+ lo sobreescribe

txt_file.write("Alejandro\nde Pablo\n22 años\nPython")

txt_file.seek(0)

# print(txt_file.read())
print(txt_file.read(10)) # Lectura funciona con punteros
print(txt_file.readline())
print(txt_file.readline())
for line in txt_file.readlines():
     print(line.strip())

posicion_anterior = txt_file.tell() # El final del archivo antes de escribir "No me gusta Python"

txt_file.write("\nNo me gusta Python")
txt_file.flush()

txt_file.seek(posicion_anterior + 2) # El + 2 porque no cuenta el cambio de linea e imprime vacio
print(txt_file.readline())  # Lee la nueva línea escrita

txt_file.close()

with open("Intermediate/my_file.txt", "a") as my_other_file:
    my_other_file.write("\nNi JavaScript")

# os.remove("Intermediate/my_file.txt")

# .json file
