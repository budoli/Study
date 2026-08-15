from pathlib import Path
from collections import Counter

def normalize(text):
    return (
    text.lower()
    .replace(",", "")
    .replace(".", "")
    .replace("!", "")
    .replace("?", "")
    .split()
)

def read_token(path):
    text = Path(path).read_text(encoding="utf-8")
    return normalize(text)

def make_bow(tokens, vocabulary) :
    count = Counter(tokens)
    return [count[word] for word in vocabulary]

token_doc1 = read_token("data/sample_docs/day009_doc1.txt")
token_doc2 = read_token("data/sample_docs/day009_doc2.txt")
token_doc3 = read_token("data/sample_docs/day009_doc3.txt")

vocabulary = sorted(set(token_doc1+token_doc2+token_doc3))

print("Vocabulary:")
print(vocabulary)
print()
print("문서 1 BoW:")
print(make_bow(token_doc1, vocabulary))
print()
print("문서 2 BoW:")
print(make_bow(token_doc2, vocabulary))
print()
print("문서 3 BoW:")
print(make_bow(token_doc3, vocabulary))
