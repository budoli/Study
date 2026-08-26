"""Day 020 - Metadata and sources."""

from pathlib import Path


def main():

    source = Path(doc_files).read_text(encoding="utf-8")

    doc_files = ["data/sample_docs/day020_doc1.txt", "data/sample_docs/day020_doc2.txt"]
    chunk_size = 80
    overlap = 20

    chunks = []


    print(f"전체 chunk 개수: {1}")


if __name__ == "__main__":
    main()
