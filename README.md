# YaBM25

Yet Another BM25 Implementation - A fast, scalable BM25 search engine with both in-memory and disk-based indexing.

## Features
- 🚀 Compatible with rank_bm25 API
- 📦 Optional disk-based indexing for large datasets
- 🔧 Multiple BM25 variants (BM25L, BM25Adpt)
- 🛠 Production-ready with proper resource management

## Installation
```bash
pip install yabm25
```

## Quick Start

### Simple In-Memory Usage
```python
from yabm25 import BM25Indexer

# Initialize with corpus
corpus = [
    "Hello there good man!",
    "It is quite windy in London",
    "How is the weather today?"
]
tokenized_corpus = [doc.split(" ") for doc in corpus]
bm25 = BM25Indexer(tokenized_corpus)

# Search
query = "windy London"
doc_scores = bm25.get_scores(query.split(" "))
print(doc_scores)  # array([0., 0.93729472, 0.])

# Get top document
top_docs = bm25.get_top_n(query.split(" "), corpus, n=1)
print(top_docs)  # ['It is quite windy in London']
```

### Large-Scale Usage
```python
from yabm25 import BM25Indexer, BM25Config

# Configure disk-based index
config = BM25Config(
    index_dir="my_index",
    doc_chunk_size=500_000,
    compression="ZSTD"
)

# Build index
indexer = BM25Indexer(config)
indexer.build_index(large_corpus)

# Search
results = indexer.query(["term1", "term2"])
```

## Documentation
- [Examples](examples/README.md)
- [API Reference](docs/api.md)
- [Performance Guide](docs/performance.md)

## Contributing
Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License
MIT License. See [LICENSE](LICENSE) for details.