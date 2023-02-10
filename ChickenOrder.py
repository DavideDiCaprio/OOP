class ChickenOrder():

  def __init__(self,n_chickens=0, n_fries=0):
    self.n_chickens = n_chickens
    self.n_fries = n_fries
    self.status = "SUBMITTED"

  def get_n_chickens(self):
    return self.n_chickens

  def get_n_fries(self):
    return self.n_fries

  def get_status(self):
    return self.status

  def set_ready(self):
    if self.status == "SUBMITTED":
      self.status = "READY"
    
  def set_delivered(self):
    if self.status == "READY":
      self.status = "DELIVERED"

  def __str__(self):
    return f"This is an instance of ChickenOrder with {self.n_chickens} chickens and {self.n_fries} fries."
