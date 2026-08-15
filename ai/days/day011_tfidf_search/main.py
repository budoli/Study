from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

file_path = [
    "data/sample_docs/day011_doc1.txt",
    "data/sample_docs/day011_doc2.txt",
    "data/sample_docs/day011_doc3.txt"
]

documents = [
    Path(path).read_text(encoding="utf-8")
    for path in file_path
]

question = [
    "How does RAG find useful documents?"
]

vectorizer = TfidfVectorizer()
text_vector = vectorizer.fit_transform(documents)
question_vector = vectorizer.transform(question)

similarities = cosine_similarity(text_vector, question_vector)
best_index = similarities.argmax()

print(similarities)

print("질문:")
print("How does RAG find useful documents?")
print()
print("문서별 유사도:")
for index, similar in  enumerate(similarities, start=1):
    print(f"문서 {index}: {similar[0]:.4f}")
print()
print("가장 유사한 문서:")
print(f"문서번호: {best_index+1}")
print(f"유사도: {similarities.max():4f}")
print(f"내용: {documents[best_index]}")
