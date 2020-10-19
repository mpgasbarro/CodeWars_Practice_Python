# time = 23

# if time < 9:
#     print("Morning is wonderful. its only drawback is that it comes at such an incovenient time of day")
# elif time <= 16 and time > 9:
#     print("Working hard or hardly working")
# elif time < 20 and time > 16:
#     print("How did it get so late so soon")
# elif time < 22 and time > 20:
#     print("A daty without sunshine is like, you know, night")
# else:
#     print("Burning the midnight oil!")
# _______________________________________

# angry = True
# bored = True
# hungry = True
# tired = False

# if hungry and bored and angry:
#     print("Ya boy is going to eat a Triceratops")
# elif tired and hungry:
#     print("ya boy is going to eat the iguanadon")
# elif hungry and bored:
#     print("ya boy is going to eat the Stegasaurus")
# elif tired:
#     print("Ya boy is taking a nap")
# elif angry and bored:
#     print("Ya boy is fighting a velociraptor with Chris Pratt")
# elif angry and bored:
#     print("ROARRRRRRRR")
# else:
#     print("ya boy gives a toothy smile, whatever that means")
# __________________________________________________________________
# disney_characters = ['simba', 'ariel', 'pumba', 'flounder', 'nala', 'ursula', 'scar', 'flotsam', 'timon']

# for i in range(0, len(disney_characters[0: : ])):
#     if "i" in "disney_characters[i]:
#         print("I bet you're Impressively Intelligent!")
# -_________________________________________________________________________________________
# def get_average(marks):
#     summ = 0
#     length = len(marks)
#     for i in marks:
#        summ += i
#     total = summ // length
#     return(total)

# num = [1,23,4,5]

# print(get_average(num))
# _________________________________________________________________________
# return masked string
# def maskify(cc):
#     length = len(cc)
#     whereToCut = length - 4
#     index = cc.index(whereToCut)
#     print(index)
#     newArr = cc.split(whereToCut)
#     print(newArr)


# stri = "1234567"

# maskify(stri)
# 
# 

# Starting with the following list...
planeteers = ["Earth", "Wind", "Captain Planet", "Fire", "Water"]

# Access the second value in `planeteers`
# print(planeteers[1])

# Add "Heart" to the end of `planeteers`
# planeteers.append("Heart")
# print(planeteers)

# Remove "Captain Planet" from the list
# planeteers.remove("Captain Planet")
# print(planeteers)

# Combine `planeteers` with `rangers = ["Red", "Blue", "Pink", "Yellow", "Black"]` and save the result in a variable called `heroes`
rangers = ["Red", "Blue", "Pink", "Yellow", "Black"]
heroes = planeteers + rangers
# print(heroes)

# Alphabetize the contents of `heroes` using a function
# heroes.sort()
# print(heroes)

# Randomize the contents of `heroes` using a function. 
# The Python documentation might help: https://docs.python.org/2/library/random.html
# import random
# # random.shuffle(heroes.random())
# # print(heroes)

# # Bonus: Select a random element from `heroes` using a function
# # The Python documentation might help: https://docs.python.org/2/library/random.html
# print(random.sample(heroes, 1))


# Initialize a dictionary called `ninja_turtle` with the properties `name`, `weapon` and `radical`
# They should have values of "Michelangelo", "Nunchuks" and a true boolean, respectively

# ninja_turtle = {
#     "name" : "Michaelangelo",
#     "weapon" : "Nunchuks",
#     "radical" : True,
# }


# # Add a key `age` to `ninja_turtle`. Set it to whatever numerical value you'd like

# ninja_turtle["Age"] = 32

# # print(ninja_turtle)

# # Remove the `radical` key-value pair from `ninja_turtle`

# ninja_turtle.pop("radical")
# # print(ninja_turtle)

# # Add a key `pizza_toppings` to `ninja_turtle`. Set it to an list of strings (e.g., `["cheese", "pepperoni", "peppers"]`)

# ninja_turtle["Pizza Topping"] = [ "cheese", "Pepperoni", "Peppers"]

# print(ninja_turtle)

# Access the first element of `pizza_toppings`

# print(ninja_turtle["Pizza Topping"][0])


