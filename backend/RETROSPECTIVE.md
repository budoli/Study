# Backend 학습 회고록

## 학습 규칙

- AI에게 정답 코드 요청 금지
- 에러 메시지는 먼저 직접 읽기
- 막히면 힌트만 요청하기
- 하루 과제 완료 후 반드시 회고 작성
- 구현한 API는 직접 실행해서 확인하기

---

## 2026-07-22

### 오늘의 과제
`GET /hello?name=chomi` API 만들기

### 목표
쿼리 파라미터를 받아 JSON 응답을 반환하는 컨트롤러를 직접 작성한다.

### 구현한 것
- `@RestController`로 `HelloController` 생성
- `@RequestParam`으로 `name` 쿼리 파라미터 받기
- `record`로 `HelloResponse` DTO 생성
- `ResponseEntity.ok`로 JSON 응답 반환

### 배운 개념
- `@RequestMapping`은 컨트롤러 공통 경로를 지정한다.
- `@GetMapping`은 GET 요청을 처리한다.
- `@RequestParam`은 쿼리 파라미터를 받는다.
- `record`는 간단한 응답 DTO를 만들 때 사용할 수 있다.

### 다음에 개선할 점
- Java 코드 포맷을 일정하게 맞추기

---

## 2026-07-23

### 오늘의 과제
`GET /calculator/add?a=3&b=5` API 만들기

### 구현한 것
- `@RequestParam`으로 숫자 `a`, `b`를 받았다.
- 두 값을 더해서 `result`로 응답했다.
- `CalculatorResponse` record를 만들었다.

### 배운 개념
- Spring은 쿼리 파라미터를 `int`로 자동 변환해준다.
- `record`를 사용하면 간단한 JSON 응답 객체를 만들 수 있다.
- `@RequestMapping`과 `@GetMapping`을 조합해서 URL을 나눌 수 있다.

### 다음에 개선할 점
- Java 코드 포맷 맞추기
- 연산자 주변 공백 넣기

---

## 2026-07-24

### 오늘의 과제
Todo 생성 API 만들기

### 구현한 것
- `POST /todos` API를 만들었다.
- `@RequestBody`로 JSON 요청을 받았다.
- `List<Todo>`를 사용해서 메모리에 Todo를 저장했다.
- `AtomicLong`으로 id를 자동 증가시켰다.
- 생성된 Todo를 `TodoResponse`로 반환했다.

### 막힌 부분
- `List<Todo>`를 비워둬도 되는지 헷갈렸다.
- `Todo.java` 파일과 `List<Todo>`의 역할 차이를 헷갈렸다.
- `TodoResponse`를 만들 때 값을 어떻게 넣어야 하는지 고민했다.

### 배운 개념
- `List<Todo>`는 데이터를 저장하는 임시 저장소다.
- `Todo.java`는 Todo 데이터의 구조를 정의하는 파일이다.
- `record`는 생성할 때 필드 값을 모두 넣어야 한다.
- 새 Todo를 만들 때 `completed` 기본값은 `false`로 설정해야 한다.

### 테스트한 요청
- `POST /todos`
- 요청 body: `{ "title": "Spring 공부하기" }`

### 다음에 개선할 점
- Java 코드 포맷을 더 깔끔하게 맞추기
- 요청 객체, 저장 객체, 응답 객체의 역할을 더 명확히 이해하기

---

## 2026-07-24

### 오늘의 과제
Todo 목록 조회 API 만들기

### 구현한 것
- `GET /todos` API를 만들었다.
- 기존에 저장된 `List<Todo>`를 조회했다.
- `Todo` 객체를 `TodoResponse` 객체로 변환했다.
- `List<TodoResponse>` 형태로 응답을 반환했다.
- `stream().map().toList()`를 사용해서 리스트 변환을 처리했다.

### 막힌 부분
- `stream()`이 정확히 어떤 역할을 하는지 헷갈렸다.
- `List<Todo>`를 그대로 반환하는 것과 `List<TodoResponse>`로 변환해서 반환하는 것의 차이를 이해해야 했다.

### 배운 개념

#### stream
`stream()`은 리스트 안의 데이터를 하나씩 처리하기 위한 흐름을 만드는 기능이다.

예를 들어 `List<Todo>`가 있을 때:

```java
todos.stream()
```

이라고 쓰면 `todos` 안에 있는 Todo들을 하나씩 꺼내서 처리할 수 있는 상태가 된다.

#### map
`map()`은 stream으로 흘러가는 각각의 값을 다른 값으로 바꾸는 기능이다.

이번 과제에서는:

```txt
Todo -> TodoResponse
```

로 바꾸는 데 사용했다.

```java
.map(todo -> new TodoResponse(
    todo.id(),
    todo.title(),
    todo.completed()
))
```

#### toList
`toList()`는 stream으로 처리한 결과를 다시 리스트로 모아준다.

전체 흐름은 이렇게 이해할 수 있다.

```txt
List<Todo>
-> stream()
-> Todo를 하나씩 꺼냄
-> map()으로 TodoResponse로 변환
-> toList()
-> List<TodoResponse>
```

반복문으로 쓰면 아래 코드와 비슷하다.

```java
List<TodoResponse> responses = new ArrayList<>();

for (Todo todo : todos) {
    TodoResponse response = new TodoResponse(
        todo.id(),
        todo.title(),
        todo.completed()
    );

    responses.add(response);
}
```

stream을 쓰면 이 반복과 변환 과정을 더 짧게 표현할 수 있다.

```java
List<TodoResponse> responses = todos.stream()
    .map(todo -> new TodoResponse(
        todo.id(),
        todo.title(),
        todo.completed()
    ))
    .toList();
```

### 테스트한 요청
- `POST /todos`
- `POST /todos`
- `GET /todos`

### 테스트 결과
- Todo 2개 생성 후 목록 조회 성공
- 응답에 `id`, `title`, `completed`가 정상적으로 포함됨
- `completed` 기본값은 `false`로 반환됨

### 다음에 개선할 점
- `stream()` 문법에 익숙해지기
- `for문`과 `stream` 방식의 차이를 비교해보기
- `Todo.java` 코드 포맷 깔끔하게 정리하기

---

## 2026-07-24

### 오늘의 과제
Todo 단건 조회 API 만들기

### 구현한 것
- `GET /todos/{id}` API를 만들었다.
- `@PathVariable`로 URL 경로의 id 값을 받았다.
- `List<Todo>`에서 id가 같은 Todo를 찾았다.
- 찾은 Todo를 `TodoResponse`로 변환해서 반환했다.
- 없는 id를 요청하면 `404 Not Found`를 반환했다.

### 배운 개념

#### @PathVariable
`@PathVariable`은 URL 경로에 들어간 값을 메서드 파라미터로 받을 때 사용한다.

```java
@GetMapping("/{id}")
public ResponseEntity<TodoResponse> getTodo(
    @PathVariable long id
)
```

요청이 아래처럼 들어오면:

```http
GET /todos/1
```

`id` 값에는 `1`이 들어간다.

`@RequestParam`과 차이:

```txt
@RequestParam
/todos?id=1

@PathVariable
/todos/1
```

#### filter
`filter()`는 stream 안에서 조건에 맞는 값만 남기는 기능이다.

