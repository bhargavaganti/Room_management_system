"""
Name        :  Room Allocation system.
Author      :  Benjamin Wacha
Github      :  @bmwachajr
Descrption  :  This is a system used to randomly allocate rooms to new Staff and Fellows at Andela
"""
import sys

class Room(object):
  """
  Rooms at The Dojo
  Attributes:
  Room name
  Room type
  Room Occupants
  """
  def __init__(self, room_name, room_type):
    self.name = room_name
    self.occupants = []
  
class livingspace(Room):
  """Living space instance at the dojo"""
  max_people = 4
  
  def __init__(self, room_name, room_type):
    self.name = room_name
    self.type = room_type
    self.occupants= []
    
class office(Room):
  """office instance at the dojo"""
  
  def __init__(self, room_name, room_type):
    selfmax_people = 6
    self.name = room_name  
    self.type = room_type
    self.occupants= []