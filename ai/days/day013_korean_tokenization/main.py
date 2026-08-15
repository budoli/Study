"""Day 013 - Korean tokenization."""
from pathlib import Path
from collections import Counter

def main():
    file_path = Path("data/sample_docs/day013.txt")
    text = file_path.read_text(encoding="utf-8")

    tab_token = text.split()

    particles = ["은", "는", "이", "가", "을", "를", "의", "에", "로", "으로"]

    particles_token = []

    for token in tab_token:
        token = token.replace(".","")

        for particle in particles :
            if token.endswith(particle) :
                token = token[:-len(particle)]
                break

        particles_token.append(token)

    particles_token_count = Counter(particles_token)
    particles_token_common = particles_token_count.most_common(5)

    print("원본 텍스트:")
    print(text)
    print()
    print("공백 기준 토큰:")
    print(tab_token)
    print()
    print(f"공백 기중 토큰 개수:{len(tab_token)}")
    print()
    print("조사 제거 후 토큰:")
    print(particles_token)
    print()
    print(f"조사 제거 후 토큰 개수: {len(particles_token)}")
    print()
    print("단어 빈도 상위 5개:")
    for word, count in particles_token_common:
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()

