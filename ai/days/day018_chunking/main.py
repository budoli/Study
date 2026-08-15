"""Day 018 - Document chunking."""
from pathlib import Path

def main():

    file_path = Path("data/sample_docs/day018.txt")
    text = file_path.read_text(encoding="utf-8")

    chunk_size = 100

    chunks = []

    for i in range(0, len(text), 100) :
        end = i + chunk_size
        chunk = text[i:end]
        chunks.append(chunk)

    print(f"전체 chunk 개수: {len(chunks)}")
    print()
    for index, text in enumerate(chunks, start=1) :
        print(f"Chunk {index}")
        print(f"길이: {len(text)}")
        print("내용:")
        print(text)

if __name__ == "__main__":
    main()
