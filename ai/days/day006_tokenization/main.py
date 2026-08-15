from pathlib import Path

file_path = Path("data/sample_docs/day006.txt")
text = file_path.read_text(encoding="utf-8")

basics_token = text.split()
normalized_token = (
    text.lower()
    .replace(",", "")
    .replace(".", "")
    .replace("!", "")
    .replace("?", "")
    .split()
)

unique_token = sorted(set(normalized_token))


print("원본 텍스트:")
print(text)
print()
print("기본 토큰:")
print(basics_token)
print()
print("정규화 토큰:")
print(normalized_token)
print()
print(f"기본 토큰 개수: {len(basics_token)}")
print(f"정규화 토큰 개수: {len(normalized_token)}")
print()
print("고유 토큰:")
print(unique_token)
print()
print(f"고유 토큰 개수: {len(unique_token)}")
