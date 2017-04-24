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


if __name__ == "__main__":
  unittest.main()