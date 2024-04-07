from coverage_code.caesar_cipher import caesarCipher
import unittest

class Caesar_Cipher(unittest.TestCase):
    def test_give_middle_Outz_with_2_shift(self):
        string = "abcdefg"
        k = 1
        expected_output = "bcdefgh"
        
        result = caesarCipher(string, k)
        
        self.assertEqual(result, expected_output, f'Should be {expected_output}')
        
    def test_give_PacharaponKetkaew_with_26_shift(self):
        string = "PacharaponKetkaew"
        k = 26
        expected_output = "PacharaponKetkaew"
        
        result = caesarCipher(string, k)
        
        self.assertEqual(result, expected_output, f'Should be {expected_output}') 
    
    def test_give_testingisnotthathard_with_0_shift(self):
        result = "testingisnotthathard"
        k = 0
        expected_output = "testingisnotthathard"
        
        result = caesarCipher(result, k)
        
        self.assertEqual(result, expected_output, f'Should be {expected_output}')

    def test_give_123_with_3_shift(self):
        result = "123"
        k = 3
        expected_output = "123"
        
        result = caesarCipher(result, k)
        
        self.assertEqual(result, expected_output, f'Should be {expected_output}')

    def test_empty_string_with_5_shift(self):
        string = ""
        k = 5
        expected_output = ""
        
        result = caesarCipher(string, k)
        
        self.assertEqual(result, expected_output, f'Should be {expected_output}')