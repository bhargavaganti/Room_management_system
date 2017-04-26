"""
Name : room management system.
Author : benjamin wacha
Email: bmwachajr@gmail,com
Descrption: a system to randomly allocate rooms to andela staff and fellows.
"""
import unittest
from unittest import TestCase
from RoomMgt import Dojo
from Person import Person, Staff, Fellow

class TestCreateRoom(unittest.TestCase):
  def SetUp():
    dojo = dDjo()
    
  
  def test_create_room_successfully(self):
    dojo = Dojo()
    initial_room_count = len(dojo.all_rooms)
    blue_office = dojo.create_room("Blue", "office")
    self.assertTrue(blue_office)
    new_room_count = len(dojo.all_rooms)
    self.assertEqual(new_room_count - initial_room_count, 1)
    
  def test_create_multiple_offices_successfully(self):
    dojo = Dojo()
    initial_room_count = len(dojo.all_rooms)
    blue_office = dojo.create_room("Blue","Black","Brown", "office")
    self.assertTrue(blue_office)
    new_room_count = len(dojo.all_rooms)
    self.assertEqual(new_room_count - initial_room_count, 1)
    
  def test_create_multiple_livingspace_successfully(self):
    dojo = Dojo()
    initial_room_count = len(dojo.all_rooms)
    blue_office = dojo.create_room("Blue","Black","Brown", "livingspace")
    self.assertTrue(blue_office)
    new_room_count = len(dojo.all_rooms)
    self.assertEqual(new_room_count - initial_room_count, 1)

  def test_create_room_name_with_no_name(self):
    dojo = Dojo()
    with self.assertRaises(RuntimeError) as context:
      empty_office = dojo.create_room("","")
      self.assertEqual(
          'Couldnt create Room.',
          context.exception.message,
          'Both Room Name and Room Type must be given'
      )
      
  def test_create_room_type_not_given(self):
    dojo = Dojo()
    with self.assertRaises(RuntimeError) as context:
      no_type_office = dojo.create_room("no_type", "")
      self.assertEqual(
          'Couldnt create Room.',
          context.exception.message,
          'Both Room Name and Room Type must be given'
      )
      
  def test_office_room_adds_to_office_list(self):
    dojo = Dojo()
    initial_room_count = len(dojo.all_rooms)
    red_office = dojo.create_room("Red", "office")
    self.assertTrue(red_office)
    new_room_count = len(dojo.all_rooms)
    self.assertEqual(new_room_count - initial_room_count, 1)
      
  def test_living_space_adds_to_livngSpace_list(self):
    dojo = Dojo()
    initial_room_count = len(dojo.livingspace_list)
    red_livingspace = dojo.create_room("Red", "livingspace")
    self.assertTrue(red_livingspace)
    new_room_count = len(dojo.livingspace_list)
    self.assertEqual(new_room_count - initial_room_count, 1)
    
  def test_adds_Staff_successfully(self):
    dojo = Dojo()
    blue_office = dojo.create_room("Blue","Black","Brown", "office")
    Staff_Henry = Staff(dojo, "staff", "Henry")
    self.assertTrue(Staff_Henry)
    self.assertEqual(Staff_Henry.name, "Henry", msg='Name should be Henry')
    self.assertEqual(Staff_Henry.office_space, True, msg='No office allocated')
  """
  def test_creates_Fellow_successfully(self):
    dojo = Dojo()
    multiple_offices = dojo.create_room("Blue","Black","Brown", "livingspace")
    fellow_Albert = Fellow("Fellow", "Albert", "Y")
    self.assertEqual(fellow_Albert.name, "Albert", msg='Name should be Henry')
    self.assertEqual(fellow_Albert.wants_accomodation, "Y", msg='Name should be Albert')
"""
if __name__ == "__main__":
  unittest.main()