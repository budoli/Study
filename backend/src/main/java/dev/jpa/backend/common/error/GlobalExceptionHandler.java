package dev.jpa.backend.common.error;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;

import dev.jpa.backend.todo.TodoNotFoundException;

@RestControllerAdvice
public class GlobalExceptionHandler {

	@ExceptionHandler(TodoNotFoundException.class)
	protected ResponseEntity<Void> handleTodoNotFound (
	) {
		return ResponseEntity.notFound().build();
	}
}
