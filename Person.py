"""
  name : room management system.
  authr : benjamin wacha
  email: bmwachajr@gmail,com
  descrption: a system to randomly allocate rooms to andela staff and fellows.
"""

import sys

class Person(object):
  def __init__(self, person_name):
    self.person_name = person_name
    
  def add_person(self, *args):
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

class Staff(Person):
  """
    Staff member at andela.
    
    Atrributes:
      office_space
      
  """
  
  #assign staff an office space
  def __init__(self):
    self.office_space = ""

        

class Fellow(Person):
  """
    Fellow at andela.
    
    Atrributes:
      office_space
      wants_accomodation
      living_space
      
  """
  def __init__(self):
    #self.wants_accomodation = wants_accomodation
    self.office_space = ""
    self.wants_accomodation = 
    if self.wants_accomodation == "Y":
      self.living_space = ""
    else:
      self.living_space = ""
    
 