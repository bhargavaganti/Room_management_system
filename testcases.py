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
  def setUp(self):
    self.dojo = Dojo()
    
  def test_create_room_successfully(self):
    initial_room_count = len(self.dojo.all_rooms)
    blue_office = self.dojo.create_room("Blue", "office")
    self.assertTrue(blue_office)
    new_room_count = len(self.dojo.all_rooms)
    self.assertEqual(new_room_count - initial_room_count, 1)
    
  def test_create_multiple_offices(self):
    initial_room_count = len(self.dojo.all_rooms)
    blue_office = self.dojo.create_room("Blue","Black","Brown", "office")
    self.assertTrue(blue_office)
    new_room_count = len(self.dojo.all_rooms)
    self.assertEqual(new_room_count - initial_room_count, 3)
    
  def test_create_multiple_livingspace(self):
    initial_room_count = len(self.dojo.all_rooms)
    blue_office = self.dojo.create_room("Blue","Black","Brown", "livingspace")
    self.assertTrue(blue_office)
    new_room_count = len(self.dojo.all_rooms)
    self.assertEqual(new_room_count - initial_room_count, 3)

  def test_create_nameless_room(self):
    with self.assertRaises(RuntimeError) as context:
      empty_office = self.dojo.create_room("","")
      self.assertEqual(
          'Couldnt create Room.',
          context.exception.message,
          'Both Room Name and Room Type must be given'
      )
      
  def test_adds_room_to_office_list(self):
    initial_room_count = len(self.dojo.all_rooms)
    red_office = self.dojo.create_room("Red", "office")
    self.assertTrue(red_office)
    new_room_count = len(self.dojo.all_rooms)
    self.assertEqual(new_room_count - initial_room_count, 1)
      
  def test_adds_room_to_livngSpace_list(self):
    initial_room_count = len(self.dojo.livingspace_list)
    red_livingspace = self.dojo.create_room("Red", "livingspace")
    self.assertTrue(red_livingspace)
    new_room_count = len(self.dojo.livingspace_list)
    self.assertEqual(new_room_count - initial_room_count, 1)

  def test_adds_Staff_successfully(self):
    self.dojo.create_room("Blue","Black","Brown", "office")
    Staff_Henry = self.dojo.add_person("Staff", "Henry")
    self.assertTrue(Staff_Henry)
    self.assertEqual(Staff_Henry.name, "Henry", msg='Name should be Henry')
    self.assertNotEqual(Staff_Henry.office, None, msg='No office allocated')

  def test_adds_Fellow_successfully(self):
    self.dojo.create_room("Blue","Black","Brown", "office")
    red_livingspace = self.dojo.create_room("Red", "Indigo", "livingspace")
    fellow_Albert = self.dojo.add_person("Fellow", "Albert", "Y")
    self.assertNotEqual(fellow_Albert.livingspace, None, msg='Name should be Albert')
    self.assertNotEqual(fellow_Albert.office, None, msg='Name should be Albert')
    
  def test_adds_Fellow_with_no_accomodation(self):
    offices = self.dojo.create_room("Blue")
    livingspaces = self.dojo.create_room("Harambe")
    fellow_Albert = self.dojo.add_person("Fellow", "Albert", "N")
    self.assertEqual(fellow_Albert.name, "Albert", msg='Name should be Henry')
    self.assertEqual(fellow_Albert.livingspace, None, msg='Name should be Albert')
    self.assertNotEqual(fellow_Albert.office, None, msg='Name should be Albert')
    
  def test_adds_Fellow_with_no_accomodation(self):
    office = self.dojo.create_room("Brown", "office")
    living_space = self.dojo.create_room("Brown", "livingspace")
    livingspaces = self.dojo.create_room("Harambe")
    fellow_Albert = self.dojo.add_person("Fellow", "Albert")
    self.assertEqual(fellow_Albert.name, "Albert", msg='Name should be Henry')
    self.assertEqual(fellow_Albert.livingspace, 'None', msg='Name should be Albert')
    self.assertNotEqual(fellow_Albert.office, None, msg='Name should be Albert')

  def test_gets_occupants(self):
    office = self.dojo.create_room("Black", "office")
    fellow1 = self.dojo.add_person("Staff", "Albert")
    self.assertEqual(self.dojo.get_occupants("Black"), ['Albert'], msg='Couldnot get occupants')
  """
  def test_reallocate_person(self):
    office = self.dojo.create_room("Black", "office")
    staff = self.dojo.add_person("Staff", "Albert")
    office = self.dojo.create_room("Orange", "office")
    self.dojo.reallocate_person("Albert", "Orange")
    self.assertEqual(staff.office, 'Orange', msg='Name should be Albert')"""

if __name__ == "__main__":
  unittest.main()