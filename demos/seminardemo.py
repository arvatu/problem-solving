print("Please chose  and option from menu:\n1-Nice message\n2-are of rectangle\n3-area of triangle\n4-times table")

option = int (input())
if option == 1:
  print("today willl be a good day")
elif option == 2:
  print("enter the lenght of the rectangle:")
  l = int(input())
  print("enter the width of the rectangle")
  w = int(input())
  area = w*1
  print("the area of thys rectangle was {}".format(area))
elif option == 3:
  print("enter the base of the triangle:")
  base = float(input())
  print("enter the height of the triangle")
  height = float(input())
  area = 0.5*base*height
  print("the area of thys triangle was {}".format(area))
elif option == 4:
  print("what number would you like to see times table for?")
  n = int(input())
  for i in range(1,11,1):

  print("{}x{} = {}".format(n,i.n*i))