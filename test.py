import unittest
from Tkinter import *
from matrix_symbol import *

class TestMS(unittest.TestCase):
    def test_ms(self):
        application = program()
        self.assertEqual(application.run(), 'test')
        
if __name__ == '__main__':
    unittest.main()