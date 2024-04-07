from coverage_code.alternating_characters import alternatingCharacters, random_string
import unittest
from unittest import mock


#Strub Testing
class RandomStringTest(unittest.TestCase):

    def test_random_should_length_0_20(self):
        result = random_string()

        self.assertIn(len(result), range(0, 21))

class AlternatingCharactersTest(unittest.TestCase):

    @mock.patch("coverage_code.alternating_characters.random_string", return_value="ABABABABAB")
    def test_give_ABABABABAB_should_be_0(self, random_string_mock):
        expected_output = 0
        string = random_string_mock.return_value

        result = alternatingCharacters(string)

        self.assertEqual(result,expected_output,f'Should be {expected_output}')

    @mock.patch("coverage_code.alternating_characters.random_string", return_value="ABBABBAA")
    def test_give_ABBABBAA_should_be_3(self, random_string_mock):
        expected_output = 3
        string = random_string_mock.return_value

        result = alternatingCharacters(string)

        self.assertEqual(result,expected_output,f'Should be {expected_output}')

    @mock.patch("coverage_code.alternating_characters.random_string", return_value="")
    def test_give_empty_string_should_be_0(self, random_string_mock):
        expected_output = 0
        string = random_string_mock.return_value

        result = alternatingCharacters(string)

        self.assertEqual(result, expected_output, f'Should be {expected_output}')   

    @mock.patch("coverage_code.alternating_characters.random_string", return_value="ABCD" * 1000)
    def test_give_long_ABCD_should_be_0(self, random_string_mock):
        expected_output = 0
        string = random_string_mock.return_value

        result = alternatingCharacters(string)

        self.assertEqual(result, expected_output, f'Should be {expected_output}')

    @mock.patch("coverage_code.alternating_characters.random_string", return_value="CCCCC")
    def test_give_CCCCC_should_be_4(self, random_string_mock):
        expected_output = 4
        string = random_string_mock.return_value

        result = alternatingCharacters(string)

        self.assertEqual(result, expected_output, f'Should be {expected_output}')

class AlternatingCharactersWithRandomString(unittest.TestCase):
    def test_random_should_return_funny_or_notfunny(self):
        expected_result = range(0,21)
        string = "Random Value"
        
        result = alternatingCharacters(string)

        self.assertIn(result, expected_result)
