# Spring Boot 백엔드 학습 로드맵

## 목표

Spring Boot와 PostgreSQL 기반 백엔드 개발을 AI 도움 없이 직접 구현할 수 있는 수준까지 훈련한다.

초반에는 메모리 기반 API로 HTTP, Controller, DTO, List 처리, 예외 응답 흐름을 익히고, 이후 PostgreSQL, JPA, 인증, 테스트, AI API 연동으로 확장한다.

## 학습 규칙

- AI에게 정답 코드 요청 금지
- 막히면 힌트만 요청하기
- 공식 문서, 에러 메시지, 검색은 허용
- 하루 과제는 작게 끝내기
- 구현 후 직접 API 요청으로 확인하기
- 완료 후 `RETROSPECTIVE.md`에 회고 작성하기

---

## 전체 현황

| Day | 단계 | 과제 | 핵심 개념 | 완료 기준 | 상태 |
| --- | --- | --- | --- | --- | --- |
| 01 | API 기초 | Health Check API | `@GetMapping`, JSON 응답 | `GET /health` 성공 | 완료 |
| 02 | API 기초 | Hello API | `@RequestParam`, DTO 응답 | `GET /hello?name=chomi` 성공 | 완료 |
| 03 | API 기초 | Calculator Add API | 숫자 파라미터, 연산 응답 | `GET /calculator/add?a=3&b=5` 성공 | 완료 |
| 04 | Todo CRUD | Todo 생성 API | `@RequestBody`, `List`, `AtomicLong` | `POST /todos` 성공 | 완료 |
| 05 | Todo CRUD | Todo 목록 조회 API | `stream`, `map`, `toList` | `GET /todos` 성공 | 완료 |
| 06 | Todo CRUD | Todo 단건 조회 API | `@PathVariable`, `filter`, `findFirst`, 404 | `GET /todos/{id}` 성공 | 완료 |
| 07 | Todo CRUD | Todo 삭제 API | `@DeleteMapping`, 삭제 처리, 204 | `DELETE /todos/{id}` 성공 | 완료 |
| 08 | Todo CRUD | Todo 완료 처리 API | `@PatchMapping`, 상태 변경 | `PATCH /todos/{id}/complete` 성공 | 완료 |
| 09 | Todo CRUD | Todo 제목 수정 API | 수정 DTO, 기존 데이터 변경 | `PATCH /todos/{id}` 성공 | 완료 |
| 10 | Todo CRUD | Todo 입력 검증 | Validation, `@NotBlank`, `@Size` | 빈 title 요청 시 400 | 완료 |
| 11 | 구조 분리 | TodoService 분리 | Controller/Service 책임 분리 | Todo 로직 Service 이동 | 완료 |
| 12 | 예외 처리 | 공통 예외 처리 | `orElseThrow`, CustomException, Handler | 없는 id 요청 시 공통 404 | 완료 |
| 13 | 리팩터링 | 응답 변환 정리 | `from()` 메서드, 중복 제거 | 변환 로직 한 곳으로 이동 | 완료 |
| 14 | DB | PostgreSQL Docker Compose | Docker, datasource 설정 | Spring Boot DB 연결 성공 | 완료 |
| 15 | JPA | Todo Entity/Repository | Entity, `JpaRepository` | Todo DB 저장 성공 | 완료 |
| 16 | JPA | 조회 API JPA 전환 | Repository 조회, DB 기반 API | 메모리 List 제거 | 완료 |
| 17 | JPA | 수정/삭제 API JPA 전환 | `@Transactional`, 변경 감지, 삭제 | 수정/삭제 DB 반영 성공 | 완료 |
| 18 | 테스트 | Controller 테스트 | MockMvc, 요청/응답 검증 | 생성/목록/단건 테스트 성공 | 완료 |
| 19 | 테스트 | Testcontainers 적용 | PostgreSQL 통합 테스트 | 컨테이너 기반 테스트 성공 | 예정 |
| 20 | AI 준비 | 문서 API 확장 | Document 도메인, CRUD | 문서 생성/조회 성공 | 예정 |
| 21 | AI 준비 | AI 요약 구조 | `AiClient`, Fake 구현체 | 가짜 요약 응답 성공 | 예정 |
| 22 | AI 연동 | 실제 AI API 연동 | 환경 변수, 외부 API 호출 | 실제 요약 응답 성공 | 예정 |
| 23 | AI 연동 | 요약 결과 저장 | Summary Entity, 관계 설계 | 요약 결과 DB 저장 | 예정 |
| 24 | 비동기 | 비동기 요약 작업 | Job 상태, 비동기 처리 | job id 반환 후 처리 | 예정 |
| 25 | 채팅 | 채팅 세션 구조 | Session, Message 모델 | 세션별 메시지 저장 | 예정 |
| 26 | 문서 QA | 문서 기반 질문 API | 문서+질문 전달, 답변 저장 | 문서별 질문 응답 성공 | 예정 |
| 27 | RAG | 문서 Chunking | 긴 문서 분할, Chunk 저장 | 문서 저장 시 chunk 생성 | 예정 |
| 28 | RAG | Embedding 저장 구조 | 벡터 저장 설계, fake vector | chunk별 embedding 저장 | 예정 |
| 29 | RAG | 간단한 RAG 검색 | 관련 chunk 선택, 답변 생성 | 관련 문서 기반 답변 | 예정 |
| 30 | 정리 | 최종 프로젝트 정리 | README, 실행 방법, API 문서 | 처음 보는 사람이 실행 가능 | 예정 |
