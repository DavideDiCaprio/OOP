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
