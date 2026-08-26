# Week 03 - PostgreSQL, JPA, 테스트

## Day 15. PostgreSQL 연결하기

### 목표

Docker Compose로 PostgreSQL을 실행하고 Spring Boot와 연결합니다.

### 요구사항

- `docker-compose.yml`에 PostgreSQL 서비스를 만든다.
- `application.properties`에 datasource 설정을 추가한다.
- 서버 실행 시 DB 연결 에러가 없어야 한다.

### 완료 기준

- PostgreSQL 컨테이너가 실행된다.
- Spring Boot가 DB에 연결된다.

### 회고 질문

- datasource url, username, password는 각각 무엇인가?
- Docker Compose를 쓰면 무엇이 편해지는가?

## Day 16. TodoEntity와 TodoRepository 만들기

### 목표

JPA Entity와 Repository의 기본 구조를 익힙니다.

### 요구사항

- `TodoEntity`를 만든다.
- 필드는 `id`, `title`, `completed`를 가진다.
- `TodoRepository extends JpaRepository<TodoEntity, Long>`를 만든다.

### 완료 기준

- Entity에 `@Entity`, id에 `@Id`가 붙어 있다.
- Repository가 Spring Bean으로 등록된다.

### 회고 질문

- Entity는 DB 테이블과 어떤 관계인가?
- JpaRepository를 상속하면 어떤 메서드를 바로 쓸 수 있는가?

## Day 17. DB 기반 Todo 생성/목록 조회

### 목표

메모리 List 대신 Repository를 사용합니다.

### 요구사항

- Todo 생성 시 `todoRepository.save(...)`를 사용한다.
- 목록 조회 시 `todoRepository.findAll()`을 사용한다.
- 응답은 `TodoResponse`로 변환한다.

### 완료 기준

- 서버를 재시작해도 DB에 저장된 데이터가 남아 있다.
- 생성 후 목록 조회에서 DB 데이터가 보인다.

### 회고 질문

- save와 findAll은 어디서 제공되는가?
- Entity를 그대로 응답하지 않는 이유는 무엇인가?

## Day 18. Controller 테스트 작성

### 목표

MockMvc로 API 요청/응답을 테스트합니다.

### 요구사항

- `POST /todos` 생성 테스트를 작성한다.
- `GET /todos` 목록 조회 테스트를 작성한다.
- `GET /todos/{id}` 단건 조회 테스트를 작성한다.
- 없는 id 조회 시 404 테스트를 작성한다.

### 완료 기준

- `@SpringBootTest`와 `@AutoConfigureMockMvc`를 사용한다.
- `jsonPath`로 응답 body를 검증한다.

### 회고 질문

- Controller 테스트는 무엇을 검증하는가?
- `jsonPath("$.title")`은 응답의 어느 값을 보는가?

## Day 19. Service 테스트 작성

### 목표

Service 로직을 직접 호출해서 검증합니다.

### 요구사항

- `TodoServiceTest`를 만든다.
- `@SpringBootTest`를 사용한다.
- `TodoService`, `TodoRepository`를 `@Autowired`로 주입한다.
- `@BeforeEach`에서 `todoRepository.deleteAll()`을 호출한다.
- 생성, 목록 조회, 단건 조회, 없는 id 조회 테스트를 작성한다.

### 완료 기준

- MockMvc를 사용하지 않는다.
- 테스트마다 필요한 Todo를 직접 만든다.
- 없는 id는 `TodoNotFoundException` 발생을 검증한다.

### 회고 질문

- Controller 테스트와 Service 테스트는 무엇이 다른가?
- 테스트에서 id를 1L로 고정하면 왜 위험한가?

## Day 20. Update/Delete Service 테스트 추가

### 목표

수정, 완료 처리, 삭제 로직까지 테스트합니다.

### 요구사항

- `completeTodo` 성공 테스트를 작성한다.
- `updateTitle` 성공 테스트를 작성한다.
- `deleteTodo` 성공 테스트를 작성한다.
- 없는 id로 수정/삭제 시 예외 테스트를 작성한다.

### 완료 기준

- 변경 후 다시 조회했을 때 값이 유지된다.
- 삭제 후 다시 조회하면 예외가 발생한다.

### 회고 질문

- 변경 테스트에서 왜 다시 조회해보는 것이 좋은가?
- 삭제 성공 응답은 body가 꼭 필요할까?

## Day 21. Transaction과 변경 감지 이해하기

### 목표

JPA에서 Entity 값을 바꾸면 DB에 반영되는 흐름을 이해합니다.

### 요구사항

- `completeTodo`, `updateTitle`에 `@Transactional`이 필요한 이유를 정리한다.
- 수정 메서드에서 `save`를 호출하지 않아도 반영되는지 확인한다.
- 변경 감지 테스트를 작성한다.

### 완료 기준

- 트랜잭션 안에서 Entity 변경이 DB에 반영된다.
- 테스트로 변경 전/후 값을 확인한다.

### 회고 질문

- 영속성 컨텍스트는 어떤 역할을 하는가?
- 변경 감지는 언제 동작하는가?
