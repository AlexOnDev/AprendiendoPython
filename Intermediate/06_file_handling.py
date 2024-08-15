### File Handling ###

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

with open("Intermediate/my_file.txt", "a") as my_other_file: # Con with no hace falta escribir .close(), tambien maneja excepciones. *** Mejor opción ***
    my_other_file.write("\nNi JavaScript")

import os
# os.remove("Intermediate/my_file.txt")



# .json file
import json
import xml.dom
import xml.etree

json_file = open("Intermediate/my_file.json", "w+")

json_test ={
    "name":"Alejandro", 
    "surname":"de Pablo",
    "age":22, 
    "languages": ["Python","Kotlin", "Swift"],
    "website":"https://example.com"}

json.dump(json_test, json_file, indent = 2)

json_file.close() # Lo cerramos para abrirlo de nuevo y poder leerlo

with open("Intermediate/my_file.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

json_dict = json.load(open("Intermediate/my_file.json"))
print(json_dict)
print(type(json_dict))
print(json_dict["name"])



# .csv file
import csv

csv_file =  open("Intermediate/my_file.csv", "w+")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "surname", "age","language", "website"])
csv_writer.writerow(["Alejandro", "de Pablo", "22","Python", "inventada.com"])
csv_writer.writerow(["Roswell", "","2","COBOL", ""])

csv_file.close()

with open("Intermediate/my_file.csv") as my_other_file:
    for line in my_other_file.readlines():
        print(line.strip())

# .xlsx file
# import xlrd # debe instalarse el módulo



# .xml file
import xml.etree.ElementTree as ET

# CREAR ARCHIVO XML

# Crear un elemento raíz
root = ET.Element("root")

# Crear sub-elementos
child1 = ET.SubElement(root, "child1")
child1.text = "Texto del primer hijo"

child2 = ET.SubElement(root, "child2")
child2.text = "Texto del segundo hijo"

# Crear un objeto ElementTree
tree = ET.ElementTree(root)

# Guardar el árbol XML en un archivo
with open("Intermediate/my_file.xml", "wb") as file:
    tree.write(file, encoding="utf-8", xml_declaration=True)

# LEER ARCHVIO XML
tree = ET.parse("Intermediate/my_file.xml")
root = tree.getroot()

# Imprimir el contenido del XML
print("Contenido del archivo XML:")

for child in root:
    print(f"{child.tag}: {child.text}")

print("Archivo XML leído exitosamente.")


# MODIFICAR ARCHIVO XML

# Crear un nuevo elemento
new_child = ET.SubElement(root, "child3")
new_child.text = "Texto del tercer hijo"

# Guardar el árbol XML modificado en el archivo
with open("Intermediate/my_file.xml", "wb") as file:
    tree.write(file, encoding="utf-8", xml_declaration=True)

print("Archivo XML modificado exitosamente.")


