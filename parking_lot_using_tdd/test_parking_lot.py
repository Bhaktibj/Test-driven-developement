import unittest
from ParkingLot import ParkingLot

parking_lot = ParkingLot()

class TestParkingLot(unittest.TestCase):

    def test_create_parking_lot_valid(self):
        result = parking_lot.create_parking_lot(4)
        self.assertEqual(4,result)

    def test_create_parking_lot_invalid(self):
        result = parking_lot.create_parking_lot(4)
        self.assertNotEqual(5, result)

    def test_park(self):
        result = parking_lot.create_parking_lot(7)
        result = parking_lot.park("KA-01-HH-111", "White")
        result = parking_lot.park("KA-01-HH-112", "Black")
        self.assertNotEqual(-1, result)

    def test_leave_slot(self):
        result = parking_lot.create_parking_lot(6)
        result = parking_lot.park("KA-01-HH-1001", "White")
        result = parking_lot.park("KA-01-HH-1002", "Black")
        result = parking_lot.leave_slot(1)
        self.assertEqual(True, result)

    def test_get_regno_from_color(self):
        result = parking_lot.create_parking_lot(8)
        result = parking_lot.park("KA-01-HH-123", "White")
        result = parking_lot.park("KA-01-HH-999", "White")
        regnos = parking_lot.get_regno_from_color("White")
        self.assertIn("KA-01-HH-123", regnos)
        self.assertIn("KA-01-HH-999", regnos)
        self.assertNotIn("MH-0-AB-123", regnos)

    def test_get_slotno_from_regno(self):
        res = parking_lot.create_parking_lot(6)
        res = parking_lot.park("KA-01-HH-3001", "White")
        res = parking_lot.park("KA-01-HH-9999", "White")
        slotno = parking_lot.get_slotno_from_regno("KA-01-HH-9999")
        self.assertEqual(2, slotno)

    def test_get_slotno_from_color(self):
        parking = ParkingLot()
        result = parking.create_parking_lot(8)
        result = parking.park("KA-01-HH-2001", "Black")
        result = parking.park("KA-01-HH-2002", "White")
        result = parking.park("MH-01-HH-2004", "Blue")
        result = parking.park("KA-01-HH-2005", "Black")
        slotnos = parking.get_slotno_from_color("Black")
        self.assertIn("1", slotnos)
        self.assertNotIn("2", slotnos)
        self.assertNotIn("3", slotnos)

if __name__ == '__main__':
    unittest.main()


