# This is an example project for replit and git!
import random

def question3():
  #get a number
  #Don't forget to convert the string into an integer
  num = int(input("Please enter a number! \n"))

  if num > 10:
    print("Your number is greater than 10.")

  elif num < 10:
    print("Your number is less than 10.")

  else:
    print("Your number is equal to 10.")

def example():
  my_list = []
  for i in range(10):
    pass
  for i in range(len(my_list)):
    pass

def question6():
  #Write a program that uses a loop fill an empty list with 10 numbers 
  num_lst = []
  num_lst2 = []
  num_lst3 = []
  for i in range(10):
    #The numbers can be random or simply put 
    #in the numbers 0-9 
    #or 1-10 in ascending order 
    num_lst.append(i)
    num_lst2.append(i +1)

    num_lst3.append(random.randint(1,10))
    
  
  #and prints the list to the console. 
  print(num_lst)
  print(num_lst2)
  print(num_lst3)

  
def main():
  #question3()
  question6()
  pass

if __name__ == "__main__":
  main()
