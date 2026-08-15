"""Day 016 - Sentence similarity."""
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
def main():
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

    query = "How can I find relevant documents?"

    sentences = [
    "RAG retrieves useful documents for a question.",
    "Python is used for data analysis.",
    "Search systems find relevant information.",
    "Machine learning trains models with data.",
    "NLP processes human language.",
    ]

    embeddings = model.encode(sentences)
    query_embeddings = model.encode([query])

    similarities = cosine_similarity(embeddings, query_embeddings)

    results = []
    for sentence, score in zip(sentences, similarities) :
        results.append((sentence, score[0]))

    results = sorted(results, key=lambda x: x[1], reverse=True)

    print("기준 문장:")
    print(query)
    print()
    print("문장별 유사도:")
    print()
    for sentence, score in results:
        print(sentence)
        print(f"유사도: {score:.4f}")
    print("가장 유사한 문장:")
    print(results[0][0])
    print(f"유사도: {results[0][1]:.4f}")

if __name__ == "__main__":
    main()
