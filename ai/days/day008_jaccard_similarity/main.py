from pathlib import Path

def nomalized(text) :
    return (
    text.lower()
    .replace(",", "")
    .replace(".", "")
    .replace("!", "")
    .replace("?", "")
    .split()
)
def text_to_word_set(path) :
    text = Path(path).read_text(encoding="utf-8")
    normalized_token = nomalized(text)
    return set(normalized_token)

def jaccard_similarity(setA, setB) :
    intersection = setA & setB
    union = setA | setB

    if not union :
        return 0

    return len(intersection) / len(union)

unique_token_a = text_to_word_set("data/sample_docs/day008_doc1.txt")
unique_token_b = text_to_word_set("data/sample_docs/day008_doc2.txt")
unique_token_c = text_to_word_set("data/sample_docs/day008_doc3.txt")

print()
print("문서 A-B 비교")
print(f"교집합: {sorted(unique_token_a & unique_token_b)}")
print(f"합집합: {sorted(unique_token_a | unique_token_b)}")
print(f"Jaccard 유사도: {jaccard_similarity(unique_token_a, unique_token_b)}")
print()
print("문서 A-C 비교")
print(f"교집합: {sorted(unique_token_a & unique_token_c)}")
print(f"합집합: {sorted(unique_token_a | unique_token_c)}")
print(f"Jaccard 유사도: {jaccard_similarity(unique_token_a, unique_token_c)}")
print()
print("문서 B-C 비교")
print(f"교집합: {sorted(unique_token_b & unique_token_c)}")
print(f"합집합: {sorted(unique_token_b | unique_token_c)}")
print(f"Jaccard 유사도: {jaccard_similarity(unique_token_b, unique_token_c)}")

