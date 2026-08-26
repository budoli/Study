# Week 04 - 조회 기능 고도화와 API 품질

## Day 22. 제목 검색 기능 만들기

### 목표

Todo 제목에 특정 문자열이 포함된 데이터만 조회합니다.

### 요구사항

- `GET /todos/search?keyword=spring` API를 만든다.
- Repository에 title contains 조회 메서드를 추가한다.
- 검색 결과를 `List<TodoResponse>`로 반환한다.

### 완료 기준

- keyword가 포함된 Todo만 반환된다.
- 대소문자 처리는 우선 신경 쓰지 않아도 된다.

### 회고 질문

- Spring Data JPA의 메서드 이름 쿼리는 어떻게 동작하는가?
- 검색 API는 목록 조회 API와 어떻게 구분하는 것이 좋은가?

## Day 23. 완료 상태 필터 만들기

### 목표

완료 여부에 따라 Todo 목록을 필터링합니다.

### 요구사항

- `GET /todos?completed=true` 요청을 지원한다.
- completed 값이 없으면 전체 목록을 반환한다.
- completed 값이 있으면 해당 상태만 반환한다.

### 완료 기준

- query parameter가 optional하게 동작한다.
- Service에서 분기 처리가 명확하다.

### 회고 질문

- 필수 파라미터와 선택 파라미터는 어떻게 다르게 받는가?
- Controller에서 분기할지 Service에서 분기할지 어떻게 판단하는가?

## Day 24. 페이징 적용하기

### 목표

데이터가 많아졌을 때 페이지 단위로 조회하는 방법을 익힙니다.

### 요구사항

- `GET /todos/page?page=0&size=10` API를 만든다.
- Repository에서 `Pageable`을 사용한다.
- 응답에는 content, page, size, totalElements 값을 포함한다.

### 완료 기준

- page와 size에 따라 조회 결과 개수가 달라진다.
- Page 객체에서 필요한 값을 꺼내 응답 DTO로 만든다.

### 회고 질문

- List와 Page는 무엇이 다른가?
- page 번호는 보통 0부터 시작하는가, 1부터 시작하는가?

## Day 25. 생성 시간과 정렬 추가

### 목표

Todo 생성 시간을 저장하고 최신순 정렬을 적용합니다.

### 요구사항

- `createdAt` 필드를 Entity에 추가한다.
- 생성 시 현재 시간이 저장되게 한다.
- 목록 조회를 최신순으로 반환한다.

### 완료 기준

- 응답에 createdAt이 포함된다.
- 새로 만든 Todo가 목록의 앞쪽에 나온다.

### 회고 질문

- createdAt은 사용자가 입력하는 값인가, 서버가 만드는 값인가?
- 정렬은 DB에서 하는 것이 좋은가, Java List에서 하는 것이 좋은가?

## Day 26. Validation 고도화

### 목표

잘못된 요청에 대해 더 명확한 에러 응답을 반환합니다.

### 요구사항

- Todo 생성 title은 비어 있으면 안 된다.
- title은 최대 100자까지만 허용한다.
- validation 실패 시 필드명과 메시지를 응답한다.

### 완료 기준

- `@NotBlank`, `@Size`를 사용한다.
- `MethodArgumentNotValidException`을 전역 처리한다.

### 회고 질문

- validation은 Controller, Service, Entity 중 어디에 두는 것이 좋은가?
- 에러 응답에 field 정보를 넣으면 무엇이 좋은가?

## Day 27. 공통 API 응답 포맷 만들기

### 목표

성공 응답과 실패 응답의 구조를 통일합니다.

### 요구사항

- 성공 응답 형식 예시:

```json
{
  "success": true,
  "data": {}
}
```

- 실패 응답 형식 예시:

```json
{
  "success": false,
  "message": "Todo not found"
}
```

- Todo API 일부에 공통 응답을 적용한다.

### 완료 기준

- 성공/실패 응답 구조가 일관된다.
- Controller 코드가 지나치게 복잡해지지 않는다.

### 회고 질문

- 모든 API에 공통 응답 포맷을 강제하는 것이 항상 좋은가?
- 프론트엔드 입장에서 응답 구조가 일정하면 무엇이 편한가?

## Day 28. 간단한 사용자 식별 추가

### 목표

인증의 아주 기초인 사용자별 데이터 분리 감각을 익힙니다.

### 요구사항

- 요청 헤더 `X-USER-ID`를 받는다.
- Todo에 `userId` 필드를 추가한다.
- 목록 조회 시 해당 userId의 Todo만 반환한다.
- 생성 시 해당 userId로 Todo가 저장된다.

### 완료 기준

- 사용자 A가 만든 Todo가 사용자 B 목록에 보이지 않는다.
- 아직 로그인/JWT는 구현하지 않는다.

### 회고 질문

- 인증과 인가는 무엇이 다른가?
- 헤더로 사용자 id를 받는 방식은 왜 실제 서비스에서 위험할 수 있는가?
