#1. Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
#Example: countdown(5) should return [5,4,3,2,1,0]
#Pseudocode:
    #Set a function.
        #set an array
        #Create a for loop that starts at int, ends at 0, and decrements by 1
            #Inside the for loop, apply each iteration to a list of values.
        #Make the function return said array.
countdown_list = []
def countdown(int):
    for x in range(int, 0, -1):
        countdown_list.append(x)
    return countdown_list

print(countdown(9))

#2. Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
#Example: print_and_return([1,2]) should print 1 and return 2
def print_and_return(a, b):
    print(a)
    return(b)

print(print_and_return(1, 2))

#3. First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
#Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)
#Pseudocode:
    #Create a function first_plus_length(list):
        #Inside said function, return list[0] + list.length
def first_plus_length(x):
    return x[0] + len(x)

print(first_plus_length([5, 4, 3, 2, 1]))

#4. Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that 
# are greater than its 2nd value. 
# Print how many values this is and then return the new list. 
# If the list has less than 2 elements, have the function return False
#Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
#Example: values_greater_than_second([3]) should return False
#Pseudocode:
    #Create a function values_greater_than_second(x):
        #Inside said function, create a for loop that starts at 0, ends at len(x) - 1, and increments by 1
            #Inside the for loop, create a conditional:
                #If value at index is larger than x[1], add it to a New List y
        #Print the number of elements in New List Y
        #Print number of elements in New List Y < 2
        #Return New List Y
def values_greater_than_second(x):
    if len(x) < 2:
        return "false"
    else:
        y = []
        for i in range(0, len(x), 1):
            if x[i] > x[1]:
                y.append(x[i])
        print (len(y))
        print (len(y) > 2)
        return y

print(values_greater_than_second([5,2,3,2,1,4]))

#5. This Length, That Value - Write a function that accepts two integers as parameters: size and value. 
# The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
#Example: length_and_value(4,7) should return [7,7,7,7]
#Example: length_and_value(6,2) should return [2,2,2,2,2,2]

def this_length_that_value (a, b):
    the_list = []
    for i in range(0, a, 1):
        the_list.append(b)
    return the_list

print(this_length_that_value(6, 2))