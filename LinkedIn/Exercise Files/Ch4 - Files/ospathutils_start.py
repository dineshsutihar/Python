#
# Example file for working with os.path module
#
import os
from os import path
import datetime
from datetime import date, time, timedelta
import time


def main():
  # Print the name of the OS
  print(f"Official Name of Windoes Operating System is: {os.name}")
  
  # Check for item existence and type
  print(f"Item exists: {str(path.exists('textfile.txt'))}")
  print(f"Item is a file: {path.isfile('textfile.txt')}")
  print(f"Item is a Diractory: {path.isdir('textfile.txt')}")
  
  # Work with file paths
  print(f"Item's path: {path.realpath('textfile.txt')}")
  print(f"Item's path and name: {path.split(path.realpath('textfile.txt'))}")
  
  # Get the modification time
  t = time.ctime(path.getmtime("textfile.txt"))
  print(t)
  print(datetime.datetime.fromtimestamp(path.getmtime("textfile.txt")))
  
  # Calculate how long ago the item was modified
  td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
  print(f"It has been {td} since the file was modified")
  print(f"Or, {td.total_seconds()} seconds")
  
if __name__ == "__main__":
  main()
