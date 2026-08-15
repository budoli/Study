# NLP/RAG 30일 로드맵

| Day | 주제 | 문제명 | 핵심 | 노트 |
| --- | --- | --- | --- | --- |
| 001 | 파일 처리 | 텍스트 파일 읽기 | Path, read_text | [day001.md](./notes/day001.md) |
| 002 | 문자열 | 문장과 단어 세기 | split, strip | [day002.md](./notes/day002.md) |
| 003 | 문자열 | 구두점 제거와 정규화 | lower, replace | [day003.md](./notes/day003.md) |
| 004 | 빈도 분석 | 자주 나온 단어 찾기 | Counter | [day004.md](./notes/day004.md) |
| 005 | 전처리 | 불용어 제거 | stopwords | [day005.md](./notes/day005.md) |
| 006 | 토큰화 | 텍스트를 토큰으로 나누기 | tokenization | [day006.md](./notes/day006.md) |
| 007 | 미니과제 | 기본 텍스트 분석기 | file, count | [day007.md](./notes/day007.md) |
| 008 | 유사도 | 두 문서 비교하기 | Jaccard | [day008.md](./notes/day008.md) |
| 009 | 벡터화 | Bag of Words 만들기 | BoW | [day009.md](./notes/day009.md) |
| 010 | TF-IDF | 문서 키워드 뽑기 | TfidfVectorizer | [day010.md](./notes/day010.md) |
| 011 | 검색 | 질문과 가까운 문서 찾기 | cosine similarity | [day011.md](./notes/day011.md) |
| 012 | 검색 | 간단한 키워드 검색기 | ranking | [day012.md](./notes/day012.md) |
| 013 | 한국어 NLP | 한국어 토큰화 맛보기 | 형태소 분석 | [day013.md](./notes/day013.md) |
| 014 | 미니과제 | 문서 검색 CLI 만들기 | TF-IDF, CLI | [day014.md](./notes/day014.md) |
| 015 | 임베딩 | 문장을 숫자로 바꾸기 | embedding | [day015.md](./notes/day015.md) |
| 016 | 임베딩 | 문장 유사도 계산 | sentence-transformers | [day016.md](./notes/day016.md) |
| 017 | 벡터검색 | Top-K 문장 검색 | cosine, top-k | [day017.md](./notes/day017.md) |
| 018 | Chunking | 긴 문서 자르기 | chunk size | [day018.md](./notes/day018.md) |
| 019 | Chunking | 겹치게 자르기 | overlap | [day019.md](./notes/day019.md) |
| 020 | Metadata | 검색 결과에 출처 붙이기 | source, chunk_id | [day020.md](./notes/day020.md) |
| 021 | 미니과제 | 벡터 기반 문서 검색기 | embedding search | [day021.md](./notes/day021.md) |
| 022 | RAG | RAG 흐름 나누기 | Load, Split, Embed | [day022.md](./notes/day022.md) |
| 023 | RAG | 문서 로더 만들기 | loader | [day023.md](./notes/day023.md) |
| 024 | RAG | Retriever 만들기 | retrieve | [day024.md](./notes/day024.md) |
| 025 | RAG | Context 구성하기 | prompt context | [day025.md](./notes/day025.md) |
| 026 | RAG | 답변 템플릿 만들기 | generator | [day026.md](./notes/day026.md) |
| 027 | RAG | 출처 포함 답변 만들기 | sources | [day027.md](./notes/day027.md) |
| 028 | 미니과제 | CLI Q&A 봇 만들기 | RAG pipeline | [day028.md](./notes/day028.md) |
| 029 | FastAPI | 질문 API 만들기 | POST /ask | [day029.md](./notes/day029.md) |
| 030 | 종합 | 문서 기반 RAG API 완성 | FastAPI, RAG | [day030.md](./notes/day030.md) |

## 진행 방식

| 구간 | 방식 | 목표 |
| --- | --- | --- |
| 1주차 | 순수 Python | 텍스트 읽기와 기본 NLP |
| 2주차 | Python + scikit-learn | 유사도와 검색 |
| 3주차 | Python + embedding | 벡터 검색과 RAG 기초 |
| 4주차 | Python + FastAPI | RAG API 만들기 |
