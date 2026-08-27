"""Day 020 - Metadata and sources."""

from pathlib import Path


def main():
    doc_files = ["data/sample_docs/day020_doc1.txt", "data/sample_docs/day020_doc2.txt"]

    chunk_size = 80
    overlap = 20
    chunks = []

    step = chunk_size - overlap

    for path in doc_files:
        text = Path(path).read_text(encoding="utf-8")

        for chunk_id, start in enumerate(range(0, len(text), step), start=1):
            end = start + chunk_size

            chunk_text = text[start:end]

            if chunk_text:
                chunks.append(
                    {
                        "source": path,
                        "chunk_id": chunk_id,
                        "start": start,
                        "end": end,
                        "text": chunk_text,
                    }
                )

    print(f"전체 chunk 개수: {len(chunks)}")
    for chunk in chunks:
        print(f"Source: {chunk['source']}")
        print(f"Chunk ID: {chunk['chunk_id']}")
        print(f"Start: {chunk['start']}")
        print(f"End: {chunk['end']}")
        print(f"Text:")
        print(chunk["text"])
        print()


if __name__ == "__main__":
    main()
