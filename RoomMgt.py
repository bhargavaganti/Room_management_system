"""
  name : room management system.
  authr : benjamin wacha
  email: bmwachajr@gmail,com
  descrption: a system to randomly allocate rooms to andela staff and fellows.

"""
class Dojo(object):
  """This is the Dojo class, and andela facility"""
  all_rooms = []
  #def __init__(self):
  
  def create_room(room_name, room_type):
    room_obj = room_name + "_" + room_type
    room_obj = Room(room_name, room_type)
    Dojo.all_rooms.append(room_obj)
    
    return room_obj
  
class Room(object):
  """ 
      Rooms at The Dojo
      attributes:
      Room name
      Room Occupants
  """
  def __init__(self, room_name, room_type):
    self.room_name = room_name
    
class livingSpace(Room):
  max_people = 4
    
class Office(Room):
  max_people = 6