```java
.filter(todo -> todo.id() == id)
```

이 코드는 Todo 목록 중에서 요청으로 받은 id와 같은 Todo만 남긴다.

#### findFirst
`findFirst()`는 stream에서 조건에 맞는 첫 번째 값을 하나 꺼낸다.

```java
.findFirst()
```

찾는 값이 있을 수도 있고 없을 수도 있기 때문에 결과는 `Optional<Todo>`가 된다.

```txt
값이 있으면 Optional 안에 Todo가 들어 있음
값이 없으면 Optional이 비어 있음
```

#### map
`map()`은 Optional 안에 값이 있을 때 그 값을 다른 값으로 바꾼다.

이번 과제에서는:

```txt
Todo -> ResponseEntity<TodoResponse>
```

로 변환했다.

```java
.map(todo -> ResponseEntity.ok(new TodoResponse(
    todo.id(),
    todo.title(),
    todo.completed()
)))
```

#### orElseGet
`orElseGet()`은 Optional 안에 값이 없을 때 실행할 코드를 정한다.

```java
.orElseGet(() -> ResponseEntity.notFound().build())
```

여기서 `() ->`는 “나중에 실행할 함수”를 의미한다.

```txt
Todo를 찾으면 map 실행 -> 200 OK
Todo를 못 찾으면 orElseGet 실행 -> 404 Not Found
```

### 전체 흐름

```txt
GET /todos/1 요청
-> @PathVariable로 id 받기
-> todos.stream()
-> filter로 id가 같은 Todo만 남기기
-> findFirst로 하나 찾기
-> 있으면 TodoResponse로 변환 후 200 OK
-> 없으면 404 Not Found
```

### 테스트한 요청
- `POST /todos`
- `GET /todos/1`
- `GET /todos/999`

### 테스트 결과
- `/todos/1` 요청 시 생성한 Todo가 정상 반환됨
- `/todos/999` 요청 시 `404 Not Found` 반환됨

### 다음에 개선할 점
- 단건 조회 메서드명은 `getTodos`보다 `getTodo` 또는 `getTodoById`가 더 자연스럽다.
- `Todo -> TodoResponse` 변환 코드가 반복되고 있으므로 나중에 리팩터링할 수 있다.
- 이후에는 `Service` 계층을 분리해서 컨트롤러의 책임을 줄일 수 있다.

---

## 2026-07-27

### 오늘의 과제
Todo 삭제 API 만들기

### 구현한 것
- `DELETE /todos/{id}` API를 만들었다.
- `@DeleteMapping("/{id}")`를 사용했다.
- `@PathVariable`로 URL의 id 값을 받았다.
- `removeIf`를 사용해서 id가 같은 Todo를 삭제했다.
- 삭제 성공 시 `204 No Content`를 반환했다.
- 삭제할 Todo가 없으면 `404 Not Found`를 반환했다.

### 배운 개념

#### @DeleteMapping
`@DeleteMapping`은 DELETE HTTP 요청을 처리할 때 사용한다.

```java
@DeleteMapping("/{id}")
```

위 코드는 아래 요청을 처리한다.

```http
DELETE /todos/1
```

#### removeIf
`removeIf`는 리스트에서 조건에 맞는 요소를 삭제한다.

```java
todos.removeIf(todo -> todo.id() == id)
```

조건에 맞는 Todo가 있으면 삭제하고 `true`를 반환한다. 조건에 맞는 Todo가 없으면 삭제하지 않고 `false`를 반환한다.

```txt
true  -> 삭제 성공
false -> 삭제할 데이터 없음
```

#### 204 No Content
`204 No Content`는 요청은 성공했지만 응답 body가 없다는 뜻이다.

삭제 API에서는 보통 삭제 성공 시 아래처럼 응답한다.

```java
ResponseEntity.noContent().build()
```

#### 404 Not Found
삭제하려는 id가 존재하지 않으면 `404 Not Found`를 반환한다.

```java
ResponseEntity.notFound().build()
```

### 전체 흐름

```txt
DELETE /todos/1 요청
-> @PathVariable로 id 받기
-> removeIf로 id가 같은 Todo 삭제 시도
-> 삭제 성공이면 true
-> 204 No Content 반환
-> 삭제할 Todo가 없으면 false
-> 404 Not Found 반환
```

### 테스트한 요청
- `POST /todos`
- `DELETE /todos/2`
- `GET /todos/2`
- `DELETE /todos/999`

### 테스트 결과
- Todo 생성 성공
- 생성된 Todo 삭제 성공
- 삭제 성공 시 `204 No Content` 반환
- 삭제 후 단건 조회 시 `404 Not Found` 반환
- 없는 id 삭제 시 `404 Not Found` 반환

### 다음에 개선할 점
- 삼항 연산자가 길어질 때는 줄바꿈해서 가독성을 높이기
- 삭제 로직도 나중에 `TodoService`로 분리하기
- `removeIf` 외에도 `findFirst` 후 삭제하는 방식과 비교해보기

---

## 2026-07-27

### 오늘의 과제
Todo 완료 처리 API 만들기

### 구현한 것
- `PATCH /todos/{id}/complete` API를 만들었다.
- `@PatchMapping("/{id}/complete")`를 사용했다.
- `@PathVariable`로 URL의 id 값을 받았다.
- `for`문으로 `List<Todo>`의 index를 순회했다.
- id가 같은 Todo를 찾은 뒤 `completed` 값이 `true`인 새 Todo를 만들었다.
- `todos.set(i, updatedTodo)`로 기존 Todo를 새 Todo로 교체했다.
- 변경된 Todo를 `TodoResponse`로 반환했다.
- 없는 id를 요청하면 `404 Not Found`를 반환했다.

### 막힌 부분
- `record`의 값을 직접 수정할 수 있는지 헷갈렸다.
- 기존 Todo의 `id`, `title`을 유지하면서 `completed`만 바꾸는 방법을 고민했다.
- `for`문 안에서 언제 `return`해야 하는지 헷갈렸다.
- `else`에서 바로 404를 반환하면 아직 뒤의 Todo를 확인하지 못한다는 점을 배웠다.
- 처음에는 응답을 수정 전 `todo` 기준으로 만들어서 `completed=false`가 반환됐다.

### 배운 개념

#### @PatchMapping
`@PatchMapping`은 리소스의 일부 상태를 변경할 때 사용하는 PATCH 요청을 처리한다.

```java
@PatchMapping("/{id}/complete")
```

위 코드는 아래 요청을 처리한다.

```http
PATCH /todos/1/complete
```

#### record는 불변 객체
Java `record`는 한 번 만들어지면 내부 값을 직접 바꿀 수 없다.

따라서 아래처럼 기존 Todo의 `completed` 값만 직접 바꾸는 방식은 사용할 수 없다.

```java
todo.completed = true;
```

대신 기존 Todo의 값을 꺼내서 새 Todo를 만들어야 한다.

```java
Todo updatedTodo = new Todo(
    todo.id(),
    todo.title(),
    true
);
```

#### List.set
`List.set(index, value)`는 리스트의 특정 위치에 있는 값을 새 값으로 교체한다.

```java
todos.set(i, updatedTodo);
```

