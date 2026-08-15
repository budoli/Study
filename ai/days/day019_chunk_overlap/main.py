"""Day 019 - Chunk overlap."""

from pathlib import Path


def main():
    file_path = Path("data/sample_docs/day019.txt")
    text = file_path.read_text(encoding="utf-8")

    chunk_size = 100
    overlap = 20

    chunks = []
    step = chunk_size - overlap

    print(f"chunk_size = {chunk_size}")
    print(f"overlap = {overlap}")

    for start in range(0, len(text), step):
        end = start + chunk_size
        chunk = text[start:end]

        if chunk :
            chunks.append((start, end, chunk))

    print(f"전체 Chunk 개수: {len(chunks)}")

    for index, (start, end, chunk) in enumerate(chunks, start=1):
        print(f"Chunk {index}")
        print(f"시작 위치: {start}")
        print(f"끝 위치: {end}")
        print(f"길이: {len(chunk)}")
        print("내용:")
        print(chunk)

if __name__ == "__main__":
    main()
