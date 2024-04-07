from coe_number.number_utils import is_prime_list
import unittest



class PrimeListTest(unittest.TestCase):
    def test_give_1_2_3_is_prime(self):
        prime_list = [1, 2, 3]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)

    def test_give_1_2_4_6_is_not_prime(self):
        number_list = [1, 2, 4, 6]
        is_prime = is_prime_list(number_list)
        self.assertFalse(is_prime)
    
    def test_give_71_73_79_83_89_is_prime(self):
        prime_list = [71, 73, 79, 83, 89]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)

    def test_give_29_31_37_is_prime(self):
        prime_list = [29, 31, 37]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)

    def test_give_53_59_61_is_prime(self):
        prime_list = [53, 59, 61]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)
    
    def test_give_7_11_13_is_prime(self):
        prime_list = [7, 11, 13]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)