from coverage_code.funny_string import funnyString, random_string
import unittest
from unittest import mock

#Strub Testing
class RandomStringTest(unittest.TestCase):

    def test_random_should_length_0_10(self):
        result = random_string()

        self.assertIn(len(result), range(0, 11))


class IsFunnyStringTest(unittest.TestCase):
    
    @mock.patch("coverage_code.funny_string.random_string", return_value="acxz")
    def test_give_acxz_is_funny_string(self, random_string_mock):
        expected_output = "Funny"
        string = random_string_mock.return_value

        result = funnyString(string)

        self.assertEqual(result, expected_output, f"Should be {expected_output}")

    @mock.patch("coverage_code.funny_string.random_string", return_value="ksdpox")
    def test_give_ksdpox_is_not_funny_string(self, random_string_mock):
        expected_output = "Not Funny"
        string = random_string_mock.return_value

        result = funnyString(string)

        self.assertEqual(result, expected_output, f"Should be {expected_output}")

    @mock.patch("coverage_code.funny_string.random_string", return_value="")
    def test_give_empty_string_is_funny_string(self, random_string_mock):
        expected_output = "Funny"
        string = random_string_mock.return_value

        result = funnyString(string)

        self.assertEqual(result, expected_output, f"Should be {expected_output}")

    @mock.patch("coverage_code.funny_string.random_string", return_value="a")
    def test_give_a_string_is_funny_string(self, random_string_mock):
        expected_output = "Funny"
        string = random_string_mock.return_value

        result = funnyString(string)

        self.assertEqual(result, expected_output, f"Should be {expected_output}")

    @mock.patch("coverage_code.funny_string.random_string", return_value="aaaa")
    def test_give_aaaa_is_not_funny_string(self, random_string_mock):
        expected_output = "Funny"
        string = random_string_mock.return_value

        result = funnyString(string)

        self.assertEqual(result, expected_output, f"Should be {expected_output}")


class FunnyStringWithRandomString(unittest.TestCase):
    def test_random_should_return_funny_or_notfunny(self):
        expected_result = ["Funny", "Not Funny"]
        string = "Random Value"
        
        result = funnyString(string)

        self.assertIn(result, expected_result)
