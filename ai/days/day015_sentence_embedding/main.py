"""Day 015 - Sentence embedding."""
from sentence_transformers import SentenceTransformer

def main():

    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

    sentences = [
        "Python is useful for data analysis.",
        "NLP processes human language.",
        "RAG retrieves relevant documents.",
        "Search systems find useful information.",
        "Machine learning uses numerical vectors.",
    ]

    embeddings = model.encode(sentences)
    
    print("임베딩 타입:")
    print(type(embeddings))
    print()
    print("임베딩 shape:")
    print(embeddings.shape)
    print()
    print("첫 번째 문장 임베딩 앞 10개:")
    print(embeddings[0][:10])
    print()
    print("문장별 벡터 길이:")
    for index, text in enumerate(embeddings, start=0) :
        print(sentences[index])
        print(f"벡터 길이: {len(text)}")
        print()


if __name__ == "__main__":
    main()
