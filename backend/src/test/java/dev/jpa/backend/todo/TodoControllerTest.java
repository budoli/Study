package dev.jpa.backend.todo;

import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.webmvc.test.autoconfigure.AutoConfigureMockMvc;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.test.web.servlet.request.MockMvcRequestBuilders;

@SpringBootTest
@AutoConfigureMockMvc
public class TodoControllerTest {

	@Autowired
	private MockMvc mockMvc;

	@Test
	void createTodo_success() throws Exception{
		mockMvc.perform(
			MockMvcRequestBuilders.post("/todos")
				.contentType("application/json")
				.content("{\"title\":\"Spring study\"}"))
			.andExpect(status().isOk())
			.andExpect(jsonPath("$.title").value("Spring study"))
			.andExpect(jsonPath("$.completed").value(false));
	}

	@Test
	void getTodoList_success() throws Exception {
		mockMvc.perform(
				MockMvcRequestBuilders.get("/todos"))
			.andExpect(status().isOk())
			.andExpect(jsonPath("$").isArray());

	}

	@Test
	void getTodo_success() throws Exception{
		mockMvc.perform(
			MockMvcRequestBuilders.get("/todos/{id}",1))
			.andExpect(status().isOk());
	}

	@Test
	void getTodo_notFound() throws Exception{
		mockMvc.perform(
				MockMvcRequestBuilders.get("/todos/{id}",9999))
			.andExpect(status().isNotFound());
	}

}
