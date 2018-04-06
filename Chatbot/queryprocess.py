import re
import random
from corpus.pattern import *
from corpus.corpus import *
from preprocessing import Preprocess
from nltk import data, tag
from nltk.tokenize import RegexpTokenizer
from corpus.documents.synonyms import *
import random

"""
    querytype = 0 : Bot related
    querytype = 1 : Factoid wh-questions
    querytype = 2 : Factoid truth and ability
    querytype = 3 : Factoid definition
    querytype = 4 : Complex
"""

verb_tags = ['VB','VBG','VBN','VBZ','VBD']
subject_tags = ['JJ','NN','NNS','method','person','location']

class QueryProcess:
    def __init__(self):
        self.query = ''
        self.response = ''
        self.query_type = -1
        self.query_tokens = []
        self.pos_tags = None
        self.subjects = []
        self.verbs = []
        self.domain = None

    def queryResponse(self):
        ###### BOT RELATED ######
        if self.query.lower().rstrip('?') in about[0]:
            self.response = random.choice(about[1])
            querytype = 0
        elif self.query.lower().rstrip('?') in who[0]:
            self.response = random.choice(who[1])
            querytype = 0
        elif self.query.lower().rstrip('?') in create[0]:
            self.response = random.choice(create[1])
            querytype = 0
        ##########################
        else:
            self.queryProcess()
            default_tagger = data.load('taggers/maxent_treebank_pos_tagger/english.pickle')
            custom_tagger = tag.UnigramTagger(model=models, backoff=default_tagger)
            self.pos_tags = custom_tagger.tag(self.query_tokens)
            print(self.pos_tags)

            if self.query_type == 1:
                self.response = self.responseProcess(1)
                self.subjects = []
                self.verbs = []
            elif self.query_type == 2:
                self.response = self.responseProcess(2)
            elif self.query_type == 3:
                self.response = self.responseProcess(3)
            elif self.query_type == 4:
                self.response = self.responseProcess(4)

            # self.response = "I am being trained. My knowledge base is so small"
        return self.response

    def queryProcess(self):
        preprocess = Preprocess()
        self.query = self.query.lower()
        self.query = preprocess.preprocess(self.query)

        tokenizer = RegexpTokenizer(r"[\d-]+\w+|[A-Z][.A-Z]+\b\.*|[\w-]+|'.*'")
        self.query_tokens = tokenizer.tokenize(self.query)

        if self.query_tokens[0] in wh_qstn_words:
            self.query_type = 1
        elif self.query_tokens[0] in ab_qstn_words:
            self.query_type = 2
        elif self.query_tokens[0] in desc_qstn_words:
            self.query_type = 3
        else:
            self.query_type = 4

    def responseProcess(self, qtype):
        response = ""
        if qtype == 1:
            # print(self.query_tokens[0])
            if self.query_tokens[0] == 'who':
                self.domain = person
                self.getSubjects()
                self.getVerbs()
                response = self.getAnswer(self.subjects,self.verbs)
                self.domain = None
                self.subjects = []
                self.verbs = []
        elif qtype == 3:
            if self.query_tokens[0] in desc_qstn_words:
                self.domain = definition
                self.getSubjects()
                response = self.getAnswer(self.subjects)
                self.domain = None
                self.subjects = []
        return response

    def getSubjects(self):
        for p in self.pos_tags:
            if (p[1] in subject_tags) and (p[0] not in stop_words):
                self.subjects.append(p)

    def getVerbs(self):
        for p in self.pos_tags:
            if p[1] in verb_tags and (p[0] in action_verbs):
                self.verbs.append(p)

    def getAnswer(self, subjects, verbs=None):
        response = ''
        res_subjects = []
        res_verbs = []
        for subject in subjects:
            s = self.getSynonyms(subject, stype='subject')
            if s:
                res_subjects.append(s)

        if verbs is None:
            if len(res_subjects) > 0:
                response = self.domain[res_subjects[0]]
            else:
                response = random.choice(unknown)
        else:
            for verb in verbs:
                v = self.getSynonyms(verb)
                if v:
                    res_verbs.append(v)

            for verb in res_verbs:
                for d, r in self.domain.items():
                    if verb == d:
                        if len(res_subjects) > 0:
                            response = r[res_subjects[0]]
                        else:
                            response = random.choice(unknown)
        return response

    def getSynonyms(self,word, stype='verb'):
        if stype == 'subject':
            for key, value in subject_synonyms.items():
                if word[0] in key:
                    return value
        for key, value in verb_synonyms.items():
            if word[0] in key:
                return value
        return None