이번 과제에서는 기존 Todo를 직접 수정하는 대신 같은 위치에 새 Todo를 넣었다.

#### for문과 return 위치
id를 찾는 과정에서 `else` 안에서 바로 404를 반환하면 안 된다.

예를 들어 찾는 id가 3인데 첫 번째 Todo의 id가 1이면, 아직 뒤의 Todo를 확인하지 않았는데 바로 404가 반환된다.

따라서 흐름은 아래처럼 가야 한다.

```txt
for문으로 끝까지 찾기
-> 중간에 찾으면 수정 후 200 OK 반환
-> 끝까지 못 찾으면 for문 밖에서 404 반환
```

### 전체 흐름

```txt
PATCH /todos/1/complete 요청
-> @PathVariable로 id 받기
-> for문으로 todos 순회
-> id가 같은 Todo 찾기
-> 기존 id, title은 유지하고 completed=true인 새 Todo 만들기
-> todos.set(i, updatedTodo)로 교체
-> updatedTodo 기준으로 TodoResponse 생성
-> 200 OK 반환
-> 끝까지 못 찾으면 404 Not Found 반환
```

### 테스트한 요청
- `POST /todos`
- `PATCH /todos/1/complete`
- `GET /todos/1`
- `PATCH /todos/999/complete`

### 테스트 결과
- Todo 생성 성공
- 완료 처리 후 응답에서 `completed=true` 반환
- 단건 조회에서도 `completed=true` 확인
- 없는 id 완료 처리 요청 시 `404 Not Found` 반환

### 다음에 개선할 점
- `Todo -> TodoResponse` 변환 코드가 반복되므로 나중에 `TodoResponse.from(todo)`로 정리하기
- 상태 변경 로직도 나중에 `TodoService`로 분리하기
- 같은 날짜에 여러 과제를 하면 회고 제목에 과제명을 명확히 적기

---

## 2026-07-28

### 오늘의 과제
Todo 제목 수정 API 만들기

### 구현한 것
- `PATCH /todos/{id}` API를 만들었다.
- `@PatchMapping("/{id}")`를 사용했다.
- `@PathVariable`로 URL의 id 값을 받았다.
- `@RequestBody`로 JSON 요청 body를 받았다.
- `TodoUpdateRequest` record를 만들었다.
- 기존 Todo의 `id`, `completed`는 유지하고 `title`만 변경했다.
- `record`는 불변이므로 새 Todo를 만들어 `todos.set(i, updateTodo)`로 교체했다.
- 수정된 Todo를 `TodoResponse`로 반환했다.
- 없는 id를 요청하면 `404 Not Found`를 반환했다.

### 막힌 부분
- 처음에는 `@RequestBody String title`로 받았는데, JSON 전체가 문자열로 들어갔다.
- 원하는 값은 `Spring Boot 복습하기`였지만 실제로는 `{"title":"Spring Boot 복습하기"}` 형태가 title에 저장됐다.
- JSON 요청은 단순 `String`보다 요청 DTO로 받는 것이 더 적절하다는 점을 배웠다.

### 배운 개념

#### 요청 DTO
요청 body의 구조가 JSON 객체라면 그 모양에 맞는 DTO를 만드는 것이 좋다.

```json
{
  "title": "Spring Boot 복습하기"
}
```

위 요청은 아래처럼 `title` 필드를 가진 record로 받을 수 있다.

```java
public record TodoUpdateRequest(
    String title
) {
}
```

#### @RequestBody와 DTO
`@RequestBody`는 요청 body의 JSON을 Java 객체로 변환해준다.

```java
@RequestBody TodoUpdateRequest updateRequest
```

이렇게 받으면 요청 JSON의 `title` 값을 아래처럼 꺼낼 수 있다.

```java
updateRequest.title()
```

#### 기존 값 유지 + 일부 값 변경
제목 수정 API에서는 기존 Todo의 `id`, `completed`는 유지하고 `title`만 변경해야 한다.

```txt
기존 Todo
id 유지
completed 유지
title만 request.title()로 변경
```

record는 불변 객체이므로 기존 Todo를 직접 수정하지 않고 새 Todo를 만들어 교체했다.

```java
Todo updateTodo = new Todo(
    todo.id(),
    updateRequest.title(),
    todo.completed()
);
```

#### 완료 처리 API와 제목 수정 API 비교

```txt
완료 처리 API
id 유지
title 유지
completed만 true로 변경

제목 수정 API
id 유지
completed 유지
title만 request.title()로 변경
```

두 API 모두 기존 객체를 직접 바꾸지 않고 새 Todo를 만든 뒤 `todos.set(i, updatedTodo)`로 교체한다.

### 전체 흐름

```txt
PATCH /todos/1 요청
-> @PathVariable로 id 받기
-> @RequestBody로 TodoUpdateRequest 받기
-> for문으로 todos 순회
-> id가 같은 Todo 찾기
-> 기존 id, completed는 유지하고 title만 변경한 새 Todo 만들기
-> todos.set(i, updateTodo)로 교체
-> updateTodo 기준으로 TodoResponse 생성
-> 200 OK 반환
-> 끝까지 못 찾으면 404 Not Found 반환
```

### 테스트한 요청
- `POST /todos`
- `PATCH /todos/1`
- `GET /todos/1`
- `PATCH /todos/999`

### 테스트 결과
- Todo 생성 성공
- 제목 수정 후 응답에서 변경된 title 반환
- 단건 조회에서도 변경된 title 확인
- 기존 `completed=false` 값 유지
- 없는 id 제목 수정 요청 시 `404 Not Found` 반환

### 다음에 개선할 점
- `for (int i=0; i<todos.size(); i++)` 같은 코드에 공백을 넣어 포맷 정리하기
- 생성, 완료 처리, 제목 수정에서 반복되는 `TodoResponse` 변환 코드를 나중에 정리하기
- 수정 로직이 늘어나고 있으므로 이후 `TodoService`로 분리하기

---

## 2026-07-28

### 오늘의 과제
Todo 입력 검증 추가하기

### 구현한 것
- `spring-boot-starter-validation` 의존성을 추가했다.
- `TodoCreateRequest`에 검증 어노테이션을 추가했다.
- `TodoUpdateRequest`에 검증 어노테이션을 추가했다.
- `title`이 비어 있거나 공백만 있는 요청을 막았다.
- `title` 길이가 100자를 넘는 요청을 막았다.
- Controller의 `@RequestBody` 앞에 `@Valid`를 추가했다.
- 잘못된 요청이 들어오면 `400 Bad Request`가 반환되도록 만들었다.

### 막힌 부분
- DTO에 검증 어노테이션을 붙이는 것과 Controller에서 `@Valid`를 붙이는 것의 역할 차이를 이해해야 했다.
- `@NotBlank`와 `@Size`가 각각 어떤 검증을 담당하는지 정리할 필요가 있었다.

### 배운 개념

#### Bean Validation
Bean Validation은 요청 DTO 같은 객체의 필드 값이 규칙에 맞는지 검사하는 기능이다.

Spring Boot에서는 validation 의존성을 추가해야 사용할 수 있다.

```gradle
implementation 'org.springframework.boot:spring-boot-starter-validation'
```

#### @NotBlank
`@NotBlank`는 문자열이 비어 있거나 공백만 있는 경우를 막는다.

