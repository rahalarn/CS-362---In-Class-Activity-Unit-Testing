def addition(a, b):
   return a + b

def subtraction(a, b):
   return a - b

def multiplication(a, b):
   return a * b

def division(a, b):
   try:
      return round(a / b, 1)
   except ValueError:
      print("Cannot divide by 0 .. or can you?")
