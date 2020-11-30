#34

number = int(input("Enter an number here: "))

if (number % 2) == 0: 
    print("\nYour number is an even number")
else: 
    print("\Your number is an odd number")


#35:

years = int(input("Please enter your dog's age in human years: "))

if (0 <= years <= 2):
    young = 10.5 * years
    print(f"Your dog is {young} years old.")

if years > 2:
    (old) = 21 + 4 * (years - 2)
    print(f"Your dog is {old} years old.")

elif years < 0:
    print("Please type in a valid age.")
    
    
#36:

letter = input("Enter a letter of the alphabet: ")

if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
    print("Vowel")
elif letter == "y":
    print("Your letter is a vowel")
else:
    print("Your letter is a Consonant")
    
#37:

shape = int(input("Enter the number of sides of your shape: "))
if shape == 3: 
    print("Triangle")
if shape == 4: 
    print("Square")
if shape == 5: 
    print("Pentagon")
if shape == 6: 
    print("Hexagon")
if shape == 7: 
    print("Heptagon")
if shape == 8: 
    print("Octagon")
if shape == 9:
    print("Nonagon")
if shape == 10:
    print("Decagon")
else:
    print("your shape side has to be between 3 and 10")
    
print(f"your shape is a {shape}")

#38: 

month = input("Enter your month: ")

if month == "January" or month == "March" or month == "May" or month == "July" or month == "August" or month == "October" or month == "December":
    print("Your month has 31 days")
elif month == "April" or month == "June" or month == "September" or month == "November":
    print("Your month has 30 days")
elif month == "February":
    print("Your month has 28 and 29 on leap years")
    
#39:
    
sound_level = int(input("What is your sound level decibels?: "))

if sound_level == 130:
    print("Your sound level is as loud as a Jackhammer")
if sound_level == 106:
    print("Your sound level is as loud as a Gas lawnmower")
if sound_level == 70:
    print("Your sound level is as loud as a Alarm clock")
if sound_level == 40:
    print("Your sound level is as loud as a Quiet room")
if (107 <= sound_level <= 129):
    print("Your sound level is between Jackhammer and Gas lawnmower")
if (71 <= sound_level <= 105):
    print("Your sound level is between Gas lawnower and Alarm clock")
if (41 <= sound_level <= 69):
    print("Your sound level is between Alarm clock and Quiet room")
if sound_level > 130:
    print("Your sound level is louder than a jackhammar")
if sound_level < 40:
    print("Your sound level is quieter than a silent room")
    
#40:

side1 = int(input("What is the length of side 1 of your triangle: "))
side2 = int(input("What is the length of side 2 of your triangle: "))
side3 = int(input("What is the length of side 3 of your triangle: "))
print("\n")
if side1 == side2 == side3:
    print("Your triangle is an Equilateral Triangle")
if side1 == side2 or side1 == side3 or side2 == side3:
    print("Your triangle is an Isosceles Triangle")
else:
    print("Your triangle is a Scalene Triangle")
    
#43:
    
bill = int(input("How much is your bill worth: $"))

print(" ")
if bill == 1:
    print("The person on your bill is George Washington")
if bill == 2:
     print("The person on your bill is Thomas Jefferson")
if bill == 5:
    print("The person on your bill is Abraham Lincoln")
if bill == 10:
   print("The person on your bill is Alexander Hamilton")
if bill == 20:
   print("The person on your bill is Andrew JAckson")
if bill == 50:
   print("The person on your bill is Ulysses S. Grant")
if bill == 100:
   print("The person on your bill is Benjamin Franklin")
else:
    print("Your bill must be in the range of 1 to 100 dollars")
    
#44

month = input("What month is your holiday in?: ")
if month == "January":
    day = int(input("What day is your holiday in?: "))
if day == 1:
    print("Your holiday is New Years")
else:
    print("Your holiday does not exist:(")
elif month == "July":
    day = int(input("What day is your holiday in?: "))
if day == 1:
    print("Your holiday is Canada Day")
else:
    print("Your holiday doesn't exist:(")
elif month == "December":
    day = int(input("What day is your holiday in?: "))
if day == 25:
    print("Your holiday is Christmas, my favourite")
else:
    print("Your holiday does not exist:(")
else:
    print("This month does not have a holiday with consistant date.")
  
#45

letter = input("What is the letter on the horizontal axis?: ")
if letter == "a" or letter == "c" or letter == "e" or letter == "g":
    number = int(input("What is the letter on the vertical axis?: "))
if (number % 2) == 0:
    print("The colour of your square is white")
elif number > 8:
    print("Please type in the proper number and letter")
else:
    print("The colour of your square is black")
if letter == "b" or letter == "d" or letter == "f" or letter == "h":
    number = int(input("What is the letter on the vertical axis?: "))
if (number % 2) == 0:
    print("The colour of your square is black")
elif number > 8:
    print("Please type in the proper number and letter")
else:
    print("The colour of your square is white")

#1
name = input("Enter name: ")
print(f"Hi {name!")

#2
str_1 = input("Enter a string: ")
str_2 = input("Enter a second string: ")
print(str_1 + str_2 + str_2 + str_1)

#3
out_str = input("Enter an out string of length 4: ")
word = input("Enter a word: ")
print(out_str[0] + out_str[1] + word + out_str[2] + out_str[3])

#4
            
str = input("Enter a word: ")
last_char = str[-1]
second_last_char = str[-2]
print(second_last_char + last_char + second_last_char + last_char + second_last_char + last_char)

#5

str = input("Enter a string: ")
print(str[1:-1])

#6

str_1 = input("Enter a string: ")
str_2 = input("Enter a second string: ")
str_1_omitted = str1[1:-1] + str_1[-1]
str_2_omitted = str2[1:-1] + str_2[-1]
print(str_1_omitted + str_2_omitted)

#7

str = input('Enter a string: ')
first_two_char = str[0] + str [1]
end = str[2:-1] + str [-1]
print(end + first_two_char)

#8

str = input("Enter a string: ")
last_two_char = str[-2] + str[-1]
front = str[0:-2]
print(last_two_char + front)

#9

str = input("Enter a string: ")
if str[-2] == "l" and str[-1] == "y":
    print("True")
else:
    print("False")

#10

str_1 = input("Enter a string: ")
str_2 = input("Enter a second string: ")
if str_1[-1] == str_2[0]:
    print(str_1[0:-1] + str_2)
else:
    print(str_1 + str_2)
