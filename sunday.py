import os
def Garreth():
       if os.path.exists("sunday.txt"):
              data = open("sunday.txt")
              for each_line in data:
                     print(each_line)

Garreth()