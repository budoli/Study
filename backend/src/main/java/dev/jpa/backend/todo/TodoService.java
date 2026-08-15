package dev.jpa.backend.todo;

import java.util.List;

public interface TodoService {
	TodoResponse createTodo(TodoCreateRequest request);
	List<TodoResponse> getTodoList();
	TodoResponse getTodo(long id);
	void deleteTodo(long id);
	TodoResponse completeTodo(long id);
	TodoResponse updateTitle(long id, TodoUpdateRequest request);
}
