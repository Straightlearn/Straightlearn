import unittest

class Testing(unittest.TestCase):
    def test_lower(self):
        self.assertEqual('FOO'.lower(), 'foo')

if __name__ == '__main__':
    unittest.main()
