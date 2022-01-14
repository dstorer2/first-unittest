import unittest
from vehicle import Vehicle

class TestVehicle(unittest.TestCase):

    def test_email(self):
        car_1 = Vehicle("red", "beep", 4, "sedan", 15)
        car_2 = Vehicle("purple", "boop", 2, "hot wheels", 600)

        self.assertEqual(car_1.email, "red.beep@email.com")
        self.assertEqual(car_2.email, "purple.boop@email.com")

        car_1.color = "green"
        car_2.color = "orange"

        self.assertEqual(car_1.email, "green.beep@email.com")
        self.assertEqual(car_2.email, "orange.boop@email.com")

    def test_full_deets(self):
        car_1 = Vehicle("red", "beep", 4, "sedan", 15)
        car_2 = Vehicle("purple", "boop", 2, "hot wheels", 600)

        self.assertEqual(car_1.full_deets, "red 4-door sedan")
        self.assertEqual(car_2.full_deets, "purple 2-door hot wheels")

        car_1.color = "green"
        car_2.color = "orange"

        self.assertEqual(car_1.full_deets, "green 4-door sedan")
        self.assertEqual(car_2.full_deets, "orange 2-door hot wheels")
    
    def test_give_tune_up(self):
        car_1 = Vehicle("red", "beep", 4, "sedan", 15)
        car_2 = Vehicle("purple", "boop", 2, "hot wheels", 600)

        car_1.give_tune_up()
        car_2.give_tune_up()

        self.assertEqual(car_1.topSpeed, 30)
        self.assertEqual(car_2.topSpeed, 615)

if __name__ == '__main__':
    unittest.main()
