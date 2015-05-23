import unittest
import notebook
from notebook import Notebook

class TestNotebook(unittest.TestCase):
    def test_greettings(self):
        notebook = Notebook()
        self.assertEqual(notebook.greeting(), 'Hi there! How have you been?')

if __name__ == '__main__':
    unittest.main()
