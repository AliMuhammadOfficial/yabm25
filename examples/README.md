# YaBM25 Examples

This directory contains examples demonstrating various use cases of YaBM25.

## Basic Usage

### Simple In-Memory BM25 (rank_bm25 style)
See [quickstart.py](quickstart.py) for rank_bm25 compatible usage:
```python
from yabm25 import BM25Indexer

corpus = [
    "Hello there good man!",
    "It is quite windy in London",
    "How is the weather today?"
]

tokenized_corpus = [doc.split(" ") for doc in corpus]
bm25 = BM25Indexer(tokenized_corpus)

# Get scores for query
query = "windy London"
doc_scores = bm25.get_scores(query.split(" "))
# array([0., 0.93729472, 0.])

# Get top documents
top_docs = bm25.get_top_n(query.split(" "), corpus, n=1)
# ['It is quite windy in London']
```

### Disk-Based Index
See [persistent_index.py](persistent_index.py) for large-scale usage:
```python
from yabm25 import BM25Indexer, BM25Config

config = BM25Config(
    index_dir="my_index",
    doc_chunk_size=500_000,
    compression="ZSTD"
)

indexer = BM25Indexer(config)
indexer.build_index(large_corpus)
results = indexer.query(["term1", "term2"])
```

## Advanced Examples

- [preprocessing.py](preprocessing.py): Text preprocessing and tokenization
- [variants.py](variants.py): BM25L and BM25Adpt usage
- [index_management.py](index_management.py): Index backup and optimization
- [parallel_processing.py](parallel_processing.py): Multi-threaded indexing
