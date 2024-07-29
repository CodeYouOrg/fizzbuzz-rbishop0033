# Print numbers 1 to 100
# If divisible by 3 print Fizz instead of number
# If divisible by 5 print Buzz instead of number
# If divisible by 3 and 5, print FizzBuzz instead of number

for x in range(1,101):
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print ("Fizz")
    elif x % 5 == 0:
        print ("Buzz")
    else:
        print(x)         


