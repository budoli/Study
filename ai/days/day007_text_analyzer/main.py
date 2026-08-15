from pathlib import Path
from collections import Counter

file_path = Path("data/sample_docs/day007.txt")
text = file_path.read_text(encoding="utf-8")

lines = text.splitlines()
no_empty_line = [line for line in lines if line.strip()]

basics_token = text.split()
normalize_token = (
    text.lower()
    .replace(",", "")
    .replace(".", "")
    .replace("!", "")
    .replace("?", "")
    .split()
)
unique_token = sorted(set(normalize_token))

stopwords = {"is", "and", "for", "the", "a", "an"}
count = Counter(normalize_token)
top_filter = count.most_common(5)

remove_stopword = [word for word in normalize_token if word not in stopwords]
count_rs = Counter(remove_stopword)
top_filter_rs = count_rs.most_common(5)

print("원본 텍스트:")
print(text)
print()
print("기본 분석:")
print(f"전체 줄 수: {len(lines)}")
print(f"빈 줄 제외 줄 수: {len(no_empty_line)}")
print(f"기본 토큰 개수: {len(basics_token)}")
print(f"정규화 토큰 개수: {len(normalize_token)}")
print(f"고유 토큰 개수: {len(unique_token)}")
print()
print("단어 빈도 상위 5개:")
for word, count in top_filter:
    print(f"{word}: {count}")
print()
print("불용어 제거 후 단어 빈도 상위 5개:")
for word, count in top_filter_rs:
    print(f"{word}: {count}")