```java
@NotBlank
String title
```

아래 요청들은 실패한다.

```json
{
  "title": ""
}
```

```json
{
  "title": "   "
}
```

#### @Size
`@Size`는 문자열 길이를 제한할 때 사용한다.

```java
@Size(max = 100)
String title
```

이번 과제에서는 `title`을 최대 100자까지만 허용했다.

#### @Valid
`@Valid`는 RequestBody 객체 안에 있는 검증 어노테이션을 실제로 실행하게 만든다.

```java
public ResponseEntity<TodoResponse> createTodo(
    @Valid @RequestBody TodoCreateRequest request
)
```

DTO에 `@NotBlank`, `@Size`를 붙여도 Controller 파라미터에 `@Valid`가 없으면 검증이 실행되지 않는다.

### 전체 흐름

```txt
POST /todos 요청
-> JSON body가 TodoCreateRequest로 변환됨
-> @Valid가 DTO 검증 실행
-> @NotBlank로 빈 문자열/공백 문자열 검사
-> @Size로 길이 검사
-> 검증 성공이면 기존 로직 실행
-> 검증 실패면 400 Bad Request 반환
```

```txt
PATCH /todos/1 요청
-> JSON body가 TodoUpdateRequest로 변환됨
-> @Valid가 DTO 검증 실행
-> title 검증 성공 시 제목 수정
-> 검증 실패 시 400 Bad Request 반환
```

### 테스트한 요청
- 정상 title로 `POST /todos`
- 빈 title로 `POST /todos`
- 공백 title로 `POST /todos`
- 101자 이상 title로 `POST /todos`
- 빈 title로 `PATCH /todos/1`

### 테스트 결과
- 정상 생성 요청 성공
- 빈 title 생성 요청 시 `400 Bad Request`
- 공백 title 생성 요청 시 `400 Bad Request`
- 101자 이상 title 생성 요청 시 `400 Bad Request`
- 빈 title 수정 요청 시 `400 Bad Request`

### 다음에 개선할 점
- 검증 어노테이션을 줄바꿈해서 가독성 높이기
- 나중에 `GlobalExceptionHandler`를 만들어 validation 에러 응답 형식을 직접 정리하기
- 생성 요청과 수정 요청의 검증 규칙이 같을 때 중복을 어떻게 줄일 수 있는지 고민하기

---

## 2026-07-29

### 오늘의 과제
TodoService 분리하기

### 구현한 것
- `TodoService` 인터페이스를 만들었다.
- `TodoServiceImpl` 구현 클래스를 만들었다.
- `@Service`를 사용해서 Service를 Spring Bean으로 등록했다.
- Controller에 있던 `List<Todo>`와 `AtomicLong`을 Service로 이동했다.
- Todo 생성, 목록 조회, 단건 조회, 삭제, 완료 처리, 제목 수정 로직을 Service로 옮겼다.
- Controller는 Service를 호출하고 HTTP 응답으로 변환하는 역할만 하도록 정리했다.
- 없는 Todo를 표현하기 위해 `Optional<TodoResponse>`를 사용했다.
- 삭제 성공/실패는 `boolean`으로 표현했다.

### 막힌 부분
- Service에서 Todo를 찾지 못했을 때 `return null`을 사용해도 되는지 고민했다.
- `null`을 반환하면 Controller에서 `200 OK + null`처럼 잘못 응답될 수 있다는 점을 배웠다.
- `Optional`을 Controller 응답 body로 직접 반환하려고 해서 타입 처리가 헷갈렸다.
- `Optional`은 boolean이 아니므로 삼항 연산자의 조건으로 쓸 수 없다는 점을 배웠다.
- `ResponseEntity.ok()`와 `ResponseEntity.ok(response)`의 차이 때문에 타입 오류가 발생했다.

### 배운 개념

#### Controller와 Service 역할 분리
Controller는 HTTP 요청과 응답을 담당한다.

```txt
요청 받기
PathVariable, RequestBody 받기
Service 호출하기
ResponseEntity로 응답 만들기
```

Service는 실제 Todo 처리 로직을 담당한다.

```txt
Todo 생성
Todo 조회
Todo 삭제
Todo 수정
List<Todo> 관리
id 생성
```

#### @Service
`@Service`는 해당 클래스를 Spring Bean으로 등록한다.

```java
@Service
public class TodoServiceImpl implements TodoService {
}
```

이렇게 등록된 Service는 Controller에서 생성자 주입으로 사용할 수 있다.

#### Optional
`Optional`은 값이 있을 수도 있고 없을 수도 있음을 표현한다.

```java
Optional<TodoResponse>
```

의미:

```txt
값 있음 -> Todo를 찾았다
값 없음 -> Todo를 찾지 못했다
```

Service에서는 못 찾은 경우 `null` 대신 아래처럼 표현한다.

```java
return Optional.empty();
```

찾은 경우에는 아래처럼 감싼다.

```java
return Optional.of(response);
```

#### Optional을 HTTP 응답으로 변환하기
Controller에서는 Service가 반환한 `Optional<TodoResponse>`를 HTTP 응답으로 변환한다.

```java
return todoService.getTodo(id)
    .map(ResponseEntity::ok)
    .orElseGet(() -> ResponseEntity.notFound().build());
```

흐름:

```txt
Optional 안에 값 있음
-> ResponseEntity.ok(response)
-> 200 OK

Optional 비어 있음
-> ResponseEntity.notFound().build()
-> 404 Not Found
```

#### ResponseEntity.ok()와 ResponseEntity.ok(response)
`ResponseEntity.ok()`는 body가 없는 응답을 만들기 위한 builder에 가깝다.

`ResponseEntity.ok(response)`는 실제 응답 body를 포함한 `ResponseEntity<TodoResponse>`를 만든다.

이번 과제에서는 Todo 응답을 내려야 하므로 아래 형태가 필요했다.

```java
ResponseEntity.ok(response)
```

#### 삭제 결과는 boolean으로 표현
삭제 API는 응답 body가 필요하지 않다.

Service에서는 삭제 성공 여부만 알려주면 된다.

```java
boolean deleteTodo(long id)
```

Controller는 boolean 값을 HTTP 응답으로 바꾼다.

```txt
true -> 204 No Content
false -> 404 Not Found
```

### 전체 흐름

```txt
POST /todos
-> Controller가 요청 DTO 검증
-> Service.createTodo 호출
-> Service가 Todo 생성 후 List에 저장
-> Controller가 200 OK 반환
```

```txt
GET /todos/1
-> Controller가 id 받기
-> Service.getTodo 호출
-> Service가 Optional<TodoResponse> 반환
-> 값 있으면 200 OK
-> 값 없으면 404 Not Found
```

```txt
DELETE /todos/1
-> Controller가 id 받기
-> Service.deleteTodo 호출
-> true면 204 No Content
-> false면 404 Not Found
```

### 테스트한 요청
- `POST /todos`
- `GET /todos`
- `GET /todos/1`
- `GET /todos/999`
- `PATCH /todos/1/complete`
- `PATCH /todos/999/complete`
- `PATCH /todos/1`
- `PATCH /todos/999`
- `DELETE /todos/1`
- `DELETE /todos/999`

