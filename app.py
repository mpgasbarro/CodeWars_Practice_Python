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

ninja_turtle = {
    "name" : "Michaelangelo",
    "weapon" : "Nunchuks",
    "radical" : True,
}


# Add a key `age` to `ninja_turtle`. Set it to whatever numerical value you'd like

ninja_turtle["Age"] = 32

# print(ninja_turtle)

# Remove the `radical` key-value pair from `ninja_turtle`

ninja_turtle.pop("radical")
# print(ninja_turtle)

# Add a key `pizza_toppings` to `ninja_turtle`. Set it to an list of strings (e.g., `["cheese", "pepperoni", "peppers"]`)

ninja_turtle["Pizza Topping"] = [ "cheese", "Pepperoni", "Peppers"]

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