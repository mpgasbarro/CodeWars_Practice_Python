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
# 
# 
# 
# 
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
# _________________________________________________________________-



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
# /-_____________________________________________________




# CODEWARS PROBLEM - 10/20/20

# Create a function with two arguments that will return an array of the first (n) multiples of (x).
# Assume both the given number and the number of times to count will be positive numbers greater than 0.
# Return the results as an array (or list in Python, Haskell or Elixir).
# Examples:
# count_by(1,10) #should return [1,2,3,4,5,6,7,8,9,10]
# count_by(2,5) #should return [2,4,6,8,10]


# *****SOLUTION*******
# def count_by(x, n):
#     sum = x * n
#     arr = []
#     total = range(x, sum + 1, x)

#     for i in total:
#         arr.append(i)
    
#     return(arr)

# count_by(2, 5)

# ____________________________________________________________
# CODEWARS PROBLEM 10/20/20
# Task:
# Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...". Input will always be valid, i.e. no negative integers.


# *****SOLUTION*****
# def count_sheep(n):
#     x = range(1, n + 1, 1)
#     sum = ""
#     for i in x:
#         sum = sum + str(i) + " sheep..."
        
#     return sum 

# count_sheep(5)




# _______________________________________________________________

# CODEWARS PROBLEM 10/20/20


# Challenge:

# Given a two-dimensional array, return a new array which carries over only those arrays from the original, which were not empty and whose items are all of the same type (i.e. homogenous). For simplicity, the arrays inside the array will only contain characters and integers.

# Example:

# Given [[1, 5, 4], ['a', 3, 5], ['b'], [], ['1', 2, 3]], your function should return [[1, 5, 4], ['b']].

# Addendum:

# Please keep in mind that for this kata, we assume that empty arrays are not homogenous.

# The resultant arrays should be in the order they were originally in and should not have its values changed.

# No implicit type casting is allowed. A subarray [1, '2'] would be considered illegal and should be filtered out.


# ***** SOLUTION *****
# def filter_homogenous(arrays):
#     for i in arrays:
#         for x in i:
#             print(x)
       




# filter_homogenous([[1, 5, 4], ['a', 3, 5], ['b'], [], ['1', 2, 3]])

# ____________________________________________________________________
# CODEWARS PROBLEM - 10/21/20
# Let's play! You have to return which player won! In case of a draw return Draw!.
# Examples:

# rps('scissors','paper') // Player 1 won!
# rps('scissors','rock') // Player 2 won!
# rps('paper','paper') // Draw!


# ***** SOLUTION *****
# def rps(p1, p2):
#     if p1 == "scissors" and p2 == "paper":
#         return "Player 1 won!"
#     elif p1 == "paper" and p2 == "scissors":
#         return "Player 2 won!"
#     elif p1 == "rock" and p2 == "paper":
#         return "Player 2 won!"
#     elif p1 == "paper" and p2 == "rock":
#         return "Player 1 won!"
#     elif p1 == "rock" and p2 == "scissors":
#         return "Player 1 won!"
#     elif p1 == "scissors" and p2 == "rock":
#         return "PLayer 2 won!"
#     elif p1 == p2:
#         return "Draw!"
    

# rps("scissors", "paper")

# ____________________________________________________________


# CODEWARS PROBLEM 10/22/20


# Challenge:

# Given a two-dimensional array, return a new array which carries over only those arrays from the original, which were not empty and whose items are all of the same type (i.e. homogenous). For simplicity, the arrays inside the array will only contain characters and integers.

# Example:

# Given [[1, 5, 4], ['a', 3, 5], ['b'], [], ['1', 2, 3]], your function should return [[1, 5, 4], ['b']].

# Addendum:

# Please keep in mind that for this kata, we assume that empty arrays are not homogenous.

# The resultant arrays should be in the order they were originally in and should not have its values changed.

# No implicit type casting is allowed. A subarray [1, '2'] would be considered illegal and should be filtered out.


# ***** SOLUTION *****I WAS NOT ABLE TO SOLVE THIS****

# def filter_homogenous(arrays):
#     return[a for a in arrays if len(set(map(type,a)))==1]




