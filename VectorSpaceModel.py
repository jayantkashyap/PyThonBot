from TfIdf import TfIdf
import numpy as np


class VectorSpaceModel:
    def __init__(self, query, documents):
        self.query = query
        self.documents = documents
        ti = TfIdf()
        self.tfidf = ti.tfidf(self.documents)
        pass

    def cosine_similarity(self, query, document):
        _dot = np.dot(query,document)
        _qnorm = np.linalg.norm(query)
        _dnorm = np.linalg.norm(document)
        _magnitude = _qnorm*_dnorm
        if not _magnitude:
            return 0
        return _dot/_magnitude

    def vectorize(self):
        ranks = {}
        doc_idx = 0
        for doc in self.tfidf:
            q_vector = []
            d_vector = list(doc.values())
            for word in self.query:
                q_vector.append(doc.get(word, 0))
            ln = abs(len(d_vector)-len(q_vector))
            z = np.zeros(ln)
            if len(d_vector) > len(q_vector):
                q_vector = np.concatenate((q_vector, z))
            else:
                d_vector = np.concatenate((d_vector, z))
            # print(q_vector)
            # print(doc.keys())
            ranks[doc_idx-1] = self.cosine_similarity(query=np.array(q_vector),document=np.array(d_vector))
            doc_idx += 1

        return ranks


if __name__ == '__main__':
    pass
