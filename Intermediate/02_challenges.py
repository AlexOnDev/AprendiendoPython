### Challenges ###

# FIZZ BUZZ
def fizzbuzz():
    for i in range(1, 101):
        if i % 5 == 0 and i % 3 == 0:
          print(f"{i} FIZZBUZZ")
        elif i % 3 == 0:
          print(f"{i} FIZZ")
        elif i % 5 == 0:
          print(f"{i} BUZZ")
        else:
          print(i)
fizzbuzz()

# ¿Es un anagrama?

def is_anagram(word_one,word_two):
   if word_one.lower() == word_two.lower():
      return False
   return sorted(word_one.lower()) == sorted(word_two.lower())

print(is_anagram("Ramo", "Roma"))

# Fibonacci
def fibonacci():
    prev = 0
    next = 1
    for i in range(0, 50):
       print(prev)
       fib = prev + next
       prev = next
       next = fib
fibonacci()

# ¿Es un número primo?
def is_prime():
   
   for number in range(1,101):
        if number >= 2:
            is_divisible = False

            for i in range(2,number):
                if number % i == 0:
                    is_divisible = True
                    break

            if not is_divisible:            
                print(number)
is_prime()

# Invertir cadena texto sin usar funciones

def reverse(text):
    reversed_text = ""
    text_length = len(text)
    
    for index in range (0, text_length):
        reversed_text += text[text_length - index - 1]
    return reversed_text
print(reverse("Hola mundo"))