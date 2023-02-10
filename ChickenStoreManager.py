from ChickenOrder import ChickenOrder


class ChickenStoreManager():

  def __init__(self):
    self.order_list = []

  def insert_order(self):

    submitted_order = []
    for order in range(len(self.order_list)):
      if self.order_list[order].get_status() == "SUBMITTED":
        submitted_order.append(self.order_list[order])
        
    if len(submitted_order) >=5:
      print('Sorry we are too busy at the moment.')
      return
      
    n_chickens = int(input("How many chicken:"))
    n_fries = int(input("How many fries:"))
    order = ChickenOrder(n_chickens,n_fries)
    self.order_list.append(order)
    print(f'Your order is number {len(self.order_list)-1}')

    waiting_time = 0
 
    for i in range(len(submitted_order)):
      chicken = submitted_order[i].get_n_chickens()
      fries = submitted_order[i].get_n_fries()
      order_time = (chicken*2) + (fries*1)
      waiting_time += order_time
      print(f'i:{i},chichen:{chicken},fries:{fries},waiting time:{waiting_time}')
      print(submitted_order[i])

    print(f'You have to wait {waiting_time} minutes.')
    

  def display_n_submitted(self):
    n = 0
    for x in range(len(self.order_list)-1):
      if self.order_list[x].get_status() == "SUBMITTED":
        n+=1
    print(f'There are {n} submitted orders at the moment.')

    
  def display_n_ready(self):
    n = 0
    for x in range(len(self.order_list)-1):
      if self.order_list[x].get_status() == "READY":
        n+=1
    print(f'There are {n} ready orders at the moment.')

    
  def display_n_delivered(self):
    n = 0
    for x in range(len(self.order_list)-1):
      if self.order_list[x].get_status() == "DELIVERED":
        n+=1
    print(f'{n} orders have been delivered so far.')

    
  def display_status(self,idx_order=0):
    print(f'Order {idx_order} is {self.order_list[idx_order].get_status()}')

    
  def set_ready(self,idx_order=0):
    if self.order_list[idx_order].get_status() == "SUBMITTED":
      self.order_list[idx_order].set_ready()

      
  def set_delivered(self,idx_order=0):
    if self.order_list[idx_order].get_status() == "READY":
      self.order_list[idx_order].set_delivered()

      
  def print_order_list(self):
    for x in range(len(self.order_list)):
      print(x,self.order_list[x])
