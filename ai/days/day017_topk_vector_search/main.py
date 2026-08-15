"""Day 017 - Top-K vector search."""
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

def main():
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

    query = "How can I search relevant documents?"

    sentences = [
        "RAG retrieves relevant documents for a user question.",
        "Python is a programming language for automation.",
        "Search engines rank documents by relevance.",
        "NLP analyzes and processes human language.",
        "Vector search finds semantically similar text.",
        "Databases store structured business records.",
        "Question answering systems use retrieved context.",
    ]

    embeddings = model.encode(sentences)
    query_embedding = model.encode([query])

    similarities = cosine_similarity(embeddings, query_embedding)

    results = []

    for sentence , similar in zip(sentences, similarities) :
        results.append((sentence, similar[0]))

    results = sorted(results, key=lambda x : x[1], reverse=True)

    print("질문:")
    print(query)
    print()
    print("Top 3 검색 결과:")
    for i in range(0,3) :
        print(f"{i+1}. {results[i][0]}")
        print(f"유사도: {results[i][1]:.4f}")

if __name__ == "__main__":
    main()
