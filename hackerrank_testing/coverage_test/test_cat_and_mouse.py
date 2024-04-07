from coverage_code.cat_and_mouse import catAndMouse, randomMouseDistance
import unittest
from unittest import mock


#Strub Testing
class RandomMouseDistanceTest(unittest.TestCase):
    def test_random_should_0_10(self):
        result = randomMouseDistance()

        self.assertIn(result, range(0, 10))


class CatMouseTest(unittest.TestCase):
    @mock.patch("coverage_code.cat_and_mouse.randomMouseDistance", return_value=3)
    def test_catA_1_catB_2_mouse_3(self, random_integer_mock):
        expected_output = "Cat B"
        cat_A = 1
        cat_B = 2
        mouse = random_integer_mock.return_value
        
        who_closet = catAndMouse(cat_A, cat_B, mouse)

        self.assertEqual(who_closet, expected_output, f"Should be {expected_output}")

    @mock.patch("coverage_code.cat_and_mouse.randomMouseDistance", return_value=2)
    def test_catA_1_catB_3_mouse_2(self, random_integer_mock):
        expected_output = "Mouse C"
        cat_A = 1
        cat_B = 3
        mouse = random_integer_mock.return_value

        who_closet = catAndMouse(cat_A, cat_B, mouse)

        self.assertEqual(who_closet, expected_output, f"Should be {expected_output}")

    @mock.patch("coverage_code.cat_and_mouse.randomMouseDistance", return_value=2)
    def test_catA_1_catB_4_mouse_2(self, random_integer_mock):
        expected_output = "Cat A"
        cat_A = 1
        cat_B = 4
        mouse = random_integer_mock.return_value

        who_closet = catAndMouse(cat_A, cat_B, mouse)

        self.assertEqual(who_closet, expected_output, f"Should be {expected_output}")

    @mock.patch("coverage_code.cat_and_mouse.randomMouseDistance", return_value=1)
    def test_catA_3_catB_2_mouse_1(self, random_integer_mock):
        expected_output = "Cat B"
        cat_A = 3
        cat_B = 2
        mouse = random_integer_mock.return_value

        who_closet = catAndMouse(cat_A, cat_B, mouse)

        self.assertEqual(who_closet, expected_output, f"Should be {expected_output}")

    @mock.patch("coverage_code.cat_and_mouse.randomMouseDistance", return_value=5)
    def test_catA_5_catB_5_mouse_5(self, random_integer_mock):
        expected_output = "Mouse C"
        cat_A = 5
        cat_B = 5
        mouse = random_integer_mock.return_value

        who_closet = catAndMouse(cat_A, cat_B, mouse)

        self.assertEqual(who_closet, expected_output, f"Should be {expected_output}")


class CatMouseTestWithRandomMouseDistance(unittest.TestCase):
    def test_random_should_return_catA_or_catB_or_mouseC(self):
        expected_result = ["Cat A", "Cat B", "Mouse C"]
        cat_A = 3
        cat_B = 7
        mouse = "Random Value"

        result = catAndMouse(cat_A, cat_B, mouse)

        self.assertIn(result, expected_result)
