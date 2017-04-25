"""
  Name : room management system.
  Authr : benjamin wacha
  Email: bmwachajr@gmail,com
  Descrption: a system to randomly allocate rooms to andela staff and fellows.
"""

import sys
from RoomMgt import Dojo, Room

class Person(object):
  """Object of everbody at the Dojo"""
  def __init__(self, args):
    self.name = args[0]
    self.type = args[1]
      
    
  def add_person(self, *args):
    """Adding a new person to the dojo"""    
    #if the person is staff, create staff instance and allocate room
    self.name = args[0]
    self.type = args[1]
    
    #if Person is Staff, allocate office
    if self.type == "Staff":
      self.office = dojo.allocate_office()
      return self
      
    #if Person is employee, allocate office and living space(optionall)
    elif self.type = "Fellow":
      wants_accomodation = args[-1]
      if args[-1] == "Y"
        dojo.allocate_office(self)
        dojo.allocate_livingspace(self)
        
        return self
      else:
        self.office = dojo.allocate_office()
        self.livingspace = None
        return self
    
class Staff(Person):
  """Staff member at andela. Attributes, First name Last name Type"""
  def __init__(self, args):
    self.name = str(args[0]) + " " + str(args[1])
    self.type = args[2]

        

class Fellow(Person):
  """ Fellow at andela. Atrributes: office_space, wants_accomodation,   living_space"""
  def __init__(self, *args):
    self.name = args[0]
    self.wants_accomodation = None
    
 