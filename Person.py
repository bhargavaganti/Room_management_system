"""
  Name : room management system.
  Authr : benjamin wacha
  Email: bmwachajr@gmail,com
  Descrption: a system to randomly allocate rooms to andela staff and fellows.
"""

import sys
from RoomMgt import Dojo, Room

class Person(object):
  """ person at the Dojo"""
  def __init__(self, person_name):
    self.person_name = person_name
    
  def add_person(self, *args):
    """Adding a new person at the dojo"""
    person_type = args[0]
    self.person_name = args[1]
    
    #if the person is a staff, create staff instance
    if len(args) == 2:
      person_name = Staff()
      return self
      
    #if the person is a fellow, create Fellow instance
    elif len(args) == 3:
      wants_accomodation = args[2]
      self.wants_accomodation = wants_accomodation
      print(self.wants_accomodation)
      return self
      
    def allocate_office(self, office):
      self.office = office;
      
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
  def __init__(self, wants_accomodation):
    self.wabts_accomodation = wants_accomodation
    
    #self.wants_accomodation = wants_accomodation
    if self.wants_accomodation == "Y":
      self.living_space = random_LivingSpace()
    else:
      self.living_space = False
    
 