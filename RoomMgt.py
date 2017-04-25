"""
  name : room management system.
  authr : benjamin wacha
  email: bmwachajr@gmail,com
  descrption: a system to randomly allocate rooms to andela staff and fellows.

"""
import sys

class Dojo(object):
  """This is the Dojo class, and andela facility"""
  def __init__(self):
    self.all_rooms = []
  
  def create_room(self, *args):
    #if a single room is created 
    if len(args) == 2:
      room_name = args[0]
      room_type = args[1]
      if (room_name == "") or (room_type == ""):
        raise RuntimeError("Couldnt create Room, both Room Name and Room Type needed")      
        return room_object
      
      else:
        room_object = room_name + "_" + room_type
        room_object = Room(room_name, room_type)
        self.all_rooms.append(room_object)
        print ("An " + room_type + " called " + room_name + " has been created successfully \n" )
        
        return room_object
    
  
      
    #is multiple rooms are created    
    if len(args) > 2:
      count = 0
      room_type = args[len(args)-1]
      while count < (len(args)-1):
        room_name = args[count]
        room_object = room_name + "_" + room_type
        room_object = Room(room_name, room_type)
        self.all_rooms.append(room_object)
        count += 1
        
        print ("An " + room_type + " called " + room_name + " has been created successfully \n" )
      return room_object
      
  
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