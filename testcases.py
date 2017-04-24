 """
  name : room management system.
  authr : benjamin wacha
  email: bmwachajr@gmail,com
  descrption: a system to randomly allocate rooms to andela staff and fellows.

"""
import unittest
from unittest import TestCase
from RoomMgt import Dojo

class TestCreateRoom(unittest.TestCase):
  def test_create_room_successfully(self):
    self.Dojo = Dojo()
    initial_room_count = len(Dojo.all_rooms)
    blue_office = Dojo.create_room("Blue", "office")
    self.assertTrue(blue_office)
    new_room_count = len(Dojo.all_rooms)
    self.assertEqual(new_room_count - initial_room_count, 1)

  def test_create_room_name_not_given(self):
    with self.assertRaises(RuntimeError) as context:
      empty_office = Dojo.create_room("","")
      self.assertEqual(
          'Couldnt create Room.',
          context.exception.message,
          'Both Room Name and Room Type must be given'
      )
      
    def test_create_room_type_not_given(self):
    with self.assertRaises(RuntimeError) as context:
      no_type_office = Dojo.create_room("no_type", "")
      self.assertEqual(
          'Couldnt create Room.',
          context.exception.message,
          'Both Room Name and Room Type must be given'
        )
if __name__ == "__main__":
  unittest.main()