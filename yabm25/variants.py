import numpy as np
from .core import BM25Indexer


class BM25L(BM25Indexer):
    def __init__(self, delta: float = 0.5, **kwargs):
        super().__init__(**kwargs)
        self.delta = delta

    def _process_term(self, term: str, idf: float):
        doc_ids, tfs = super()._process_term(term, idf)
        adjusted_tfs = tfs + self.delta
        # BM25L specific scoring
        return doc_ids, adjusted_tfs * idf


class BM25Adpt(BM25Indexer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._adapt_parameters()

    def _adapt_parameters(self):
        """Automatically adjust k1 and b based on corpus stats"""
        doc_length_std = np.std(self.doc_lengths)
        self.config.k1 = 1.2 + (0.3 * (self.avgdl - 100) / 100)
        self.config.b = 0.75 + (0.15 * (doc_length_std / self.avgdl))
