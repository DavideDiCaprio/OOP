'''
Implement the class Cashier, which computes bills for the customers of a shop. The class has
the following behaviour:

1. It stores a dictionary matching products and prices, the dictionary has the following
   structure: {product_identifier: product_price}.
2. It provides the method add_product(product_id, product_price) which allows to add a new
   product to the products dictionary. NOTE: if the product_id is already present, the price
   is updated with the most recent product_price.
3. It provides the method display_n_products() which prints the number of products stored in
   the dictionary.
4. It provides the method get_bill(basket). The method get_bill takes as input the dictionary
   basket, with the following structure: {product_id: product_amount} and prints the total
   bill. 
   An entry {'mosquito_spray': 3} in the basket means that the customer has bought 3 items
   with the id 'mosquito_spray'.
   In order to compute the bill, the amount of each product needs to be multiplied by its
   price and this quantity should be summed up for all the products.
5. It provides the method get_bill_verbose(basket). This method works exactly like get_bill,
   with the exception that the computations are displayed row by row. Look at the examples
   below for more clarity.

*NOTE*: If a product in basket is not present in the products dict, the bill cannot be
        calculated. Therefore the message 'Sorry, we don't have the product: {product_id}'
        should be displayed to the user.

Examples:
```
cashier = Cashier()

cashier.add_product(product_id='mosquito_spray', product_price=1.5)
cashier.add_product(product_id='mosquito_sting_relief', product_price=3.5)

cashier.display_n_products() # prints: 'I have 2 products registered.'

basket = {'mosquito_sting_relief': 2, 'mosquito_spray': 1}
cashier.get_bill(basket=basket) # prints: 'You spent a total of 8.5'.

cashier.get_bill_verbose(basket=basket)
# prints:
#  mosquito_sting_relief: 3.5 x 2 = 7
#  mosquito_spray’: 1.5 x 1 = 1.5.
#  ___________________________
#  You spent a total of 8.5.

cashier.add_product(product_id='mosquito_sting_relief', product_price=3)
cashier.get_bill(basket=basket) # prints: 'You spent a total of 7.5'.

basket = {'mosquito_sting_relief': 2, popsicle: 1}
cashier.get_bill(basket=basket) # prints: 'Sorry, we don't have the product: popsicle'.
```
'''
class Cashier():
   def __init__(self):
      self.products_and_prices = {}
   
   def add_product(self, product_id, product_price):
      self.products_and_prices[product_id] = product_price
      
   def display_n_products(self):
      print(f'I have {len(self.products_and_prices)} products registered.')

   def get_bill(self, basket):
      bill = 0
      for x in basket.keys():
         if x not in self.products_and_prices:
            print(f"Sorry, we don't have the product: {x}")
            return
         bill += self.products_and_prices[x] * basket[x]
         print(f'You spent a total of {bill}')

   def get_bill_verbose(self, basket):
      bill = 0
      for x in basket.keys():
         if x not in self.products_and_prices:
            print(f"Sorry, we dont't have the product: {x}")
            continue
         bill += self.products_and_prices[x] * basket[x]
         print(f'{x} : {self.products_and_prices[x]} x {basket[x]}')
      print(f'You spent a total of {bill}')
