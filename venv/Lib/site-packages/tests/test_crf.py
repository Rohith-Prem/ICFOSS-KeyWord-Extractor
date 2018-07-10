import unittest

from sys import path
path.append('crf')


class TestCRF(unittest.TestCase):

    def test_baseline_1(self):
        self.assertEqual(
                1,
                1
                )



if __name__ == '__main__':
    unittest.main()
