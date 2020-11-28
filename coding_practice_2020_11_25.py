#34

number = int(input("Enter an integer here: "))

if (number % 2) == 0: 
    print("\nThis is an even number obviously")
else: 
    print("\nThis is an odd number you dummy")


#35:

years = int(input("Please enter dog's age in human years: "))

if (0 <= years <= 2):
    child = 10.5 * years
    print(f"Your dog is {child} years old.")

if years > 2:
    (adult) = 21 + 4 * (years - 2)
    print(f"Your dog is {adult} years old.")

elif years < 0:
    print("Unavailable number, try again.")
    
    
#36:

letter = input("Please enter a letter of the alphabet: ")

if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
    print("Vowel")
elif letter == "y":
    print("Vowel when it feels like being a vowel")
else:
    print("Consonant")
    
#37:

shape = int(input("Number of sides of the shape: "))
print("")
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
    
#38: 

month = input("Enter your month: ")

if month == "January" or month == "March" or month == "May" or month == "July" or month == "August" or month == "October" or month == "December":
    print("31 days")
elif month == "April" or month == "June" or month == "September" or month == "November":
    print("30 days")
elif month == "February":
    print("28, 29 on leap years")
    
#39:
    
decibal = int(input("What is your sound level (dB)?: "))

if decibal == 130:
    print("Jackhammer")
if decibal == 106:
    print("Gas lawnmower")
if decibal == 70:
    print("Alarm clock")
if decibal == 40:
    print("Quiet room")

if (107 <= decibal <= 129):
    print("Between Jackhammer and Gas lawnmower")
if (71 <= decibal <= 105):
    print("Between Gas lawnower and Alarm clock")
if (41 <= decibal <= 69):
    print("Between Alarm clock and Quiet room")
if decibal > 130:
    print("That's a really loud sound, please be cautious")
if decibal < 40:
    print("Very quiet sound, where even are you")
    
#40:

side1 = int(input("What is the length of side 1: "))
side2 = int(input("What is the length of side 2: "))
side3 = int(input("What is the length of side 3: "))
print("\n")



if side1 == side2 == side3:
    print("Equilateral Triangle")
if side1 == side2 or side1 == side3 or side2 == side3:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")
    
#43:
    
banknote = int(input("How much is your banknote worth: $"))

print(" ")
if banknote == 1:
    print("The face on the banknote is George Washington")
if banknote == 2:
     print("The face on the banknote is Thomas Jefferson")
if banknote == 5:
    print("The face on the banknote is Abraham Lincoln")
if banknote == 10:
   print("The face on the banknote is Alexander Hamilton")
if banknote == 20:
   print("The face on the banknote is Andrew JAckson")
if banknote == 50:
   print("The face on the banknote is Ulysses S. Grant")
if banknote == 100:
   print("The face on the banknote is Benjamin Franklin")
else:
    print("Error, no such banknote exists.")
    
#44

month = input("What month is your holiday in?: ")

if month == "January":
    day = int(input("What is the day of your holiday month?: "))
    if day == 1:
            print("New year's Day. Happy New Year!!")
    else:
            print("Not a holiday :(")
elif month == "July":
    day = int(input("What is the day of your holiday month?: "))
    if day == 1:
        print("Canada Day. Woo!")
    else:
        print("Not a holiday :(")
    
elif month == "December":
    day = int(input("What is the day of your holiday month?: "))
    if day == 25:
        print("Christmas. Merry Christmas!!")
    else:
        print("Not a holiday :(")

else:
    print("This month does not have a holiday with fixed date.")
  
#45

letter = input("What is the letter on the horizontal axis?: ")

if letter == "a" or letter == "c" or letter == "e" or letter == "g":
    number = int(input("What is the letter on the vertical axis?: "))
    if (number % 2) == 0:
            print("The colour of your square is white")
    elif number > 8:
            print("Error, please try again")
    else:
            print("The colour of your square is black")

if letter == "b" or letter == "d" or letter == "f" or letter == "h":
    number = int(input("What is the letter on the vertical axis?: "))
    if (number % 2) == 0:
            print("The colour of your square is black")
    elif number > 8:
            print("Error, please try again")
    else:
            print("The colour of your square is white")