### 테스트 결과
- 전체 API가 Service 분리 후에도 기존과 동일하게 동작했다.
- 생성, 목록 조회, 단건 조회 성공
- 없는 id 조회 시 `404 Not Found`
- 완료 처리 성공
- 없는 id 완료 처리 시 `404 Not Found`
- 제목 수정 성공
- 없는 id 제목 수정 시 `404 Not Found`
- 삭제 성공 시 `204 No Content`
- 없는 id 삭제 시 `404 Not Found`

### 다음에 개선할 점
- 반복되는 `Todo -> TodoResponse` 변환 코드를 `TodoResponse.from(todo)`로 정리하기
- `TodoService` 인터페이스와 구현체 분리가 꼭 필요한지 나중에 다시 판단하기
- `GlobalExceptionHandler`를 도입하면 `Optional` 처리 대신 `orElseThrow()`를 사용할 수 있다.
- Controller는 HTTP 처리, Service는 비즈니스 로직이라는 역할 구분을 계속 유지하기

---

## 2026-07-31

### 오늘의 과제
공통 예외 처리 만들기

### 구현한 것
- `TodoNotFoundException` custom exception을 만들었다.
- `RuntimeException`을 상속해서 Todo를 찾지 못한 상황을 표현했다.
- `GlobalExceptionHandler`를 만들었다.
- `@RestControllerAdvice`를 사용했다.
- `@ExceptionHandler(TodoNotFoundException.class)`를 사용해서 Todo 조회 실패 예외를 잡았다.
- Service에서 Todo를 찾지 못하면 `TodoNotFoundException`을 던지도록 수정했다.
- Controller에서 `Optional` 처리 로직을 제거하고 성공 응답 중심으로 단순화했다.
- 없는 Todo 조회, 완료 처리, 제목 수정 요청이 `404 Not Found`로 반환되도록 만들었다.

### 막힌 부분
- `Custom Exception`을 어떤 형태로 만들어야 하는지 헷갈렸다.
- `Optional`을 더 이상 Controller로 반환하지 않는 구조가 처음에는 어색했다.
- Service의 for문에서 못 찾았을 때 무엇을 반환해야 하는지 고민했다.
- `GlobalExceptionHandler`에 `@ExceptionHandler`를 붙이지 않으면 Spring이 예외 처리 메서드로 인식하지 않는다는 점을 배웠다.

### 배운 개념

#### Custom Exception
Custom Exception은 직접 만든 예외 클래스다.

이번 과제에서는 Todo를 찾지 못한 상황을 명확히 표현하기 위해 `TodoNotFoundException`을 만들었다.

```java
public class TodoNotFoundException extends RuntimeException {
}
```

#### RuntimeException
`RuntimeException`을 상속하면 Service 메서드마다 `throws`를 붙이지 않아도 된다.

Spring 백엔드에서는 비즈니스 예외를 `RuntimeException` 기반으로 만들고, `@RestControllerAdvice`에서 HTTP 응답으로 변환하는 방식을 자주 사용한다.

#### orElseThrow
`orElseThrow`는 Optional 안에 값이 없을 때 예외를 던진다.

```java
.orElseThrow(() -> new TodoNotFoundException("Todo not found"))
```

흐름:

```txt
값 있음 -> 값 반환
값 없음 -> 예외 발생
```

#### for문에서 못 찾은 경우
for문으로 Todo를 찾는 경우, 찾았을 때는 바로 `return`한다.

끝까지 못 찾았다는 것은 해당 id의 Todo가 없다는 뜻이므로 for문 밖에서 예외를 던진다.

```txt
for문 안
-> 찾으면 처리 후 return

for문 밖
-> 끝까지 못 찾았으므로 throw
```

#### @RestControllerAdvice
`@RestControllerAdvice`는 여러 Controller에서 발생하는 예외를 한 곳에서 처리할 수 있게 해준다.

```java
@RestControllerAdvice
public class GlobalExceptionHandler {
}
```

#### @ExceptionHandler
`@ExceptionHandler`는 특정 예외가 발생했을 때 실행할 메서드를 지정한다.

```java
@ExceptionHandler(TodoNotFoundException.class)
protected ResponseEntity<Void> handleTodoNotFound() {
    return ResponseEntity.notFound().build();
}
```

### 전체 흐름

```txt
GET /todos/999 요청
-> Controller가 Service 호출
-> Service가 Todo를 찾지 못함
-> TodoNotFoundException 발생
-> GlobalExceptionHandler가 예외를 잡음
-> 404 Not Found 반환
```

```txt
PATCH /todos/999/complete 요청
-> Controller가 Service 호출
-> Service의 for문이 끝까지 Todo를 찾지 못함
-> TodoNotFoundException 발생
-> GlobalExceptionHandler가 404로 변환
```

### 테스트한 요청
- `GET /todos/999`
- `PATCH /todos/999/complete`
- `PATCH /todos/999`
- `POST /todos`
- `DELETE /todos/999`

### 테스트 결과
- 없는 Todo 조회 시 `404 Not Found`
- 없는 Todo 완료 처리 시 `404 Not Found`
- 없는 Todo 제목 수정 시 `404 Not Found`
- 정상 Todo 생성 성공
- 없는 Todo 삭제 시 기존 방식대로 `404 Not Found`

### 다음에 개선할 점
- 예외 메시지는 터미널에서 깨지지 않도록 영어 또는 ASCII로 작성하기
- `TodoNotFoundException` 생성자에서 id를 받아 메시지를 만들도록 개선하기
- 예외 응답 body가 필요해지면 `{ code, message }` 형태의 공통 에러 응답 DTO 만들기
- 반복되는 `Todo -> TodoResponse` 변환 코드를 다음 과제에서 정리하기

---

## 2026-07-31

### 오늘의 과제
응답 변환 메서드 정리하기

### 구현한 것
- `TodoResponse` record 안에 `from(Todo todo)` 정적 메서드를 추가했다.
- `TodoServiceImpl`에 반복되던 `new TodoResponse(...)` 코드를 제거했다.
- Todo 생성, 목록 조회, 단건 조회, 완료 처리, 제목 수정 응답에서 `TodoResponse.from(todo)`를 사용했다.
- 목록 조회에서는 `TodoResponse::from` 메서드 참조를 사용했다.
- 기존 API 동작은 유지하면서 변환 로직만 정리했다.

### 배운 개념

#### 정적 팩토리 메서드
정적 팩토리 메서드는 객체 생성을 의미 있는 이름의 메서드로 감싸는 방식이다.

```java
public static TodoResponse from(Todo todo) {
    return new TodoResponse(
        todo.id(),
        todo.title(),
        todo.completed()
    );
}
```

이번 과제에서는 `Todo`를 `TodoResponse`로 바꾸는 규칙을 `TodoResponse.from()` 안에 모았다.

#### DTO 변환 로직 모으기
기존에는 Service 여러 곳에서 아래 코드가 반복됐다.

```java
new TodoResponse(
    todo.id(),
    todo.title(),
    todo.completed()
)
```

이제는 아래처럼 짧게 쓸 수 있다.

```java
TodoResponse.from(todo)
```

응답 필드가 나중에 바뀌면 `TodoResponse.from()`만 수정하면 된다.

