"""Day 012 - Simple keyword search."""

from pathlib import Path


def normalized(text):
    return (
        text.lower().replace(",", "").replace(".", "").replace("!", "").replace("?", "")
    )


def main():

    doc_path = [
        "data/sample_docs/day012_doc1.txt",
        "data/sample_docs/day012_doc2.txt",
        "data/sample_docs/day012_doc3.txt",
    ]

    documents = [Path(path).read_text(encoding="utf-8") for path in doc_path]

    query = "search"
    normalized_query = normalized(query)

    result = []

    for index, document in enumerate(documents, start=1):
        normalized_document = normalized(document)
        words = normalized_document.split()
        score = words.count(normalized_query)

        if score > 0:
            result.append((index, score, document))

    result = sorted(result, key=lambda x: x[1], reverse=True)

    print(f"검색어: {query}")
    print()

    print("검색결과:")
    for index, score, document in result:

        print(f"문서 {index} | 점수: {score}")
        print(document)


if __name__ == "__main__":
    main()
