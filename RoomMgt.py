"""
  name : room management system.
  authr : benjamin wacha
  email: bmwachajr@gmail,com
  descrption: a system to randomly allocate rooms to andela staff and fellows.

"""
import sys

class Dojo(object):
  """This is the Dojo class, and andela facility"""
  
  all_rooms = []
  #initializa an empty list of all rooms
  def __init__(self):
    self.all_livingSpace = []
    self.all_offices = []
  
  
  def create_room(self, *args):
    """This method creates a room at the Dojo
      
    Attributes: room_name, room_type
    """
    #To create only a single room at the Dojo 
    if len(args) == 2:
      room_name = args[0]
      room_type = (args[1]).lower()
      
      #Donot create rooms at the dojo is name or type is empty
      if (room_name == "") or (room_type == ""):
        raise RuntimeError("Couldnt create Room, both Room Name and Room Type needed")
      
      elif(room_type == "office"):
        room_object = room_name + "_" + room_type
        room_object = Room(room_name, room_type)
        self.all_offices.append(room_object)
        self.all_rooms.append(room_object)
        print ("An " + room_type + " called " + room_name + " has been created successfully \n" )
        
        return room_object
      
      elif(room_type == "living space"):
        room_object = room_name + "_" + room_type
        room_object = Room(room_name, room_type)
        self.all_livingSpace.append(room_object)
        self.all_rooms.append(room_object)
        print ("An " + room_type + " called " + room_name + " has been created successfully \n" )
        
        return room_object
    
      
    #To create multiple rooms of the same type at the Dojo   
    if len(args) > 2:

      room_type = (args[len(args)-1]).lower()
      room_group = args[0:len(args)-1]
      
      for room_name in room_group:
        room_object = room_name + "_" + room_type
        room_object = Room(room_name, room_type)
        self.all_rooms.append(room_object)
        
        print ("An " + room_type + " called " + room_name + " has been created successfully \n" )
        
      return room_object
      
    def get_random_office(self):
      office = random.choice(self.all_offices)
      return office
      
    def get_random_livingSpace(self):
      livingSpace = random.choice(self.all_livingSpace)
      return livingSpace
      
  
class Room(object):
  """
  Rooms at The Dojo
  Attributes:
  Room name
  Room Occupants
  """
  def __init__(self, room_name, room_type):
    self.room_name = room_name
  
class livingSpace(Room):
  max_people = 4
    
class Office(Room):
  max_people = 6