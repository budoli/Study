from pathlib import Path
from collections import Counter

file_path = Path("data/sample_docs/day005.txt")
text = file_path.read_text(encoding="utf-8")
normalize_text = (
    text.lower().replace(",", "").replace(".", "").replace("!", "").replace("?", "")
)
text_list = normalize_text.split()

stopwords = {"is", "are", "and", "the", "for"}

filter_word = [word for word in text_list if word not in stopwords]

count = Counter(filter_word)

print("불용어 제거 전 단어 리스트:")
print(text_list)

print("불용어 제거 후 단어 리스트:")
print(filter_word)

top_filter = count.most_common(5)

print("불용어 제거 후 단어 빈도 상위 5개:")
for word, count in top_filter:
    print(f"{word}: {count}")