# filter_homogenous([[1, 5, 4], ['a', 3, 5], ['b'], [], ['1', 2, 3]])

# CODEWARS PROBLEM - 10/26/20
# This time no story, no theory. The examples below show you how to write function accum:

# Examples:

# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"
# The parameter of accum is a string which includes only letters from a..z and A..Z.


# SOLUTION  - Still working on getting last dash out of last index
# def accum(s):
#     new_Arr = []
#     val=""
#     for char in s:
#         new_Arr.append(char)
        
#     for i in new_Arr:
#         val = new_Arr.index(i) + 1
#         last_Ind = new_Arr[len(new_Arr) -1]
#         ind = len(new_Arr)
#         new_Arr.pop(new_Arr.index(i))
#         new_Arr.insert(val - 1, (i * val))
#     result = "-".join(str(i).capitalize() for i in new_Arr)
   
    
#     print(result)

# accum("abcd")


# _______________________________________________________________________

# CODEWAR PRACTICE  - 11/05/20
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

# Note: If the number is a multiple of both 3 and 5, only count it once. Also, if a number is negative, return 0(for languages that do have them)



# ***** SOLUTION *****


# def solution(number):
#     sum = 0
#     for i in range(0, number):
#         if i % 3 == 0 and i % 5 != 0:
#             sum += i
#         if i % 5 == 0 and i % 3 != 0:
#             sum += i
#         if i % 5 == 0 and i % 3 == 0:
#             sum += i

#     print(sum)

# solution(16)

# __________________________________________________________________________

# CODEWAR PRACTICE - 11/05/20
# Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

# Examples: spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" spinWords( "This is a test") => returns "This is a test" spinWords( "This is another test" )=> returns "This is rehtona test"


#  ***** SOLUTION *****

# def spin_words(sentence):
#     newWord = sentence.split(" ")
#     newArr = []
#     for i in newWord:
#         if(len(i) >= 5):
#             indexx = newWord.index(i)
#             newWord.pop(indexx)
#             newVal = i[::-1]
#             newWord.insert(indexx, newVal)
    
#     return(" ".join(newWord))

    

# spin_words("hello there how are you doings")



# __________________________________________________________________________-
# CODEWARS PRACTICE - 11/11/20
# You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.

# #Examples:

# Kata.getMiddle("test") should return "es"

# Kata.getMiddle("testing") should return "t"

# Kata.getMiddle("middle") should return "dd"

# Kata.getMiddle("A") should return "A"
# #Input

# A word (string) of length 0 < str < 1000 (In javascript you may get slightly more than 1000 in some test cases due to an error in the test cases). You do not need to test for this. This is only here to tell you that you do not need to worry about your solution timing out.

# #Output

# The middle character(s) of the word represented as a string.


# ***** SOLUTION *****
# def get_middle(s):
#     length_of_word = len(s)
#     middle_index = 0

#     for i in s:
#         print(i)

#     if length_of_word % 2 == 0:
#         print("yo yo")
#     elif length_of_word % 2 != 0:
#         print ("suhhhhh")





# get_middle("helloz")

# __________________________________________________________________
# print("Welcome to the the Club! What is your age?")
# age = int(input())

# if age >= 18 and age < 21:
#     print("YOu can come in but you cant drink")
# elif age < 18:
#     print("You're too young, LATER")
# else:
#     print(" Come get drunk"
#     )


# planeteers = ["Earth", "Wind", "Captain Planet", "Fire", "Water"]
# rangers = ["Red", "Blue", "Pink", "Yellow", "Black"]
# planeteers.append("Heart")
# planeteers.pop(2)


# heroes = planeteers.append(rangers)

# print(heroes)
# ___________________________________________________________________
# Building up on Pzython
# for x in range(1,5):
#     print(x)

# def summation(num):
#     sum = 0
#     for i in range(1, num + 1):
#         sum += i

#     return sum

# summation(8)

# _________________________________________________________________
# def positive_sum(arr):
#     sum = 0
#     for i in arr:
#         if i > 0:
#             sum += i
           
#     return sum


# positive_sum([1,-4,7,12])
