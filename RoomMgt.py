 """
  name : room management system.
  authr : benjamin wacha
  email: bmwachajr@gmail,com
  descrption: a system to randomly allocate rooms to andela staff and fellows.

"""
class Dojo(object):
  """This is the Dojo class, and andela facility"""
  def __init__(self):
  self.all_rooms = []
  
class Room(object):
  """ 
      Rooms at The Dojo
      attributes:
      Room name
      Room Occupants
  """
  def __init__(self, room_name):
    self.room_name = room_name
    