#### 메서드 참조
람다식이 단순히 특정 메서드를 호출하는 형태라면 메서드 참조로 줄일 수 있다.

```java
todos.stream()
    .map(TodoResponse::from)
    .toList();
```

이 코드는 각 Todo를 `TodoResponse.from(todo)`로 변환한다는 뜻이다.

### 전체 흐름

```txt
Todo 객체 생성 또는 조회
-> TodoResponse.from(todo) 호출
-> TodoResponse 반환
```

목록 조회 흐름:

```txt
List<Todo>
-> stream()
-> map(TodoResponse::from)
-> List<TodoResponse>
```

### 테스트한 내용
- `.\gradlew.bat test`
- 기존 API 컴파일 유지 확인

### 테스트 결과
- Gradle 테스트 성공
- `TodoResponse.from()` 적용 후에도 컴파일 성공
- 반복 변환 코드가 줄어듦

### 다음에 개선할 점
- 예외 메시지가 깨져 보이는 부분을 ASCII 메시지나 id 기반 메시지로 정리하기
- `TodoNotFoundException(long id)` 생성자를 추가해서 예외 메시지를 더 구체적으로 만들기
- 다음 단계부터 PostgreSQL과 JPA 연결 준비하기

---

## 2026-08-03

### 오늘의 과제
PostgreSQL Docker Compose 구성하기

### 구현한 것
- `docker-compose.yml` 파일을 만들었다.
- PostgreSQL 컨테이너 설정을 추가했다.
- `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD` 환경 변수를 설정했다.
- `build.gradle`에 JPA와 PostgreSQL 드라이버 의존성을 추가했다.
- `application.properties`에 datasource 설정을 추가했다.
- Spring Boot가 PostgreSQL에 연결되도록 설정했다.

### 막힌 부분
- 처음에는 PostgreSQL 환경 변수명을 `DATABASE`, `USER`, `PASSWORD`로 작성했다.
- PostgreSQL 공식 Docker 이미지가 인식하는 환경 변수명은 `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD`라는 점을 배웠다.
- DB 이름이 `ai-backend`와 `ai_backend`로 달라서 Spring datasource 설정과 맞지 않았다.
- DB 컨테이너가 떠 있지 않으면 JPA 초기화 중 Hibernate가 dialect를 판단하지 못하고 테스트가 실패했다.

### 배운 개념

#### Docker Compose
Docker Compose는 여러 컨테이너 설정을 파일로 관리하고 실행할 수 있게 해준다.

이번 과제에서는 PostgreSQL 컨테이너 하나를 실행하는 데 사용했다.

```yaml
services:
  db:
    image: postgres
    environment:
      POSTGRES_DB: ai_backend
      POSTGRES_USER: backend
      POSTGRES_PASSWORD: backend
    ports:
      - "5432:5432"
```

#### PostgreSQL 공식 이미지 환경 변수
PostgreSQL Docker 이미지는 아래 환경 변수를 사용한다.

```txt
POSTGRES_DB
POSTGRES_USER
POSTGRES_PASSWORD
```

잘못된 변수명을 쓰면 원하는 DB와 계정이 생성되지 않는다.

#### Spring datasource 설정
Spring Boot가 PostgreSQL에 연결하려면 datasource 설정이 필요하다.

```properties
spring.datasource.url=jdbc:postgresql://localhost:5432/ai_backend
spring.datasource.username=backend
spring.datasource.password=backend
```

`docker-compose.yml`의 DB 이름, 사용자명, 비밀번호와 `application.properties`의 설정이 일치해야 한다.

#### JPA와 PostgreSQL 의존성
JPA를 사용하려면 Spring Data JPA 의존성이 필요하다.

```gradle
implementation 'org.springframework.boot:spring-boot-starter-data-jpa'
```

PostgreSQL에 연결하려면 PostgreSQL JDBC 드라이버가 필요하다.

```gradle
runtimeOnly 'org.postgresql:postgresql'
```

#### Hibernate Dialect 오류
DB에 연결하지 못하면 Hibernate가 사용하는 SQL 방언을 판단하지 못해 아래와 같은 오류가 날 수 있다.

```txt
Unable to determine Dialect without JDBC metadata
```

이번 경우에는 PostgreSQL 컨테이너가 정상 실행된 뒤 테스트가 통과했다.

### 전체 흐름

```txt
docker compose up -d
-> PostgreSQL 컨테이너 실행
-> Spring Boot datasource 설정으로 DB 연결
-> JPA 초기화
-> 테스트와 서버 실행 성공
```

### 테스트한 명령
- `docker compose ps`
- `.\gradlew.bat test`
- `.\gradlew.bat bootRun`
- `GET /health`

### 테스트 결과
- PostgreSQL 컨테이너 `backend-db-1` 실행 확인
- 포트 `5432` 매핑 확인
- Gradle 테스트 성공
- Spring Boot 서버 실행 성공
- `/health` 응답에서 `status=UP` 확인

### 다음에 개선할 점
- Docker 이미지 버전을 `postgres:17`처럼 명시하기
- 컨테이너 데이터를 유지하려면 volume 설정 추가하기
- 다음 단계에서 Todo Entity와 Repository를 만들어 메모리 저장소를 DB 저장소로 전환하기

---

## 2026-08-04

### 오늘의 과제
Todo Entity와 Repository 만들기

### 구현한 것
- `TodoEntity` 클래스를 만들었다.
- `@Entity`, `@Id`, `@GeneratedValue`를 사용했다.
- `TodoRepository`를 만들고 `JpaRepository<TodoEntity, Long>`를 상속했다.
- `TodoServiceImpl`에 `TodoRepository`를 주입했다.
- `createTodo()`에서 `todoRepository.save(...)`를 사용해 Todo를 DB에 저장했다.
- `TodoResponse.from(TodoEntity)`를 만들어 Entity를 응답 DTO로 변환했다.
- `spring.jpa.hibernate.ddl-auto=update`로 설정해 테이블이 자동 생성되도록 했다.

### 막힌 부분
- 처음에는 `ddl-auto=validate` 상태라 테이블이 없으면 앱이 실패할 수 있었다.
- `POST /todos`만 DB 저장으로 바꾸고 나머지 API는 아직 메모리 기반/주석 상태로 남겨도 되는지 범위가 헷갈렸다.
- JPA Entity의 id 타입을 primitive `long`으로 둘지 wrapper `Long`으로 둘지 고민할 필요가 있었다.

### 배운 개념

#### @Entity
`@Entity`는 해당 클래스가 JPA가 관리하는 DB 테이블 매핑 객체임을 의미한다.

```java
@Entity
public class TodoEntity {
}
```

#### @Id
`@Id`는 Entity의 기본키 필드를 지정한다.

```java
@Id
private Long id;
```

#### @GeneratedValue
`@GeneratedValue`는 DB가 id 값을 자동 생성하도록 설정할 때 사용한다.

```java
@GeneratedValue(strategy = GenerationType.IDENTITY)
```

#### JpaRepository
`JpaRepository`를 상속하면 기본적인 DB 저장, 조회, 삭제 기능을 사용할 수 있다.

```java
public interface TodoRepository extends JpaRepository<TodoEntity, Long> {
}
```

#### save
`repository.save(entity)`는 Entity를 DB에 저장하고, 저장된 Entity를 반환한다.

