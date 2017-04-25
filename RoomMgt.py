"""
Name        :  Room Allocation system.
Author      :  Benjamin Wacha
Github      :  @bmwachajr
Descrption  :  This is a system used to randomly allocate rooms to new Staff and Fellows at Andela
"""
import sys

class Dojo(object):
  """This is a class for an Andela Kenya Campus called The Dojo"""
  
  """Dojo constructor"""
  def __init__(self):
    self.all_employees = []#list of employees at Dojo
    self.all_rooms = []
  
  
  def create_room(self, *args):
    """Create a new room object
      Attributes: room_name, room_type
    """
    
    #When only one room is created
    if len(args) == 2:
      room_name = args[0]
      room_type = args[1]
      
      #If  the room_name or type is empty, Raise RunTime Error
      if (room_name == "") or (room_type == ""):
        raise RuntimeError("Couldnt create Room, both Room Name and Room Type needed")
      
      #if Room is an office, Create office object
      elif room_type == "office":
        room_object = (room_name + "_" + room_type)
        room_object = Room(room_name, room_type)
        self.all_rooms.append(room_object)
        
        return room_object
      
      #if Room is a living space, Create living space object
      elif(room_type == "living space"):
        room_object = room_name + "_" + room_type
        room_object = Room(room_name, room_type)
        self.all_rooms.append(room_object)
        
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
      
  