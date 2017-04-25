"""
  name : room management system.
  authr : benjamin wacha
  email: bmwachajr@gmail,com
  descrption: a system to randomly allocate rooms to andela staff and fellows.

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

  def test_create_room_name_not_given(self):
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
      
  def test_adds_Staff_successfully(self):
    staff = Staff()
    Staff_Henry = staff.add_person("staff", "Henry")
    self.assertTrue(Staff_Henry)
    self.assertEqual(Staff_Henry.person_name, "Henry", msg='Name should be Henry')
    self.assertEqual(Staff_Henry.office_space, "", msg='Name should be Henry')

  def test_adds_Fellow_successfully(self):
    fellow = Fellow()
    fellow_Albert = fellow.add_person("Fellow", "Albert", "Y")
    self.assertEqual(fellow_Albert.person_name, "Albert", msg='Name should be Henry')
    self.assertEqual(fellow_Albert.wants_accomodation, "Y", msg='Name should be Albert')
    
if __name__ == "__main__":
  unittest.main()