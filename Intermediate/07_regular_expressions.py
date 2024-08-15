### Regular Expressions ###

import re

# Match

my_string = "Esta es la lección numero 7: Lección llamada Expresiones Regulares"
my_other_string = "Esta no es la lección numero 6: Manejo de ficheros"

match = re.match("Esta es la lección", my_string, re.I) # Ignore Case
print(match)
start, end = match.span()
print(my_string[start:end])

match = re.match("Esta no es la lección", my_other_string)
#if not(match == None):
#if match is not None:
if match != None:
    print(match)
    start, end = match.span()
    print(my_other_string[start:end])

#print(re.match("Expresiones Regulares", my_string)) # None porque empieza a buscar desde el principio

# Search 

search = re.search("lección", my_string, re.I) # Recoge la primera que aparece 
print(search)
start, end = search.span()
print(my_string[start:end])

# Findall

findall = re.findall("la", my_string, re.I)
print(findall)

# Split

print(re.split(":", my_string))

# Sub

print(re.sub("Expresiones Regulares", "RegEx", my_string))
print(re.sub("[l|L]ección", "LECCIÓN", my_string))

# Patterns
# https://regex101.com/

pattern = r"[lL]ección"
print(re.findall(pattern, my_string))

pattern = r"[lL]ección|Expresiones"
print(re.findall(pattern, my_string))

pattern = r"[0-9]"
print(re.findall(pattern, my_string))
print(re.search(pattern, my_string))

pattern = r"\d"
print(re.findall(pattern, my_string))

pattern = r"\D"
print(re.findall(pattern, my_string))

pattern = r"[l].*"
print(re.findall(pattern, my_string))

# email validation regular expression

email = "alexondev@gmail.com"
pattern = r"^[a-zA-z0-9_.+-]+@[a-zA-z0-9-]+\.[a-zA-Z0-9-.]+$"
print(re.match(pattern, email))
print(re.search(pattern, email))
print(re.findall(pattern, email))

email = "alexondev@alexondev.com.mx"
print(re.findall(pattern, email))


