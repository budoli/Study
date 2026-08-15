from pathlib import Path
from collections import Counter

file_path = Path("data/sample_docs/day004.txt")

text = file_path.read_text(encoding="utf-8")

normalize_text = text.lower().replace(",","").replace(".","").replace("!","").replace("?","")

text_list = normalize_text.split()

count = Counter(text_list)

top_word = count.most_common(5)

print("단어 빈도 상위 5개:")
for word, count in top_word:
    print(f"{word}: {count}")