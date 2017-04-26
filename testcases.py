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
    self.assertEqual(new_room_count - initial_room_count, 3)
    
  def test_create_multiple_livingspace_successfully(self):
    dojo = Dojo()
    initial_room_count = len(dojo.all_rooms)
    blue_office = dojo.create_room("Blue","Black","Brown", "livingspace")
    self.assertTrue(blue_office)
    new_room_count = len(dojo.all_rooms)
    self.assertEqual(new_room_count - initial_room_count, 3)

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
    dojo.create_room("Blue","Black","Brown", "office")
    Staff_Henry = dojo.add_person("Staff", "Henry")
    self.assertTrue(Staff_Henry)
    self.assertEqual(Staff_Henry.name, "Henry", msg='Name should be Henry')
    self.assertNotEqual(Staff_Henry.office, None, msg='No office allocated')

  def test_creates_Fellow_successfully(self):
    dojo = Dojo()
    multiple_offices = dojo.create_room("Blue","Black","Brown", "office")
    multiple_livingspaces = dojo.create_room("Blue","Black","Brown", "livingspace")
    fellow_Albert = dojo.add_person("Fellow", "Albert", "Y")
    self.assertEqual(fellow_Albert.name, "Albert", msg='Name should be Henry')
    self.assertNotEqual(fellow_Albert.livingspace, None, msg='Name should be Albert')
    self.assertNotEqual(fellow_Albert.office, None, msg='Name should be Albert')
    
  def test_creates_Fellow_with_no_accomodation_successfully(self):
    dojo = Dojo()
    multiple_offices = dojo.create_room("Blue","Black","Brown", "office")
    multiple_livingspaces = dojo.create_room("Blue","Black","Brown", "livingspace")
    fellow_Albert = dojo.add_person("Fellow", "Albert")
    self.assertEqual(fellow_Albert.name, "Albert", msg='Name should be Henry')
    self.assertEqual(fellow_Albert.livingspace, None, msg='Name should be Albert')
    self.assertNotEqual(fellow_Albert.office, None, msg='Name should be Albert')

  def test_checks_occupants_in_room(self):
    dojo = Dojo()
    living_space = dojo.create_room("Brown", "livingspace")
    office = dojo.create_room("Brown", "office")
    fellow1 = dojo.add_person("Fellow", "Albert", "Y")
    fellow2 = dojo.add_person("Fellow", "Arthur", "Y")
    fellow3 = dojo.add_person("Fellow", "Albino", "Y")
    fellow4 = dojo.add_person("Fellow", "Benjamin", "Y")
    self.assertEqual(dojo.get_occupants("Brown"), ['Albert', 'Arthur', 'Albino', 'Benjamin'], msg='Couldnot get occupants')

if __name__ == "__main__":
  unittest.main()