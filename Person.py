"""
  Name : room management system.
  Authr : benjamin wacha
  Email: bmwachajr@gmail,com
  Descrption: a system to randomly allocate rooms to andela staff and fellows.
"""

import sys


class Person(object):
  """Object of everbody at the Dojo"""
  def __init__(self, *args):
    if len(args) > 1: 
      self.name = args[0]
      self.type = args[1]
      self.office = None
    
class Staff(Person):
  """Staff member at andela. Attributes, First name Last name Type"""
  def __init__(self, staff_type, staff_name):
    self.name = staff_name
    self.type = "Staff"
    self.office = ''

class Fellow(Person):
  """ Fellow at andela. Atrributes: office_space, wants_accomodation,   living_space"""
  def __init__(self, *args):
    self.type = "Fellow"
    self.name = args[1]
    self.livingspace = "None"
    
 