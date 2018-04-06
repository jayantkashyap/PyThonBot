from VectorSpaceModel import *
import random
from corpus.pattern_C import *
from corpus.corpus_C import *
from preprocessing import *
from nltk.tokenize import RegexpTokenizer

"""
    querytype = 0 : Bot related
    querytype = 1 : Factoid wh-questions
    querytype = 2 : Factoid truth and ability
    querytype = 3 : Factoid definition
    querytype = 4 : Complex
"""


class QueryProcess:
    def __init__(self):
        self.query = ''
        self.query_tokens = []
        # self.verbs = []
        self.response = ''
        self.document_tokens = []
        self.tf = {}
        self.documents = []

    def queryprocess(self):
        preprocess = Preprocess()
        self.query = self.query.lower().strip()
        self.query = self.query.strip('@')
        self.query = self.query.strip('#')
        self.query = self.query.strip('$')
        self.query = self.query.strip('^')

        self.query = preprocess.preprocess(self.query)

        tokenizer = RegexpTokenizer(r"[\d-]+\w+|[A-Z][.A-Z]+\b\.*|[\w\-\']+|'.*'")
        self.query_tokens = tokenizer.tokenize(self.query)

        if self.query_tokens[0] in wh_qstn_words:
            self.query_type = 1
        elif self.query_tokens[0] in ab_qstn_words:
            self.query_type = 2
        elif self.query_tokens[0] in desc_qstn_words:
            self.query_type = 3
        else:
            self.query_type = 4

        pass

    def queryResponse(self):
        ###### BOT RELATED ######
        if self.query.lower().rstrip('?') in about[0]:
            self.response = random.choice(about[1])
            self.querytype = 0
        elif self.query.lower().rstrip('?') in who[0]:
            self.response = random.choice(who[1])
            self.querytype = 0
        elif self.query.lower().rstrip('?') in create[0]:
            self.response = random.choice(create[1])
            self.querytype = 0
        ##########################
        else:
            self.queryprocess()
            # default_tagger = data.load('taggers/maxent_treebank_pos_tagger/english.pickle')
            # custom_tagger = tag.UnigramTagger(model=models, backoff=default_tagger)
            # self.pos_tags = custom_tagger.tag(self.query_tokens)
            # print(self.pos_tags)

            if self.query_type == 1:
                self.response = self.responseProcess(1)
            elif self.query_type == 2:
                self.response = self.responseProcess(2)
            elif self.query_type == 3:
                self.response = self.responseProcess(3)
            elif self.query_type == 4:
                self.response = self.responseProcess(4)

    def responseProcess(self, qtype):
        response = None
        if qtype == 1:
            if self.query_tokens[0] == 'who':
                for p,v in person.items():
                    if self.query in p:
                        response = v
                        break
                if response is None:
                    response = random.choice(unknown)
            if self.query_tokens[0] == 'when':
                for p,v in date.items():
                    if self.query in p:
                        response = v
                        break
                if response is None:
                    response = random.choice(unknown)
            if self.query_tokens[0] == 'where':
                for p,v in location_reference.items():
                    if self.query in p:
                        response = v
                        break
                if response is None:
                    response = random.choice(unknown)
            if self.query_tokens[0] == 'how':
                if self.query_tokens[1] != 'many':
                    for p,v in methodology.items():
                        if self.query in p:
                            response = v
                            break
                    if response is None:
                        response = random.choice(unknown)
                else:
                    response = "So many"
                    if response is None:
                        response = random.choice(unknown)
            if self.query_tokens[0] == 'why':
                for p,v in reason.items():
                    if self.query in p:
                        response = v
                        break
                if response is None:
                    response = random.choice(unknown)
            if self.query_tokens[0] == 'whom':
                for p,v in location_reference.items():
                    if self.query in p:
                        response = v
                        break
                if response is None:
                    response = random.choice(unknown)
        elif qtype == 2:
            if self.query_tokens[0] in ab_qstn_words:
                for p,v in ability.items():
                    if self.query in p:
                        response = v
                        break
                if response is None:
                    response = random.choice(unknown)
        elif qtype == 3:
            if self.query_tokens[0] in desc_qstn_words:
                for p,v in definition.items():
                    if self.query in p:
                        response = v
                        break
                if response is None:
                    response = random.choice(unknown)
        elif qtype == 4:
            vsm = VectorSpaceModel(self.query_tokens, self.document_tokens)
            rank = vsm.vectorize()
            max_similarity = 0
            response = ''
            for k,v in rank.items():
                if v > max_similarity:
                    response = self.documents[k]
                    max_similarity = v
            if not response:
                response = random.choice(unknown)
        else:
            response = "Question type not defined! I can only answer factoid or complex questions."
        return response
