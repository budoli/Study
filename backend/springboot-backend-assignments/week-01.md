# Week 01 - Spring Boot와 기본 REST API

## Day 1. Health API 만들기

### 목표

Spring Boot 서버가 정상 실행되는지 확인하는 가장 단순한 API를 만듭니다.

### 요구사항

- `GET /health` 요청을 만든다.
- 응답은 문자열 `"OK"`를 반환한다.
- 브라우저 또는 Postman에서 직접 호출해본다.

### 완료 기준

- 서버 실행이 된다.
- `GET /health` 호출 시 200 OK가 반환된다.
- 응답 body가 `OK`다.

### 회고 질문

- Controller는 어떤 역할을 하는가?
- `@GetMapping`은 언제 사용하는가?

## Day 2. Hello API 만들기

### 목표

Query Parameter를 받아 응답 문자열에 사용하는 방법을 익힙니다.

### 요구사항

- `GET /hello?name=kim` 요청을 만든다.
- 응답은 `"Hello kim"` 형태로 반환한다.
- `name`이 바뀌면 응답도 바뀌어야 한다.

### 완료 기준

- `@RequestParam`을 사용한다.
- `GET /hello?name=spring` 호출 시 `Hello spring`이 반환된다.

### 회고 질문

- Query Parameter는 URL의 어느 부분인가?
- `@RequestParam`이 없으면 값을 어떻게 받을 수 없게 되는가?

## Day 3. Calculator Add API 만들기

### 목표

숫자 파라미터를 받아 계산 결과를 반환합니다.

### 요구사항

- `GET /calculator/add?a=3&b=5` 요청을 만든다.
- 응답은 `8`을 반환한다.
- `a`, `b`는 정수로 받는다.

### 완료 기준

- `int` 또는 `long` 타입 파라미터를 사용한다.
- 덧셈 결과가 올바르게 반환된다.

### 회고 질문

- 문자열 파라미터와 숫자 파라미터는 받을 때 무엇이 다른가?
- 잘못된 숫자가 들어오면 어떤 에러가 발생하는가?

## Day 4. Todo 목록 조회 API 만들기

### 목표

`List`를 사용해 메모리 안의 Todo 목록을 반환합니다.

### 요구사항

- Todo는 `id`, `title`, `completed` 값을 가진다.
- `GET /todos` 요청을 만든다.
- 처음에는 Todo 2개 이상을 코드 안에 직접 만들어 반환한다.

### 완료 기준

- Todo 클래스를 만든다.
- `List<Todo>`를 반환한다.
- JSON 배열 응답이 나온다.

### 회고 질문

- `List`는 왜 필요한가?
- 객체를 반환하면 왜 JSON 형태로 보이는가?

## Day 5. Todo 단건 조회 API 만들기

### 목표

id로 Todo 하나를 찾는 흐름을 익힙니다.

### 요구사항

- `GET /todos/{id}` 요청을 만든다.
- path variable로 받은 id와 같은 Todo를 찾는다.
- 없으면 임시로 `null` 또는 에러 응답을 반환해도 된다.

### 완료 기준

- `@PathVariable`을 사용한다.
- `for`문 또는 `stream`으로 id가 같은 Todo를 찾는다.

### 회고 질문

- Path Variable과 Query Parameter는 무엇이 다른가?
- for문 안의 `return`은 어떤 흐름으로 동작하는가?

## Day 6. Todo 생성 API 만들기

### 목표

Request Body를 받아 새 Todo를 만드는 흐름을 익힙니다.

### 요구사항

- `POST /todos` 요청을 만든다.
- 요청 body는 `title`을 가진다.
- 새 Todo를 만들고 목록에 추가한다.
- 생성된 Todo를 응답으로 반환한다.

### 완료 기준

- Request DTO를 만든다.
- `@RequestBody`를 사용한다.
- 새 id를 부여한다.

### 회고 질문

- Request DTO는 왜 따로 만드는가?
- 새 Todo의 id는 어디서 만들어야 하는가?

## Day 7. Todo 수정/삭제 API 만들기

### 목표

기본 CRUD 중 update와 delete를 구현합니다.

### 요구사항

- `PATCH /todos/{id}/complete` 요청으로 완료 처리한다.
- `DELETE /todos/{id}` 요청으로 Todo를 삭제한다.
- 없는 id에 대해서는 임시 예외 또는 null 처리를 해도 된다.

### 완료 기준

- 완료 처리 후 `completed`가 `true`가 된다.
- 삭제 후 목록 조회에서 해당 Todo가 사라진다.

### 회고 질문

- 수정은 기존 객체를 바꾸는 것인가, 새 객체를 만드는 것인가?
- 삭제할 때 for문 안에서 바로 제거하면 어떤 문제가 생길 수 있는가?
