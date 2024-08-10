### Exceptions Handling ###

numberOne, numberTwo = 5, 1
numberTwo  = "1"

# try except
try:
    print(numberOne + numberTwo)
except:
    print("ERROR")

# try except else finally
try:
    print(numberOne + numberTwo)
except:
    print("ERROR")
else: # Opcional
    # Se ejecuta si no hay excepción
    print("La ejecucion continua correctamente")
finally: # Opcional
    # Se ejecuta siempre
    print("La ejecución continúa")

 # Excepciones por tipo
try:
    print(numberOne + numberTwo)
except ValueError:
    print("ERROR")
except TypeError:
    print("ERROR")

 # Captura de la información de la excepción
try:
    print(numberOne + numberTwo)
except Exception as error:
    print(error)
