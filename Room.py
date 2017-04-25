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
  Room Occupants
  """
  def __init__(self, room_name, room_type):
    self.room_name = room_name
  
class livingSpace(Room):
  max_people = 4
    
class Office(Room):
  max_people = 6