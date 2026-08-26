# Week 02 - Service, 예외 처리, DTO 분리

## Day 8. Controller와 Service 분리

### 목표

Controller에 있던 비즈니스 로직을 Service로 옮깁니다.

### 요구사항

- `TodoService`를 만든다.
- Controller는 요청을 받고 Service를 호출만 한다.
- Todo 생성, 목록 조회, 단건 조회 로직을 Service로 이동한다.

### 완료 기준

- Controller 안에 List 직접 조작 코드가 줄어든다.
- Service 메서드 이름만 보고 역할을 알 수 있다.

### 회고 질문

- Controller와 Service를 나누는 이유는 무엇인가?
- Service 메서드는 어떤 단위로 나누는 것이 좋은가?

## Day 9. Stream으로 목록 변환하기

### 목표

`stream`, `map`, `filter`, `toList`의 기본 사용법을 익힙니다.

### 요구사항

- Todo 목록에서 완료된 Todo만 조회하는 메서드를 만든다.
- `for`문 대신 `stream().filter()`를 사용한다.
- 필요하다면 TodoResponse로 변환할 때 `map()`을 사용한다.

### 완료 기준

- `filter`로 조건 조회가 된다.
- `map`으로 응답 객체 변환이 된다.

### 회고 질문

- `filter`와 `map`은 각각 어떤 역할인가?
- stream은 원본 List를 바꾸는가?

## Day 10. Optional로 단건 조회 처리

### 목표

값이 있을 수도 없을 수도 있는 상황을 표현하는 방법을 익힙니다.

### 요구사항

- id로 Todo를 찾는 로직에서 `findFirst()`를 사용한다.
- 값이 없으면 예외를 던지거나 기본 응답을 반환한다.
- `orElseGet`, `orElseThrow` 중 하나를 사용해본다.

### 완료 기준

- 없는 id에 대한 처리가 명확하다.
- `Optional.get()`을 바로 사용하지 않는다.

### 회고 질문

- Optional은 null을 완전히 없애는 도구인가?
- `orElseGet`과 `orElseThrow`는 언제 다르게 쓰는가?

## Day 11. ResponseEntity로 상태 코드 반환

### 목표

HTTP 상태 코드를 직접 선택하는 방법을 익힙니다.

### 요구사항

- 생성 성공 시 201 Created를 반환한다.
- 단건 조회 실패 시 404 Not Found를 반환한다.
- 삭제 성공 시 204 No Content를 반환한다.

### 완료 기준

- `ResponseEntity.status(...)` 또는 `ResponseEntity.ok(...)`를 사용한다.
- body가 필요한 응답과 필요 없는 응답을 구분한다.

### 회고 질문

- 200, 201, 204, 404는 각각 어떤 의미인가?
- Controller에서 상태 코드를 다루는 것이 왜 필요한가?

## Day 12. Custom Exception 만들기

### 목표

Todo를 찾지 못한 상황을 직접 만든 예외로 표현합니다.

### 요구사항

- `TodoNotFoundException`을 만든다.
- 없는 id를 조회하면 이 예외를 던진다.
- Service에서는 `return null`을 사용하지 않는다.

### 완료 기준

- 예외 클래스가 따로 존재한다.
- Service 실패 흐름이 예외로 표현된다.

### 회고 질문

- `return null`보다 예외가 나은 상황은 언제인가?
- RuntimeException을 상속하면 무엇이 달라지는가?

## Day 13. Global Exception Handler 만들기

### 목표

예외 응답 처리를 한 곳으로 모읍니다.

### 요구사항

- `@RestControllerAdvice` 클래스를 만든다.
- `TodoNotFoundException`을 처리하는 `@ExceptionHandler`를 만든다.
- 404 상태 코드와 에러 메시지를 반환한다.

### 완료 기준

- Controller마다 try-catch를 작성하지 않는다.
- 없는 Todo 조회 시 404 응답이 나온다.

### 회고 질문

- 전역 예외 처리는 왜 필요한가?
- Service가 예외를 던지고 ControllerAdvice가 응답을 만드는 흐름을 설명할 수 있는가?

## Day 14. TodoResponse DTO 분리

### 목표

내부 객체와 API 응답 객체를 분리합니다.

### 요구사항

- `TodoResponse`를 만든다.
- Controller는 Entity나 내부 Todo 객체를 그대로 반환하지 않는다.
- `TodoResponse.from(...)` 정적 팩토리 메서드를 만들어본다.

### 완료 기준

- 응답으로 필요한 값만 노출한다.
- 변환 로직이 한 곳에 모인다.

### 회고 질문

- Request DTO와 Response DTO는 무엇이 다른가?
- `from` 메서드는 왜 유용한가?
