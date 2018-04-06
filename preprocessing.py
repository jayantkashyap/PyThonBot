import re, random
from corpus.pattern_C import *

class Preprocess:
    def __init__(self):
        self.sentence = ''
        self.replacer = RegexReplacer()

    def remove_extra_end_spaces(self):
        self.sentence = self.sentence.lstrip()
        self.sentence = self.sentence.rstrip('?')
        self.sentence = re.sub(' +', ' ', self.sentence)

    def preprocess(self, sentence):
        self.sentence = sentence
        if self.sentence.isspace():
            return None
        self.sentence = self.replacer.replace(self.sentence)
        self.remove_extra_end_spaces()
        return self.sentence

    def remove_stop_words(self):
        pass

class RegexReplacer:
    def __init__(self, patterns=replacement_patterns):
        self.patterns = [(re.compile(regex), repl) for (regex, repl) in patterns]

    def replace(self, text):
        s = text
        for (pattern, repl) in self.patterns:
            s = re.sub(pattern, repl, s)

        return s
