'''
In this exercise you will implement the class ListAvg, which stores a list of the
N most recent numbers (by insertion order) and their average. It has the following
behaviour:

1. The dimension N of the list is set by the user when the class is instantiated.
2. The class provides the method add_number(num) which adds a number to the list.
   If the list has N numbers already, the oldest number (by insertion order) must
   be dropped.
3. The class provides the method display_avg() which prints the average of the
   numbers in the list.
4. The class provides the method display_list() which displays the numbers in the
   list.

Example:
```
l = ListAvg(n=4)
l.add(1)
l.display_list() # prints [1]
l.add(1)
l.display_avg() # prints 1
l.add(2)
l.add(2)
l.display_avg() # prints 1.5
l.display_list() # prints [1, 1, 2, 2]
l.add(0)
l.add(4)
l.display_avg() # prints 2
l.display_list() # prints [2, 2, 0, 4]
```
'''

class  ListAvg():
   
  def __init__(self, n=0):
   self.max_dimension_list = n
   self.list_of_recent_numbers = []
   
   
  def add_number(self, num):
   if self.max_dimension_list != len(self.list_of_recent_numbers):
      self.list_of_recent_numbers.append(num)
    else:
      self.list_of_recent_numbers.pop(-1)
      #stuck at this point

      
  def display_avg(self):
   sum_numbers = 0

    for n in self.list_of_recent_numbers:
      sum_numbers +=n
    average = sum_numbers / len(self.list_of_recent_numbers)
    print(average)
      

  def display_list(self):
   print(self.list_of_recent_numbers)
