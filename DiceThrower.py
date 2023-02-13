'''
In this exercise you will implement the class DiceThrower, with the
following behaviour:

1. The class allows to throw a dice with n_faces faces, where n_faces
   is specified when the class is instantiated.
3. The class provides the method throw_dice() which trows a dice with
   n faces and prints the result.
4. The class provides the method trow_dice_n_times(n_times) which
   throws a dice n times and prints a list of results.
5. The class has an internal counter that records the number of total
   throws, it also provides a method display_total_n_throws() which
   prints the value of the counter.

Here is an example of usage:
```
thrower = DiceThrower(n_faces=5)
thrower.display_total_n_throws() # prints: 'The total number of throws is 0.'
thrower.throw_dice() # prints: 3
thrower.throw_dice() # prints: 2
thrower.display_total_n_throws() # prints: 'The total number of throws is 2.'
thrower.throw_dice() # prints: 5
thrower.trow_dice_n_times(n_times=3) # prints: [1, 2, 5]
thrower.display_total_n_throws() # prints: 'The total number of throws is 6.'
'''

import random

class DiceThrower():

  def __init__(self,n_faces=0):
    self.n_faces = n_faces
    self.total_n_throws = 0

  def throw_dice(self):
    outcome = random.randint(1,self.n_faces)
    self.total_n_throws +=1
    print(outcome)
    return outcome

  def trow_dice_n_times(self,n_times=0):
    self.list_of_outcome = []

    while len(self.list_of_outcome) != n_times:
      self.list_of_outcome.append(self.throw_dice())
    print(self.list_of_outcome)

  def display_total_n_throws(self):
    print(f'The total number of throws is {self.total_n_throws}')
