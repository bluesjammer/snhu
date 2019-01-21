# Task_1 
# Print numbers 1 through 5

for i in range(1,6):
    print(i)
print("\n")





# Task_2 
# Print sum of 3 and 4

x = 3 + 4
print("The sum of 3 and 4 is " + str(x) + "\n")





# Task_3 
# Print sum of constant pi and square root of 2. 

import math
pi = math.pi
squareroot = math.sqrt(2)
x = pi + squareroot
print("Pi is " + str(pi))
print("The square root of 2 is " + str(squareroot))
print("The sum of pi and the square root of 2 is " + str(x) + "\n")






# Task_4 
# Print sum of cos30 + sin30 where cos and sin are trigonometric functions and angle specified is in degrees. 

import math
x = math.cos(math.radians(30))
print("The cosine of 30 degrees is " + str(x))

y = math.sin(math.radians(30))
print("The sine of 30 degrees is " + str(y))

z = (x + y)
print("The sum of the cosine of 30 degrees and the sine of 30 degrees is " + str(z) + "\n")





# Task_5
# Write code to print values of integers x, y, and z in a single line such that each value is left-justified in 6 columns.

import math

x = input("Please type an integer. \n")
y = input("Please type a second integer. \n")
z = input("Please type a third integer. \n")

print("Your three integers are: \n " + x.ljust(6) + y.ljust(6) + z.ljust(6) + "\n")





# Task_6
# Write code to print area of a circle given the value of the radius of the circle

import math

pi = math.pi
radius = input("Please enter the  radius of a circle. \n")
area = pi * int(radius) ** 2
print("The area of a circle with radius " + radius + " is " + str(area) + ". \n")




# Task_7
# Write code to print the greater of two given numbers x and y

x = input("Please enter a number. \n")
y = input("Please enter another number. \n")

if x > y:
    print(str(x) + " is greater than " + str(y) + ". \n")
elif x < y:
    print(str(x) + " is less than " + str(y) + ". \n")
else:
    print(str(x) + " is equal to " + str(y) + ". \n")



# Task_8
# Write code to print the result of negation of AND of two Boolean variables A and B

A = bool(1)
B = bool(0)

print("A is equal to 1 and B is equal to 0.")

print("A is therefore " + str(A) + ".")
print("And B is therefore " + str(B) + ".")

C = A and B

Z = not C

print("That means both together are " + str(C))

print("The negations of which makes them " + str(Z) + "\n")




# Task_9
# Write a for-loop to sum the first 10 non-zero integers

x = 1
y = 0
for i in range(1, 11):
    y = y + x
    x += 1
print("The sum of the first ten non-zero integers is " + str(y) + "\n")

    




# Task_10
# Write a while-loop to sum the first 10 non-zero integers

x = 1
i = 2
while i < 11:
    x = x + i
    i += 1
    
print("The sum of the first ten non-zero integers is " + str(x))

    




































































