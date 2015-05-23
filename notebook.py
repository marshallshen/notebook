import acts
import nltk as robot
from acts.directive import Directive

class Notebook(object):
    def __init__(self):
        self.empathy = {}

    def greeting(self):
        return 'Hi there! How have you been?'

    def listen(self, text):
        tokenized_text = robot.word_tokenize(text)
        tagged_text = robot.pos_tag(tokenized_text)
        print tagged_text

        return Directive().react()

