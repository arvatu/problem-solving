print("What is your name?")
n = input()
print("Do you have a dog? (type True or False)")
dog = input()
#bool is boolean datatype - only stores True/False
if len(n) > 9 and  dog == "True":
  print("You have a very loooong name!")
  print ("Your name contains {} letters".format(len(n)))
elif len(n) > 6 :
  print("your name is a bit long. CONSIDER A NICKNAME")
elif len(n) < 3 :
  print("your name is veery short") 
else:
  print("Your name is quite okay")
print("This is the END of the program!")
