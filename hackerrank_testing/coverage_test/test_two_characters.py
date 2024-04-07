from coverage_code.two_characters import alternate
import unittest


class TwoCharactersTest(unittest.TestCase):
    def test_give_asdcbsdcagfsdbgdfanfghbsfdab_should_be_8(self):
        char = "asdcbsdcagfsdbgdfanfghbsfdab"
        expected_output = 8

        result = alternate(char)

        self.assertEqual(result, expected_output, f"Should be {expected_output}")

    def test_give_asvkugfiugsalddlasguifgukvsa_should_be_0(self):
        char = "asvkugfiugsalddlasguifgukvsa"
        expected_output = 0

        result = alternate(char)

        self.assertEqual(result, expected_output, f"Should be {expected_output}")

    def test_give_beabeefeab_should_be_5(self):
        char = "beabeefeab"
        expected_output = 5

        result = alternate(char)

        self.assertEqual(result, expected_output, f"Should be {expected_output}")

    def test_give_empty_string_should_be_0(self):
        char = ""
        expected_output = 0

        result = alternate(char)

        self.assertEqual(result, expected_output, f"Should be {expected_output}")

    def test_give_abababababab_should_be_10(self):
        char = "abababababab"
        expected_output = 12

        result = alternate(char)

        self.assertEqual(result, expected_output, f"Should be {expected_output}")
