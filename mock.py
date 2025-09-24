#to check if number is even or odd
def odd_even(number):
  if number %2 == 0:
    print("Even Number")
  else:
    print("Odd Number")

#to check if number is positive or negative
def positive_negative(number):
   if number>0:
    print("Positive number")
   else:
    print("Negative number")

#find square of a number
def square(number):
    return number * number

#find cube of a number
def cube(number):
    return number * number * number

#the main function
def main():
    number = int(input("Enter a number: "))
    
    print("Even/Odd: ", even_odd (number))
    print("Positive/Negative: ", positive_negative(number))
    print("Square: ", square(number))
    print("Cube: ", cube(number)) 

