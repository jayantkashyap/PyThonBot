from collections import Counter
from math import log

class TfIdf:

    def __init__(self, documents=None):
        self.documents = documents

    def _term_frequency(self, term, tokenized_document):
        _term_count = tokenized_document.count(term)
        return _term_count/len(tokenized_document)

    def _augmented_term_frequency(self, term, tokenized_document):
        term_counts = Counter(tokenized_document)
        _mc_term, _mc_count = term_counts.most_common(1)[0]
        _term_count = term_counts.get(term)
        # return 0.5 + (0.5*_term_count/_mc_count)
        return _term_count/_mc_count


    def _inverse_document_frequency(self, documents):
        idf_values = {}
        l = len(documents)
        all_words = set([word for document in documents for word in document])
        for word in all_words:
            contains_word = map(lambda doc: word in doc, documents)
            idf_values[word] = log(l/sum(contains_word))
        return idf_values

    def tfidf(self, documents):
        idf = self._inverse_document_frequency(documents)
        tfidf_documents = []
        for document in documents:
            tfidf_document = {}
            for word in document:
                tfidf_document[word] = self._augmented_term_frequency(word, document) * idf[word]
            tfidf_documents.append(tfidf_document)
        return tfidf_documents