```java
TodoEntity savedTodo = todoRepository.save(todo);
```

저장된 Entity에는 DB에서 생성된 id가 들어간다.

#### Entity와 Response 변환
DB에 저장하는 객체와 API 응답 객체는 역할이 다르다.

```txt
TodoEntity
-> DB 테이블과 매핑되는 객체

TodoResponse
-> 클라이언트에게 내려주는 응답 객체
```

그래서 `TodoResponse.from(TodoEntity)`로 변환했다.

### 전체 흐름

```txt
POST /todos 요청
-> TodoCreateRequest로 title 받기
-> TodoEntity 생성
-> todoRepository.save(todo)
-> DB에 row 저장
-> 저장된 TodoEntity를 TodoResponse로 변환
-> 200 OK 반환
```

### 테스트한 명령과 요청
- `docker compose ps`
- `.\gradlew.bat test`
- `.\gradlew.bat bootRun`
- `GET /health`
- `POST /todos`
- PostgreSQL에서 `select id, title, completed from todo` 조회

### 테스트 결과
- PostgreSQL 컨테이너 실행 확인
- Gradle 테스트 성공
- Spring Boot 서버 실행 성공
- `POST /todos` 응답 성공
- DB의 `todo` 테이블에 실제 row 저장 확인

### 다음에 개선할 점
- `TodoEntity.id`를 `long`보다 `Long`으로 바꾸기
- `TodoServiceImpl`에 남아 있는 사용하지 않는 `List<Todo>`, `AtomicLong` 제거하기
- 주석 처리된 이전 메모리 기반 코드를 정리하기
- 다음 과제에서 목록 조회와 단건 조회를 DB 기반으로 전환하기

---

## 2026-08-04

### 오늘의 과제
Todo 조회 API JPA 전환하기

### 구현한 것
- `GET /todos` 목록 조회 API를 DB 기반으로 전환했다.
- `GET /todos/{id}` 단건 조회 API를 DB 기반으로 전환했다.
- `todoRepository.findAll()`을 사용해서 Todo 목록을 조회했다.
- `todoRepository.findById(id)`를 사용해서 Todo 단건을 조회했다.
- 조회된 `TodoEntity`를 `TodoResponse`로 변환했다.
- 없는 id를 조회하면 `TodoNotFoundException`을 던지도록 유지했다.
- Controller 응답 구조는 기존과 동일하게 유지했다.

### 막힌 부분
- 메모리 기반 `List<Todo>`를 사용하던 흐름에서 Repository 조회 흐름으로 바꾸는 과정이 헷갈릴 수 있었다.
- 생성 API는 DB에 저장하고 조회 API도 DB에서 읽어야 데이터 흐름이 일관된다는 점을 확인했다.
- 목록 조회에서 직접 `new TodoResponse(...)`를 만들 수도 있지만, 이미 만든 `TodoResponse.from()`을 재사용하는 것이 더 깔끔하다는 점을 확인했다.

### 배운 개념

#### findAll
`findAll()`은 Repository가 관리하는 테이블의 모든 데이터를 조회한다.

```java
todoRepository.findAll()
```

반환된 Entity 목록은 API 응답으로 바로 내리지 않고 `TodoResponse`로 변환한다.

```java
todoRepository.findAll().stream()
    .map(TodoResponse::from)
    .toList();
```

#### findById
`findById(id)`는 id로 Entity 하나를 조회한다.

```java
todoRepository.findById(id)
```

결과는 값이 있을 수도 있고 없을 수도 있으므로 `Optional<TodoEntity>` 형태다.

```txt
값 있음 -> TodoEntity
값 없음 -> Optional.empty()
```

없는 id는 기존 예외 처리 흐름을 사용해서 `TodoNotFoundException`을 던진다.

```java
todoRepository.findById(id)
    .map(TodoResponse::from)
    .orElseThrow(() -> new TodoNotFoundException("Todo not found"));
```

#### DB 기반 조회 흐름
메모리 저장소를 사용할 때는 `List<Todo>`에서 직접 찾았다.

```txt
List<Todo>
-> stream/filter/findFirst
```

JPA 전환 후에는 Repository가 DB 조회를 담당한다.

```txt
TodoRepository
-> findAll()
-> findById(id)
```

### 전체 흐름

```txt
GET /todos 요청
-> Controller가 Service 호출
-> Service가 todoRepository.findAll() 호출
-> DB에서 TodoEntity 목록 조회
-> TodoResponse 목록으로 변환
-> 200 OK 반환
```

```txt
GET /todos/2 요청
-> Controller가 id 받기
-> Service가 todoRepository.findById(id) 호출
-> TodoEntity가 있으면 TodoResponse로 변환
-> 없으면 TodoNotFoundException 발생
-> GlobalExceptionHandler가 404 반환
```

### 테스트한 명령과 요청
- `docker compose ps`
- `.\gradlew.bat test`
- `.\gradlew.bat bootRun`
- `POST /todos`
- `GET /todos`
- `GET /todos/2`
- `GET /todos/999999`

### 테스트 결과
- PostgreSQL 컨테이너 실행 확인
- Gradle 테스트 성공
- Spring Boot 서버 실행 성공
- `POST /todos`로 Todo 생성 성공
- `GET /todos`에서 DB에 저장된 Todo 목록 조회 성공
- `GET /todos/2` 단건 조회 성공
- 없는 id 조회 시 `404 Not Found`

### 다음에 개선할 점
- 목록 조회에서도 `TodoResponse::from`을 사용해 변환 코드 통일하기
- `TodoEntity.id`를 `Long`으로 변경하기
- 다음 과제에서 완료 처리, 제목 수정, 삭제 API까지 DB 기반으로 전환하기
- 주석 처리된 메모리 기반 코드 정리하기

---

## 2026-08-04

### 오늘의 과제
Todo 수정/삭제 API JPA 전환하기

### 구현한 것
- `PATCH /todos/{id}/complete` 완료 처리 API를 DB 기반으로 전환했다.
- `PATCH /todos/{id}` 제목 수정 API를 DB 기반으로 전환했다.
- `DELETE /todos/{id}` 삭제 API를 DB 기반으로 전환했다.
- `TodoEntity.id` 타입을 `Long`으로 변경했다.
- `TodoEntity`에 상태 변경 메서드를 추가했다.
- `completeTodo`, `updateTitle`에 `@Transactional`을 적용했다.
- 삭제 시 `findById`로 존재 여부를 확인한 뒤 `deleteById`를 호출했다.
- 없는 id 요청은 기존 `TodoNotFoundException` 흐름으로 `404 Not Found`를 반환하게 했다.

### 막힌 부분
- 처음에는 Entity의 필드 값을 바꿨지만 DB에 반영되지 않았다.
- JPA 변경 감지는 트랜잭션 안에서 동작한다는 점을 확인했다.
- 응답에서는 값이 바뀐 것처럼 보여도, 다시 조회했을 때 DB에 반영되지 않을 수 있다는 점을 배웠다.

### 배운 개념

#### Entity 상태 변경 메서드
Entity 내부 상태를 바꿀 때 setter를 무작정 열기보다 의미 있는 메서드를 만들 수 있다.

