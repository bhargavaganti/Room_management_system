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
        self.office = dojo.allocate_office()
        self.livingspace = dojo.allocate_livingspace(
      print(self.wants_accomodation)
      return self

  def allocate_office(self):
    print(Dojo.all_rooms)
    self.office = 'office';
    return bool(self.office)
    
  def allocate_livingSpace(self, livingSpace):
    self.office = livingSpace;
    
class Staff(Person):
  """
    Staff member at andela.     
    Atrributes:
    office_space
    
  """
  pass

        

class Fellow(Person):
  """ Fellow at andela. Atrributes: office_space, wants_accomodation,   living_space
  """
  def __init__(self):
    self.wants_accomodation = None
    
 