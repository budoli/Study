from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer

file_path = [
    "data/sample_docs/day010_doc1.txt",
    "data/sample_docs/day010_doc2.txt",
    "data/sample_docs/day010_doc3.txt"
]

documents = [
    Path(path).read_text(encoding="utf-8")
    for path in file_path
]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(documents)
feature_word = vectorizer.get_feature_names_out()

print("Vocabulary:")
print(feature_word)
print()

for index, row in enumerate(X.toarray(), start=1) :
    scores = list(zip(feature_word, row))
    top_scores = sorted(scores, key=lambda x:x[1], reverse=True)[:5]
    print(f"문서 {index} TF-IDF 상위 5개:")
    for word, score in top_scores :
        print(f"{word}: {score:.4f}")