```java
public void updateCompleted(boolean completed) {
    this.completed = completed;
}

public void updateTitle(String title) {
    if (title != null) {
        this.title = title;
    }
}
```

이렇게 하면 외부 코드가 어떤 의도로 Entity를 변경하는지 더 잘 드러난다.

#### @Transactional
`@Transactional`은 메서드 실행을 하나의 트랜잭션으로 묶는다.

JPA에서 DB에서 조회한 Entity는 트랜잭션 안에서 관리 상태가 된다. 관리 상태의 Entity 값을 변경하면, 트랜잭션이 끝날 때 JPA가 변경 사항을 감지해서 DB에 반영한다.

```java
@Transactional
public TodoResponse completeTodo(long id) {
    TodoEntity todo = todoRepository.findById(id)
        .orElseThrow(...);

    todo.updateCompleted(true);

    return TodoResponse.from(todo);
}
```

#### 변경 감지
변경 감지는 JPA가 관리 중인 Entity의 필드 변경을 감지해서 자동으로 update SQL을 실행하는 기능이다.

```txt
findById로 Entity 조회
-> Entity 값 변경
-> 트랜잭션 종료
-> JPA가 변경 감지
-> DB update
```

#### 삭제 흐름
삭제는 먼저 id에 해당하는 Todo가 있는지 확인하고, 있으면 삭제했다.

```txt
findById(id)
-> 없으면 TodoNotFoundException
-> 있으면 deleteById(id)
-> Controller에서 204 No Content 반환
```

### 전체 흐름

```txt
PATCH /todos/4/complete
-> Controller가 Service 호출
-> Service가 DB에서 TodoEntity 조회
-> 없으면 TodoNotFoundException
-> 있으면 completed=true로 변경
-> 트랜잭션 종료 시 DB 반영
-> TodoResponse 반환
```

```txt
PATCH /todos/4
-> Controller가 Service 호출
-> Service가 DB에서 TodoEntity 조회
-> title 변경
-> 트랜잭션 종료 시 DB 반영
-> TodoResponse 반환
```

```txt
DELETE /todos/4
-> Controller가 Service 호출
-> Service가 DB에서 TodoEntity 존재 확인
-> deleteById 호출
-> 204 No Content 반환
```

### 테스트한 명령과 요청
- `docker compose ps`
- `.\gradlew.bat test`
- `.\gradlew.bat bootRun`
- `POST /todos`
- `PATCH /todos/4/complete`
- `GET /todos/4`
- `PATCH /todos/4`
- `PATCH /todos/999999/complete`
- `PATCH /todos/999999`
- `DELETE /todos/4`
- `GET /todos/4`

### 테스트 결과
- Gradle 테스트 성공
- 완료 처리 후 재조회 시 `completed=true` 유지
- 제목 수정 후 재조회 시 변경된 title 유지
- 없는 id 완료 처리 시 `404 Not Found`
- 없는 id 제목 수정 시 `404 Not Found`
- 삭제 성공 시 `204 No Content`
- 삭제 후 조회 시 `404 Not Found`

### 다음에 개선할 점
- `getTodoList()`도 `TodoResponse::from`으로 변환 코드 통일하기
- `jakarta.transaction.Transactional` 대신 Spring의 `org.springframework.transaction.annotation.Transactional` 사용을 고려하기
- `TodoNotFoundException(long id)` 생성자로 예외 메시지 정리하기
- 다음 단계에서 Controller 테스트를 작성해 수동 확인을 자동화하기
- 

---

## 2026-08-05

### 오늘의 과제
Controller 테스트 작성하기

### 구현한 것
- `TodoControllerTest`를 만들었다.
- 테스트 파일을 `todo` 패키지 아래로 이동했다.
- `@SpringBootTest`를 사용했다.
- `@AutoConfigureMockMvc`를 사용해 `MockMvc`를 주입받았다.
- `POST /todos` 생성 API 테스트를 작성했다.
- 생성 응답의 `title`, `completed` 값을 `jsonPath`로 검증했다.
- `GET /todos` 목록 조회 테스트를 작성했다.
- 목록 응답이 JSON 배열인지 검증했다.
- `GET /todos/{id}` 단건 조회 테스트를 작성했다.
- 없는 id 조회 시 `404 Not Found`를 검증했다.

### 막힌 부분
- `AutoConfigureMockMvc` import를 찾지 못했다.
- Spring Boot 4에서는 기존 자료의 import 경로와 다르다는 점을 확인했다.
- `spring-boot-starter-test`만으로는 MockMvc 자동 설정 모듈이 잡히지 않았다.
- `spring-boot-starter-webmvc-test` 의존성을 추가해야 했다.
- `POST /todos` 테스트에서 요청 body와 기대 title 값이 달라 실패할 수 있었다.
- `GET /todos/{id}`에서 path variable 작성법이 헷갈렸다.

### 배운 개념

#### MockMvc
`MockMvc`는 실제 서버를 띄우지 않고 Controller에 HTTP 요청을 보내는 것처럼 테스트할 수 있게 해준다.

```java
mockMvc.perform(MockMvcRequestBuilders.post("/todos"))
```

#### @AutoConfigureMockMvc
`@AutoConfigureMockMvc`는 테스트에서 `MockMvc`를 사용할 수 있게 자동 설정해준다.

Spring Boot 4 기준 import는 아래와 같다.

```java
import org.springframework.boot.webmvc.test.autoconfigure.AutoConfigureMockMvc;
```

#### Spring Boot 4 테스트 의존성
Spring Boot 4에서는 MockMvc 테스트를 위해 아래 의존성이 필요했다.

```gradle
testImplementation 'org.springframework.boot:spring-boot-starter-webmvc-test'
```

#### JSON 요청 body
`POST /todos`는 JSON body가 필요하므로 테스트에서도 `contentType`과 `content`를 넣어야 한다.

```java
MockMvcRequestBuilders.post("/todos")
    .contentType("application/json")
    .content("{\"title\":\"Spring study\"}")
```

#### jsonPath
`jsonPath`는 응답 JSON의 특정 필드를 검증한다.

```java
.andExpect(jsonPath("$.title").value("Spring study"))
.andExpect(jsonPath("$.completed").value(false))
```

단건 응답은 객체라서 `$.title`을 사용하고, 목록 응답은 배열이라서 `$[0].title` 같은 형태를 사용할 수 있다.

#### PathVariable 테스트
PathVariable은 아래처럼 값을 넘길 수 있다.

```java
MockMvcRequestBuilders.get("/todos/{id}", 1)
```

### 테스트한 명령
- `docker compose ps`
- `./gradlew.bat test`

### 테스트 결과
- PostgreSQL 컨테이너 실행 확인
- Gradle 테스트 성공
- 생성 API 테스트 성공
- 목록 조회 테스트 성공
- 단건 조회 테스트 성공
- 없는 id 조회 테스트 성공

### 다음에 개선할 점
- `getTodo_success()`가 DB에 id 1이 있다고 가정하므로, 테스트 안에서 Todo를 생성하고 그 id로 조회하도록 개선하기
- 테스트마다 DB 상태가 서로 영향을 주지 않도록 정리하기
- 다음 단계에서 Service 테스트를 작성해 비즈니스 로직을 직접 검증하기
