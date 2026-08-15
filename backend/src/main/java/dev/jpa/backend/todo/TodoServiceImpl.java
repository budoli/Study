package dev.jpa.backend.todo;

import java.util.List;

import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import lombok.RequiredArgsConstructor;

@Service
@RequiredArgsConstructor
public class TodoServiceImpl implements TodoService {
	private final TodoRepository todoRepository;

	@Override
	public TodoResponse createTodo(TodoCreateRequest request) {
		String title = request.title();

		TodoEntity todo =  TodoEntity.createTodo(
			title,
			false);

		return TodoResponse.from(todoRepository.save(todo));
	}

	@Override
	public List<TodoResponse> getTodoList() {
		return todoRepository.findAll().stream()
			.map(TodoResponse::from)
			.toList();

	}

	@Override
	public TodoResponse getTodo(long id) {

		return todoRepository.findById(id)
			.map(TodoResponse::from)
			.orElseThrow(() -> new TodoNotFoundException("찾을 수 없습니다."));


	}

	@Override
	public void deleteTodo(long id) {

		todoRepository.findById(id)
			.orElseThrow(() -> new TodoNotFoundException("찾을 수없다."));

		todoRepository.deleteById(id);
	}

	@Override
	@Transactional
	public TodoResponse completeTodo(long id) {
		TodoEntity todo = todoRepository.findById(id)
			.orElseThrow(() -> new TodoNotFoundException("찾을 수 없습니다."));

		todo.updateCompleted(true);

		return TodoResponse.from(todo);
	}

	@Override
	@Transactional
	public TodoResponse updateTitle(long id, TodoUpdateRequest request) {
		TodoEntity todo = todoRepository.findById(id)
			.orElseThrow(() -> new TodoNotFoundException("찾을 수 없습니다."));

		todo.updateTitle(request.title());

		return TodoResponse.from(todo);
	}
}
