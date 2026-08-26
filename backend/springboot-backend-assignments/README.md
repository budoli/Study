# Spring Boot Backend 30-Day Assignments

Spring Boot와 PostgreSQL을 기반으로 백엔드 개발 기본기를 쌓기 위한 30일 과제 모음입니다.

목표는 AI 없이도 요구사항을 읽고, 직접 설계하고, 구현하고, 테스트하고, 회고할 수 있는 힘을 만드는 것입니다.

## 진행 규칙

- 하루에 하나의 Day 과제만 진행합니다.
- 먼저 요구사항을 읽고 직접 구현합니다.
- 막히면 바로 정답을 보지 말고, 아래 순서로 확인합니다.
  - 컴파일 에러 메시지 읽기
  - Controller, Service, Repository 흐름 다시 보기
  - 테스트를 먼저 작성하거나 수동 요청으로 동작 확인하기
  - 필요한 개념만 힌트로 확인하기
- 과제를 끝낸 뒤 `RETROSPECTIVE.md`에 간단히 회고합니다.

## 폴더 구성

| 파일 | 내용 |
|---|---|
| `week-01.md` | Day 1-7: Java, REST API, in-memory Todo |
| `week-02.md` | Day 8-14: Service 분리, 예외 처리, DTO, PostgreSQL/JPA |
| `week-03.md` | Day 15-21: JPA CRUD, Controller 테스트, Service 테스트 |
| `week-04.md` | Day 22-28: 검색, 페이징, validation 고도화, 인증 기초 |
| `week-05.md` | Day 29-30: 미니 프로젝트 정리, AI 백엔드 입문 |

## 30일 전체 로드맵

| Day | 주제 | 핵심 목표 |
|---:|---|---|
| 1 | Health API | Spring Boot 프로젝트 실행과 단순 응답 |
| 2 | Hello API | Query Parameter 처리 |
| 3 | Calculator API | 숫자 파라미터 처리와 응답 |
| 4 | Todo 목록 조회 | List와 in-memory 데이터 |
| 5 | Todo 단건 조회 | id 검색과 Optional 사고 |
| 6 | Todo 생성 | Request DTO와 새 객체 만들기 |
| 7 | Todo 수정/삭제 | 기본 CRUD 흐름 완성 |
| 8 | Service 분리 | Controller와 비즈니스 로직 분리 |
| 9 | Stream 기초 | List 변환과 filter/map |
| 10 | Optional 처리 | findFirst, orElseThrow |
| 11 | HTTP 상태 코드 | ResponseEntity 사용 |
| 12 | Custom Exception | 직접 예외 만들기 |
| 13 | Global Exception Handler | 예외 응답 공통화 |
| 14 | Response DTO | Entity/API 응답 분리 사고 |
| 15 | PostgreSQL 연결 | Docker Compose와 datasource |
| 16 | JPA Entity/Repository | DB 테이블과 Repository |
| 17 | JPA Create/List | DB 기반 생성/목록 |
| 18 | Controller Test | MockMvc로 API 테스트 |
| 19 | Service Test | Service와 Repository 통합 테스트 |
| 20 | Update/Delete Test | 변경/삭제 테스트 완성 |
| 21 | Transaction 이해 | 영속성 컨텍스트와 변경 감지 |
| 22 | 검색 기능 | title contains 검색 |
| 23 | 완료 상태 필터 | completed 조건 조회 |
| 24 | 페이징 | Pageable, Page 응답 |
| 25 | 정렬 | createdAt 기준 정렬 |
| 26 | Validation 고도화 | 메시지와 예외 응답 개선 |
| 27 | 공통 응답 포맷 | API 응답 구조 통일 |
| 28 | 인증 기초 | 간단한 사용자 식별 흐름 |
| 29 | 미니 프로젝트 리팩토링 | Todo API 전체 정리 |
| 30 | AI 백엔드 입문 | Prompt 요청 저장 API |

## 회고 템플릿

```md
## Day N 회고

- 오늘 구현한 것:
- 막혔던 부분:
- 해결한 방법:
- 새로 배운 개념:
- 다음에 조심할 점:
```
