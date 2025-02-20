from setuptools import setup, find_packages
import os
import re

def get_version():
    init_path = os.path.join("yabm25", "version.py")
    with open(init_path, "r", encoding="utf-8") as f:
        version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", f.read(), re.M)
        if version_match:
            return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

if __name__ == "__main__":
    setup(
        name="yabm25",
        version=get_version(),
        description="Fast BM25 search engine for Python with RAG support",
        long_description=open("README.md", encoding="utf-8").read(),
        long_description_content_type="text/markdown",
        url="https://github.com/alimuhammadofficial/yabm25",
        author="Ali Muhammad",
        author_email="ali@quantlix.com",
        license="MIT",
        classifiers=[
            "Development Status :: 4 - Beta",
            "Intended Audience :: Developers",
            "Intended Audience :: Science/Research",
            "Intended Audience :: Information Technology",
            "Topic :: Scientific/Engineering :: Artificial Intelligence",
            "Topic :: Text Processing :: Indexing",
            "Topic :: Information Retrieval",
            "Topic :: Software Development :: Libraries :: Python Modules",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
            "Programming Language :: Python :: 3.12",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        keywords="bm25 search-engine ranking information-retrieval rag llm vector-search elastic-search ranking-algorithm nltk transformers huggingface langchain llamaindex",
        packages=find_packages(),
        project_urls={
            "Documentation": "https://yabm25.quantlix.com/",
            "Source": "https://github.com/alimuhammadofficial/yabm25",
            "Issues": "https://github.com/alimuhammadofficial/yabm25/issues",
        },
        python_requires=">=3.8",
    )
