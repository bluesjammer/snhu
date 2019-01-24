# Task_1
# Write a loop that accumulates the sum of all the numbers in a list (given below) and prints the sum in the end.
# Done two ways, with a loop in a home made function and one way  with the built-in sum() function.

#Here is the first way

print("\n\n\t\tHere are two solutions to the first task. \n\n")

Data = [0, -1, 2, -3, 4, -5, 6, -7, 8]

def list_sum(items):
    num_sum = 0
    for x in items:
         num_sum += x
    return num_sum

print("For the list called Data, composed of the items : \n\n" + str(Data)+ ", \n\nthe sum of all the numbers in the list is \t" + str(list_sum(Data)) + ". \n")


#Here is the second way

Data = [0, -1, 2, -3, 4, -5, 6, -7, 8]

x = sum(Data)

print("\n")

print("Even done another way, the sum of the list called Data is still \t" + str(x) + ". \n\n\n\n")


print("\t\tAnd here is  the solution to the second task: \n\n ")

# Task_2
# Write a loop that accumulates the sum of absolute value of all the numbers in a list (given below) and prints the sum in the end.

import math

Data = [0, -1, 2, -3, 4, -5, 6, -7, 8]

def  abs_sum(items):
    sum  = 0
    for x in items:
        sum += abs(x)
    return sum
print("The sum of the absolute values of the list Data is \t" + str(abs_sum(Data)) + ".\n\n")
