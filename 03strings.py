### STRINGS ###

myString= "Mi string"
MyOtherString ="Mi otro string"

print(len(myString))
print(len(MyOtherString))

print(myString + " " + MyOtherString)

myNewLineString = "Este es un String \ncon salto de linea"
myTabString = "Este es un String \tcon tabulacion"

print(myNewLineString)
print(myTabString)

myScapeString = "\\t Este es un String \\n escapado"
print(myScapeString)

# Formateo
name, surname, age = "Alejandro", "de Pablo", 22
print("Mi nombre es {} {}, y mi edad es {}".format(name,surname,age))
print("Mi nombre es %s %s, y mi edad es %d" %(name, surname, age))

print(f"Mi nombre es {name} {surname}, y mi edad es {age}") # mejor que "Mi nombre es " + name + " ... " + ""

# Desempaquetado de caracteres
language = "python"
a, b, c, d, e, f= language
print(a)
print(b)

# División 
languageSlice = language[1:3]
print(languageSlice)

languageSlice = language[1:]
print(languageSlice)

languageSlice = language[-2]
print(languageSlice)

languageSlice = language[0:6:2]
print(languageSlice)

# Reverse
reverseLanguage = language[ :: -1]
print(reverseLanguage)

# Funciones
print(language.capitalize())
print(language.upper())
print(language.lower())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.upper().isupper())
print(language.startswith("Py"))