# # Produce an list containing all of `ninja_turtle`'s keys using a function. 
# # The Python documentation might help: https://docs.python.org/3/tutorial/datastructures.html

# print(list(ninja_turtle))

# Produce a list containing all of `ninja_turtle`'s values using a function

# print(ninja_turtle.values())
# Bonus: Write a function that prints out each key-value pair in the following format - "KEY is equal to VALUE"
#  The Python documentation might help: https://docs.python.org/3/tutorial/datastructures.html

# def val(n):
#     name = ninja_turtle["name"]
#     weapon = ninja_turtle["weapon"]
#     age = ninja_turtle["Age"]
#     pizza_topping = ["Pizza Topping"]

#     for x in list(n):
#         key = x
#     for z in ninja_turtle.values():
#         val = z
    
#     print(f"{key} is equal to {val}")

# val(ninja_turtle)


# print("welcome to the bar! how old are you?")
# age = int(input())

# if age < 21 and age > 18:
#     print("you can come in but you cant drink")
# elif age < 18:
#     print("you can't drink")
# else:
#     print("come on in and get hammered")
# _______________________________________________________________________________
# CODEWARS PRACTICE PROBLEM - 10/16/20
# Write a function that rearranges an integer into its largest possible value.
#     superSize(123456) //654321
#     superSize(105) // 510
#     superSize(12) // 21
# If the argument passed through is single digit or is already the maximum possible integer, your function should simply return it.


# def super_size(n):
#     num_string = str(n)
    
#     if len(num_string) <  2:
#         print(n)

#     else:
#         sorted_string = sorted(num_string, reverse=True)
#         return_list = int("".join(sorted_string))
#         print (return_list)



# super_size(4)
# _______________________________________________________________
# CODEWARS PRACTICE PROBLEM - 10/16/20
# Your task is simply to count the total number of lowercase letters in a string.
# Example
# lowercaseCount("abc"); ===> 3
# lowercaseCount("abcABC123"); ===> 3

# def lowercase_count(strng):
#     new_str = sorted(strng)
#     sum = 0

#     for i in new_str:
#         if i.islower():
#             sum = sum +1 
            

#     return sum

# lowercase_count("abcABC12&%*&@^#3")   
# _______________________________________________________________________
# CODEWARS PRACTICE PROBLEM - 10/17/20

# What if we need the length of the words separated by a space to be added at the end of that same word and have it returned as an array?

# add_length('apple ban') => ["apple 5", "ban 3"]
# add_length('you will win') => ["you 3", "will 4", "win 3"]
# Your task is to write a function that takes a String and returns an Array/list with the length of each word added to each element .

# Note: String will have at least one element; words will always be separated by a space.

# SOLUTION
# def add_length(str_):
#     new_new = []
#     new_word = str_.split(" ")
#     for i in new_word:
#         length = len(i)
#         new_new.append(i + " " + str(length))
#     return new_new

# add_length("hello there")




# ____________________________________________________
# CODEWARS PRACTIE PROBLEM 10/17/20
# Given two integer arrays a, b, both of length >= 1, create a program that returns true if the sum of the squares of each element in a is strictly greater than the sum of the cubes of each element in b.
# E.g.
# array_madness([4, 5, 6], [1, 2, 3]) => True #because 4 ** 2 + 5 ** 2 + 6 ** 2 > 1 ** 3 + 2 ** 3 + 3 ** 3
# Get your timer out. Are you ready? Ready, get set, GO!!!


# SOLUTION
# def array_madness(a,b):
#     sumA = 0
#     sumB = 0
#     for i in a:
#         sumA = sumA + (i ** 2)
        
#     for b in b:
#         sumB = sumB + (b ** 2)
    
#     if sumA > sumB:
#         return True
#     else:
#          return False
     



# array_madness([0, 4, 123], [4, 5, 6])

# CODEWARS PRACTICE PROBLEM 10/18/20
#  You get an array of numbers, return the sum of all of the positives ones.
# Example [1,-4,7,12] => 1 + 7 + 12 = 20
# Note: if there is nothing to sum, the sum is default to 0.

# SOLUTION
# def positive_sum(arr):
#     sum = 0
#     for i in arr:
#         if i >= 0:
#             sum += i

#     return sum


# positive_sum([-4,9,-7,-1,-2, -3])