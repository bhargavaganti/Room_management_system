"""
  name : room management system.
  authr : benjamin wacha
  email: bmwachajr@gmail,com
  descrption: a system to randomly allocate rooms to andela staff and fellows.

"""

class Person(object):
  def __init__(self):
    self.person_name = ''
    
  def add_person(self, person_type, person_name):
    #if the person is a staff, create staff instance
    if person_type == "Staff":
      self.person_name = person_name
      person_name = Staff()
      return self
      
    #if the person is a staff, create Fellow instance
    elif person_type == "Fellow":
      self.person_name = person_name
      person_name = fellow()
      return self

class Staff(Person):
  """
    Staff member at andela.
    
    atrributes:
      office_space
      
  """
  def __init__(self):
    self.office = ""

        

class Fellow(Person):
  """
    Fellow at andela.
    
    atrributes:
      office_space
      wants_accomodation
      living_space
      
  """
  def __init__(self):
    self.office_space = ""
    self.wants_accomodation = ""
    if wants_accomodation == "Y":
      self.living_space = ""
    else:
      self.living_space = ""
    
 