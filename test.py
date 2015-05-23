import unittest
import notebook
from notebook import Notebook

class TestNotebook(unittest.TestCase):
    def test_greetings(self):
        notebook = Notebook()
        self.assertEqual(notebook.greeting(), 'Hi there! How have you been?')

    def test_negative_directive(self):
        notebook = Notebook()
        reaction = notebook.listen("I did not feel so happy today.")
        self.assertEqual(reaction, 'Why is that?')

    def test_positive_directive(self):
        notebook = Notebook()
        reaction = notebook.listen("I am happy.")
        self.assertEqual(reaction, 'Yeah! Tell me more?!')

if __name__ == '__main__':
    unittest.main()
