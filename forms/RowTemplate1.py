from anvil import *
import tables
from tables import app_tables
import anvil.server

class RowTemplate1(RowTemplate1Template):

  def __init__(self, **properties):
    # You must call self.init_components() before doing anything else in this function
    self.init_components(**properties)

    # Any code you write here will run when the form opens.