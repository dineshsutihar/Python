#
# Example file for working with date information
#
from datetime import date
from datetime import time
from datetime import datetime

def main():
  ## DATE OBJECTS
  # Get today's date from the simple today() method from the date class
  today= date.today()
  print("Today date is :",today)

  # print out the date's individual components
  print("Date Component: ", today.day, today.month, today.year)
  
  # retrieve today's weekday (0=Monday, 6=Sunday)
  print("Today week day no is: ",today.weekday())
  days=["Mon", "Tue", "wed", "thu", "fri","sat","sun"]
  print("Which is a: ", days[today.weekday()])

  ## DATETIME OBJECTS
  # Get today's date from the datetime class
  today=datetime.now()
  print(today)
  
  # Get the current time
  t=datetime.time(datetime.now())
  print(t)
 

  
if __name__ == "__main__":
  main();
  