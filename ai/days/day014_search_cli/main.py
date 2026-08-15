"""Day 014 - Document search CLI."""

from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def main():
    doc_path = ["data/sample_docs/day014_doc1.txt", "data/sample_docs/day014_doc2.txt", "data/sample_docs/day014_doc3.txt"]

    documents = [Path(path).read_text(encoding="utf-8") for path in doc_path]

    query = input("검색어를 입력하세요: ").strip()

    if not query:
        print("검색어를 입력하세요.")
        raise SystemExit

    vectorizer = TfidfVectorizer()
    text_vector = vectorizer.fit_transform(documents)
    query_vector = vectorizer.transform([query])

    similarity = cosine_similarity(text_vector, query_vector)
    best_index = similarity.argmax()

    print("문서별 유사도:")

    for index, similar in enumerate(similarity, start=1):
        print(f"문서 {index}: {similar[0]:.4f}")
    print()
    print("가장 유사한 문서:")
    print(f"문서 번호: {best_index+1}")
    print(f"유사도: {similarity.max():.4f}")
    print(f"내용: {documents[best_index]}")


if __name__ == "__main__":
    main()
