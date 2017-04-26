"""
Name        :  Room Allocation system.
Author      :  Benjamin Wacha
Github      :  @bmwachajr
Descrption  :  This is a system used to randomly allocate rooms to new Staff and Fellows at Andela
"""
import sys
import random
from  Room import Room

class Dojo(object):
  """This is a class for an Andela Kenya Campus called The Dojo"""
  
  """Dojo constructor"""
  def __init__(self):
    self.office_list = []
    self.all_rooms = []
    self.livingspace_list = []
  
  
  def create_room(self, *args):
    """Create a room object
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
      elif (room_type == "office"):
        room_object = (room_name + "_" + room_type)
        room_object = Room(room_name, room_type)
        self.office_list.append(room_object)
        self.all_rooms.append(room_object)
        
        return room_object
      
      #if Room is a living space, Create living space object
      elif(room_type == "livingspace"):
        room_object = room_name + "_" + room_type
        room_object = Room(room_name, room_type)
        self.livingspace_list.append(room_object)
        self.all_rooms.append(room_object)
        
        return room_object
    
    #Creating multiple rooms at the Dojo
    if len(args) > 2:
      room_type = args[-1]
      room_group = args[0: -1]#list of names
      
      for room in room_group:
        room_object = room + "_" + room_type
        room_object = Room(room, room_type)

        if (room_type == "office"):
          self.office_list.append(room_object)
        
        if(room_type == "livingspace"):
          self.livingspace_list.append(room_object)
          
        self.all_rooms.append(room_object)
        
        return room_object
        
  def allocate_livingspace(self, fellow):
    """This method allocates a random room to a fellow"""
    
    room = random.choice(self.livingspace_list)
    #if fellow wants living space
    if fellow.wants_accomodation == None:
      fellow.livingspace = None
    
    #if occupants < rooms max people
    if len(room.occupants) < room.maxxpeople:
      room.occupants.append(fellow)
      fellow.livingspace.append(room)
      
  def allocate_office(self, person):
    """This method allocates a random office to a both staff and fellows"""
    
    room = random.choice(self.office_list)
    #if fellow wants living space
    room.occupants.append(person)
    person.livingspace.append(room)
  