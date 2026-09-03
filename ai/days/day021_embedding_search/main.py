"""Day 021 - Embedding based document search."""

from pathlib import Path
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


def main():
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

    doc_file = [
        "data/sample_docs/day021_doc1.txt",
        "data/sample_docs/day021_doc2.txt",
        "data/sample_docs/day021_doc3.txt",
    ]

    chunks = []
    chunk_size = 100
    overlap = 20
    quest = "RAG에서 출처는 왜 필요한가요?"

    embeddings = model.encode([quest])

    for path in doc_file:
        text = Path(path).read_text(encoding="utf-8")
        step = chunk_size - overlap

        for chunk_id, start in enumerate(range(0, len(text), step), start=1):
            end = start + chunk_size

            chunk_text = text[start:end]

            if chunk_text:
                chunks.append(
                    {
                        "source": path,
                        "chunk_id": chunk_id,
                        "text": chunk_text,
                    }
                )

    chunk_texts = [chunk["text"] for chunk in chunks]

    chunk_embeddings = model.encode(chunk_texts)
    query_embedding = model.encode([quest])

    similarities = cosine_similarity(query_embedding, chunk_embeddings)[0]

    results = []

    for chunk, score in zip(chunks, similarities):
        results.append(
            {
                "source": chunk["source"],
                "chunk_id": chunk["chunk_id"],
                "score": score,
                "text": chunk["text"],
            }
        )

    results = sorted(results, key=lambda x: x["score"], reverse=True)
    top_results = results[:3]

    print("질문:")
    print(quest)
    print()
    print("Top 3 검색 결과:")
    print()

    for rank, result in enumerate(top_results, start=1):
        print(f"{rank}. score: {result['score']:.4f}")
        print(f"source: {result['source']}")
        print(f"chunk_id: {result['chunk_id']}")
        print("text:")
        print(result["text"])
        print()
        
if __name__ == "__main__":
    main()
