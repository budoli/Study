from pathlib import Path

file_path = Path("data/sample_docs/day003.txt")
text = file_path.read_text(encoding="utf-8")
lines = text.splitlines()
no_empty_line = [line for line in lines if line.strip()] 

new_text = text.lower().replace(",", "").replace(".", "").replace("!", "").replace("?", "")
new_lines = new_text.splitlines()
no_empty_new_line = [new_line for new_line in new_lines if new_line.strip()]
new_normalized_words = new_text.split()

print("원본 텍스트:")
print(text)
print()
print("정규화된 텍스트:")
print(new_text)
print()

count = 0
for line in no_empty_line :
    words = line.split()
    count += len(words)

new_count = 0
for new_line in no_empty_new_line :
    new_words = new_line.split()
    new_count += len(new_words)
    

print(f"정규화 전 단어 수: {count}")
print(f"정규화 후 단어 수: {new_count}")
print()
print("정규화 된 단어 리스트:")
print(new_normalized_words)