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
  def __init__(self, person_name):
    self.name = person_name
      
    
  def add_person(self, *args):
    """Adding a new person at the dojo"""
    person_type = args[0]
    self.person_name = args[1]
    
    #if the person is a staff, create staff instance
    if len(args) == 2:
      office = self.allocate_office()
      self.office_space = office
      return self
      
    #if the person is a fellow, create Fellow instance
    elif len(args) == 3:
      wants_accomodation = args[2]
      self.wants_accomodation = wants_accomodation
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
    
 