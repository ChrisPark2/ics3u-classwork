#1 Create a program that will ask the user for their favourite colour. Have the program output a message saying something like: "Blue?! No why, that's my favourite colour too!".
colour = input ("what is your favourite colour? ")
print ("wow really thats a really cool colour.")

#2 Create a program that asks how many cans come in a pack. Then ask the user how many packs there are. Output a message indicating the total number of cans.
cansinapack = int(input("How many cans are in a pack? "))
packs = int(input("how many packs do you have? "))
print("The total number of cans is", cansinapack * packs)

#3 Ask the user for the three dimensions of a rectangular prism. Output the volume
length = int(input("what is the length of the rectangular prism in cm? "))
width = int(input("What is the width of the rectangular prism in cm? "))
height = int(input("What is the height of the rectangular prism in cm? "))
print("The volume of the rectangular prism is", length * width * height, "cm squared")
