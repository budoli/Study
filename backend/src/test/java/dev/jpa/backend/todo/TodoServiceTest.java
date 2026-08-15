package dev.jpa.backend.todo;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
public class TodoServiceTest {
	@Autowired
	private TodoService todoService;
	@Autowired
	private TodoRepository todoRepository;

	@Test
	void createTodo() {
		todoService.createTodo();
	}

	@Test
	void getTodo() {
		todoService.getTodo();
	}

	@Test
	void getTodoList() {
		todoService.getTodoList();
	}

	@Test
	void completeTodo() {
		todoService.completeTodo();
	}

	@Test
	void updateTitle() {
		todoService.updateTitle();
	}

	@Test
	void deleteTodo() {
		todoService.deleteTodo();
	}

}
