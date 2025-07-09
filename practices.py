"""print("hello world")
print("|____/")
print("|   /")
print("|  /")
print("| /")
print("|/")

char_name = "Pilli Shanyu Veda Seshu"
char_age = "20"
print("my name is " + char_name +",")
print("my age is " + char_age +".")

print("pilli shanyu\nveda seshu")
print(len(char_name)) '''hear this len to calculate the letters in char_name'''
print(char_name[2])
print(char_name.index("h"))
print(char_name.upper())
print(char_name.lower())
print(char_name.isupper())
print(char_name.islower())
print(char_name.upper().isupper())
print(char_name.lower().islower())
print(char_name.replace("Shanyu","Shannu"))"""

"""my_num = 3
print(my_num)
print(str(my_num)+" is my favorite number")
print(pow(5,2))
print(abs(my_num))
print(max(4,6))
print(min(4,6))
print(round(3.2))
print(round(3.7))
from math import*
print(floor(3.3))
print(ceil(3.3))
print(sqrt(36))"""

"""name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + "! you are " + age)"""

"""num1 = input("Enter your first number: ")
num2 = input("Enter your second number: ")
result = int(num1) + float(num2)
print(result)"""

#mad lids game
'''color = input("enter a color: ")
plural_noun = input("enter a plural noun: ")
celebrity = input("enter a celebrity: ")

print("roses are " + color)
print(plural_noun + " are blue ")
print(" i love " + celebrity)'''



#Lists

"""friends = ["rahul","nabeel","jaswanth","surya"]
friends[1]="shanyu"
print(friends[1])
print(friends[-1])
print(friends[1:])
print(friends[:2])
print(friends[1:3])"""

#Lists Functions
"""lucky_numbers = [1,3,2,4,5,6,9,8,7]
friends = ["rahul","nabeel","jaswanth","surya","surya"]
friends.extend(lucky_numbers)
friends.remove("nabeel")
friends.append("shanyu")
friends.insert(2,"seshu")
friends.clear()
friends.pop()"""
"""friends.sort()
lucky_numbers.sort()
lucky_numbers.reverse()"""
"""friends1 = friends.copy()
print(friends1)
print(lucky_numbers)
"""

#Tuples

"""coordinate = (4,5)
print(coordinate[0])
coordinates = [(4,5),(6,7),(8,9)]
print(coordinates[0])"""

#functions:
"""def say_hi(name ,age):
    print(" hi " + name + "! you are " + str(age))
say_hi("shanyu" ,"23")
say_hi("seshu" , "22")
"""
"""def cube(num):
    return num ** 3
result = cube(5)
print(cube(4))
print(cube(5))"""

#if statement


"""is_male = False
is_tall = True
if is_male and is_tall:
    print("he is a male and tall")
elif is_male and not(is_tall):
    print("he is a male and not tall")
elif not(is_male) and is_tall:
    print("he is not a male but tall")
else:
    print("he is not a male and not a tall")"""


#comparisions

"""def max_num(num1, num2 , num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    elif num3 > num1 and num3 > num2:
        return num3
    else:
        return num1
result = max_num(1, 2, 3)
print(result)"""

#advanced calculator
"""num1 = float(input("Enter your first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter your second number: "))
if op == "+":
    result = num1 + num2
    print(result)
elif op == "-":
    result = num1 - num2
    print(result)
elif op == "*":
    result = num1 * num2
    print(result)
elif op == "/":
    result = num1 / num2
    print(result)
elif op == "//":
    result = num1 // num2
    print(result)
elif op == "**":
    result = num1 ** num2
    print(result)
else:
    print("Invalid operator")"""

#dictionaries

"""monthConversion ={
    0: "January",
    1: "February",
    2: "March",
    3: "April",
    4: "May",
    5: "June",
    6: "July",
    7: "August",
    8: "September",
    9: "October",
    10: "November",
    11: "December"
}"""

"""monthConversions ={
    "Jan" : "January",
    "Feb" : "February",
    "Mar" : "March",
    "Apr" : "April",
    "May" : "May",
    "Jun" : "June",
    "Jul" : "July",
    "Aug" : "August",
    "Sep" : "September",
    "Oct" : "October",
    "Nov" : "November",
    "Dec" : "December",
}

print(monthConversions["Jun"])
print(monthConversions["Feb"])
print(monthConversions["Dec"])"""


#while loop
"""i = 1
while i <= 10:
    print(i)
    i = i + 1
print("done with loop")"""


#building a guessing game
"""secret_word = "shannu"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guess = False
while guess != secret_word and not (out_of_guess):
    if guess_count < guess_limit:
        guess = input("Guess my nickname: ")
        guess_count += 1
    else:
         out_of_guess = True
if out_of_guess:
    print("Sorry out of guesses, you lose")
else:
    print("you win")"""


#For loop
"""friends = ["shanyu" , "rahul", "nabeel" , "jaswanth" , "surya"]
for index in range(len(friends)):
    print(friends[index])"""



#exponent function
"""def raise_to_power(base_num,pow_num):
     result = 1
     for index in range(pow_num):
         result = result * base_num
     return result

print(raise_to_power(2,3))"""


#2D Lists & Nested Loops
"""number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
for row in number_grid:
    for column in row:
        print(column)"""



#build a translator

"""def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "aeiou":
            if letter.isupper():
               translation = translation + "G"
            else:
               translation = translation + "g"

        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))"""

#Try Except
"""try:
    answer = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as error:
    print("error")
except ValueError:
    print("Value is not a number")"""

#reading files
"""employe_file = open("employees.txt" , 'r')
print(employe_file.read())
employe_file.close()"""

#writing to files
"""employe_file = open("employees.txt" , 'a')
employe_file.write("\nShanyu - human resources")
employe_file.close()"""
"""employe_file = open("employees.txt" , 'w')
employe_file.write("\nShanyu - human resources")
employe_file.close()"""
"""employe_file = open("index.html" , 'w')
employe_file.write("\n<h1> shanyu<h1>")
employe_file.close()"""

#Modules and Pip
"""import usefull_tools
print(usefull_tools.roll_dice(10))"""



#Classes & Objects
"""from student import Student
student1 = Student("Shanyu","b.tech",9.0,False)
student2 = Student("Rahul","b.tech",9.88,True)

print(student2.gpa)"""

#Building a multiple choice Quiz
from question import question
"""question_prompts = [
      "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
      "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
      "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]
questions = [
    question(question_prompts[0], "a"),
    question(question_prompts[1], "c"),
    question(question_prompts[2], "b"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.promt)
        if answer == question.answer:
            score += 1
    print("your got  " + str(score) + "/" + str(len(questions)) + "correct")
run_test(questions)"""

#object functions
"""from student import Student
student1 = Student("Shanyu","b.tech",8.0,)
student2 = Student("Rahul","b.tech",9.88,)
print(student1.on_honor_roll())
print(student2.on_honor_roll())"""


#inheritance
"""
from Chef import Chef
from ChineseChef import ChineseChef
myChef = Chef()
myChef.make_special_dish()
myChineseChef = ChineseChef()
myChineseChef.make_special_dish()""""