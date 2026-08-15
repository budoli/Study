package dev.jpa.backend.todo;

public record TodoResponse(
	long id,
	String title,
	boolean completed
) {
	public static TodoResponse from(TodoEntity todo) {
		return new TodoResponse(
			todo.getId(),
			todo.getTitle(),
			todo.isCompleted()
		);
	}
}
