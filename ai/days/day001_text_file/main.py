from pathlib import Path

file_path = Path("data/sample_docs/day001.txt")

if file_path.exists() :
    text = file_path.read_text(encoding="utf-8")
    print(text)
else :
    print("파일을 찾을 수 없습니다.")