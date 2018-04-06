from __future__ import print_function

from nltk.tokenize import RegexpTokenizer

from corpus.pattern_C import *
from queryProcecess import QueryProcess
from corpus.corpus_C import *
from TfIdf import TfIdf
from preprocessing import *


class Chat:
    def __init__(self):
        self.question = ''
        self.response = ''
        self.sentence = ''
        self.question_type = ''

        self.query_process = QueryProcess()

        with open("Design-History.txt", 'r') as d:
            document = d.readlines()

        repalcer = RegexReplacer()

        document = repalcer.replace("".join(document))
        documents = document.split('@')
        self.documents = [d.strip('\n').lower() for d in documents]

        tokenizer = RegexpTokenizer(r"[\d-]+\w+|[A-Z][.A-Z]+\b\.*|[\w\-\']+|'.*'")

        self.documents_tokens = [tokenizer.tokenize(d) for d in self.documents]

        tf = TfIdf()
        self.tfidf = tf.tfidf(self.documents_tokens)

    def _greet_ques(self):
        for greeting in greetings[0]:
            if self.question == greeting:
                return random.choice(greetings[1])
        return None

    def reply(self):
        self.response = self._greet_ques()
        if not self.response:
            self.query_process.documents = self.documents
            self.query_process.document_tokens = self.documents_tokens
            self.query_process.tf = self.tfidf
            self.query_process.query = self.question
            self.query_process.queryResponse()
            self.response = self.query_process.response
        return self.response


def chatbot():
    chat = Chat()

    while True:
        chat.question = input("Q: ")

        if chat.question == "bye" or chat.question == "Bye":
            print("A: See ya!")
            break

        if not chat.question:
            print("A: There!There! Harry.")
        else:
            print("A:", chat.reply())
        print()


if __name__ == '__main__':
    chatbot()
