"""
Name        :  Room Allocation system.
Author      :  Benjamin Wacha
Github      :  @bmwachajr
Descrption  :  This is a system used to randomly allocate rooms to new Staff and Fellows at Andela
"""

import sys
import cmd
from docopt import docopt, DocoptExit
import random
from  Room import Room, livingspace, office
from  Person import Person, Staff, Fellow

class Dojo():
  """This is a class for an Andela Kenya Campus called The Dojo"""
  
  """Dojo constructor"""
  def __init__(self):
    self.office_list = []
    self.all_rooms = []
    self.livingspace_list = []
    self.allocated_list = []
    self.people = []
  
  
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
        room_object = office(room_name, room_type)
        self.office_list.append(room_object)
        self.all_rooms.append(room_object)
        
        return room_object
      
      #if Room is a living space, Create living space object
      elif(room_type == "livingspace"):
        room_object = livingspace(room_name, room_type)
        self.livingspace_list.append(room_object)
        self.all_rooms.append(room_object)
        
        return room_object
    
    #Creating multiple rooms at the Dojo
    if len(args) > 2:
      room_type = args[-1]
      room_group = args[0: -1]#list of names
      
      for room in room_group:
        if room.lower() in self.all_rooms:
          retutn ("A Room with this name exists")
        else:
          room_object = Room(room, room_type)
          self.all_rooms.append(room_object)

          if (room_type == "office"):
            self.office_list.append(room_object)
          
          if(room_type == "livingspace"):
            self.livingspace_list.append(room_object)
            
          
      return room_object

  def add_person(self, *args):
    """Adding a new person to the dojo and allocate rooms"""
    person_type = (args[0]).lower()
    person_name = args[1]
    
    #if Person is Staff, add andallocate office
    if person_type == "staff":
      Staff_object = Staff(person_type, person_name)
      Staff_object.office = self.allocate_office(Staff_object)
      self.people.append(Staff_object)
      return Staff_object
      
      
    #if Person is employee, allocate office and living space(optionall)
    if person_type == "fellow":
      wants_accomodation = args[-1]

      Fellow_object = Fellow(person_type, person_name)
      Fellow_object.office = self.allocate_office(Fellow_object)
      
      if args[-1] == "Y":
        Fellow_object.livingspace = "".join(self.allocate_livingspace(Fellow_object))
  
      self.people.append(Fellow_object)
      return Fellow_object
        
  def allocate_livingspace(self, fellow):
    """This method allocates a random room to a fellow"""
    max_occupants = 4
    random_room = random.choice(self.livingspace_list)
    
    allocate = False
    while allocate == False:
      #if occupants < rooms max people
      if len(random_room.occupants) < max_occupants:
        allocate = True
         
    random_room.occupants.append(fellow)
    return random_room.name
      
  def allocate_office(self, person):
    """This method allocates a random office to a both staff and fellows"""
    max_occupants = 6
    allocate = False
    while allocate == False:
      random_room = random.choice(self.office_list)
      if len(random_room.occupants) < max_occupants:
        allocate = True
        
    random_room.occupants.append(person)
    return random_room.name
    
  def get_all_rooms(self):  
    return self.all_rooms
   
  def get_occupants(self, room_name):
    for room in self.all_rooms:    
      if ''.join(room.name) == ''.join(room_name):
        fellow_list = []
        for occupant in room.occupants:
          fellow_list.append(occupant.name)
        return fellow_list
        
  def get_allocated_rooms(self):
    allocated = []
    for room in self.all_rooms:
      if len(room.occupants) > 0:
        allocated.append(room)
    return allocated
    
    
  def get_room(self, room_name):
    print (room_name)
    for room in dojo.all_rooms:
      if room.name == room_name :
        return room
    return None
    
  def get_person(self, name):
    print(person_name)
    for person in self.people:
      if person.name == name :
        return person
    return None
  """    
  def reallocate_person(self, person_name, new_room):
    ""this method reallocates a person to a new room ""
    #find the New room
    for room in self.all_rooms:
      if room.name == ''.join(new_room) :
        #find the person
        for person in self.people:
          if person.name == ''.join(person_name):
            #find the current room
            for old_room in self.all_rooms:
              if old_room.name == room_name :
                old_room = old_room
              pass
            
            if room.type == "office" and room.type == old_room.type:
              person.office = room.type
              room.occupants.append(person.name)
              old_room.occupants.pop(person.name)
            
            if room.type == "livingspace" and room.type == old_room.type:
              person.livingspace = room.type
              room.occupants.append(person.name)
              old_room.occupants.pop(person.name) 
            
            return person
      
      return None
    else:
      raise ("Person or Room Not Found")
"""
      
   
 