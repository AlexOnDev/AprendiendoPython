### File Handling ###
import os
# .txt file

txt_file = open("Intermediate/my_file.txt","w+") # r+ para leer y escribir. Si w+ lo sobreescribe

txt_file.write("Alejandro\nde Pablo\n22 años\nPython")

txt_file.seek(0)

# print(txt_file.read())
print(txt_file.read(10).strip()) # strip() elimina el espacio posterior
print(txt_file.readline().strip())
print(txt_file.readline().strip())
for line in txt_file.readlines():
     print(line.strip())

# Guarda la posición del puntero antes de escribir la nueva línea
posicion_anterior = txt_file.tell()

# Escribe más contenido al archivo
txt_file.write("\nNo me gusta Python")
txt_file.flush()  # Asegura que el contenido se escriba en el archivo

# Mueve el puntero de vuelta a la posición donde se escribió la nueva línea
txt_file.seek(posicion_anterior)

# Lee desde la posición donde se encuentra el puntero después de la nueva escritura
# (esto lee desde el final del archivo original hasta el nuevo contenido)
contenido_restante = txt_file.read().strip()
print(contenido_restante)  # Imprime el contenido restante, incluyendo la nueva línea


txt_file.close()

with open("Intermediate/my_file.txt", "a") as my_other_file:
    my_other_file.write("\nNi JavaScript")

# os.remove("Intermediate/my_file.txt")

# .json file
