'''Implement the class SmallestNNumbers that has the following behaviour:
1. The class stores a list of N numbers, where N is given at the moment the class is istantiated. At the beginning, the class is empty.
2. The class provides a method add_number(next_num) that allows a user to add a number to the list.
3. The list of numbers stored in the class has two properties: first, it does not have duplicates; second, it only stores the smallest N numbers, therefore if the list has N numbers, and a new one is added, the biggest must be dropped.
4. The class provides the method print_list() that will print the list of numbers.

Here is an example of usage:

snn = SmallestNNumbers(n=3)
snn.print_list() # prints ‘[]’
snn.add_number(next_num=3)
snn.print_list() # prints ‘[3]’
snn.add_number(next_num=2)
snn.add_number(next_num=2)
snn.print_list() # prints ‘[2, 3]’
snn.add_number(next_num=1)
snn.add_number(next_num=0)
snn.print_list() # prints ‘[0, 1, 2]’
snn.add_number(next_num=5)
snn.print_list() # prints ‘[0, 1, 2]’ '''


class SmallestNNumbers():

  def __init__(self,n=0):
  
    self.n_numbers = []
    self.n = n
    
  def add_number(self,next_num=0):

    if next_num in self.n_numbers:
      return

    self.n_numbers.append(next_num)
    if len(self.n_numbers) > self.n:
      max = 0
      for i in range(len(self.n_numbers)):
        if self.n_numbers[i] > max:
          max += self.n_numbers[i]
          idx = i 
      self.n_numbers.pop(idx) 

      
  def print_list(self):
    print(self.n_numbers)
