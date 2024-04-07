from coverage_code.grid_challenge import gridChallenge
import unittest

class GridChallengeTest(unittest.TestCase):
    def test_give_aaaa_aaaa_aaaa_aaaa_aaaa(self):
        grid = ['aaaa', 'aaaa', 'aaaa', 'aaaa', 'aaaa']
        expected_output = "YES"
        
        result = gridChallenge(grid)
        
        self.assertEqual(result,expected_output, f'Should be {expected_output}')
    
    def test_give_abc_lmp_qrt(self):
        grid = ['hba', 'trk', 'yxz']
        expected_output = "YES"
        
        result = gridChallenge(grid)
        
        self.assertEqual(result,expected_output, f'Should be {expected_output}')

    def test_give_abc_hjk_mpq_rtv(self):
        grid = ['ivbn', 'yadq', 'xcss','asdq']
        expected_output = "NO"
        
        result = gridChallenge(grid)
        
        self.assertEqual(result,expected_output, f'Should be {expected_output}')

    def test_give_mpxz_abcd_wlmf(self):
        grid = ['mpxz', 'abcd', 'wlmf']
        expected_output = "NO"
        
        result = gridChallenge(grid)
        
        self.assertEqual(result,expected_output, f'Should be {expected_output}')

    def test_give_abc_def_ghi(self):
        grid = ['abc', 'def', 'ghi']
        expected_output = "YES"
        
        result = gridChallenge(grid)
        
        self.assertEqual(result, expected_output, f'Should be {expected_output}')

