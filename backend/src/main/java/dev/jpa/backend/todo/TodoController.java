package dev.jpa.backend.todo;

import java.util.List;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PatchMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import jakarta.validation.Valid;
import lombok.RequiredArgsConstructor;

@RestController
@RequiredArgsConstructor
@RequestMapping("/todos")
public class TodoController {
	private final TodoService todoService;

	@PostMapping
	public ResponseEntity<TodoResponse> createTodo(
		@Valid @RequestBody TodoCreateRequest request
	) {

		return ResponseEntity.ok(todoService.createTodo(request));
	}

	@GetMapping
	public ResponseEntity<List<TodoResponse>> getTodoList() {

		return ResponseEntity.ok(todoService.getTodoList());
	}

	@GetMapping("/{id}")
	public ResponseEntity<TodoResponse> getTodo(
		@PathVariable long id
	) {

		return ResponseEntity.ok(todoService.getTodo(id));
	}

	@DeleteMapping("/{id}")
	public ResponseEntity<Void> deleteTodo(
		@PathVariable long id
	) {
		todoService.deleteTodo(id);
		return ResponseEntity.noContent().build();
	}

	@PatchMapping("/{id}/complete")
	public ResponseEntity<TodoResponse> completeTodo(
		@PathVariable long id
	) {
		return ResponseEntity.ok(todoService.completeTodo(id));
	}

	@PatchMapping("/{id}")
	public ResponseEntity<TodoResponse> updateTitle(
		@PathVariable long id,
		@Valid @RequestBody TodoUpdateRequest updateRequest
	) {
		return ResponseEntity.ok(todoService.updateTitle(id, updateRequest));

	}
}

