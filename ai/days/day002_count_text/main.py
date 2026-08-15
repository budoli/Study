from pathlib import Path

file_path = Path("data/sample_docs/day002.txt")
text = file_path.read_text(encoding="utf-8")

lines = text.splitlines()
non_empty_lines = [line for line in lines if line.strip()]

count = 0

for line in non_empty_lines :
    words = line.split()
    count += len(words)

print(f"전체 줄 수 : {len(lines)}")
print(f"빈 줄 제외 줄 수 : {len(non_empty_lines)}")
print(f"전체 단어 수 : {count}")

print('줄별 단어 수:')
for index, line in enumerate(non_empty_lines, start=1) :
    words = line.split()
    print(f"{index}번째 줄: {len(words)}개")


#splitlines 줄 나누기
#strip 빈줄 제외
#split 단어 나누기