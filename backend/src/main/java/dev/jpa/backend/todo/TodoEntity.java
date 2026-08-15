package dev.jpa.backend.todo;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

@Entity
@Getter
@Builder
@NoArgsConstructor
@AllArgsConstructor
@Table(name = "todo")
public class TodoEntity {
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private Long id;

	private String title;

	private boolean completed;

	public static TodoEntity createTodo(
		String title,
		boolean completed
	) {
		return TodoEntity.builder()
			.title(title)
			.completed(completed)
			.build();
	}

	public void updateCompleted(
		boolean completed
	) {
		this.completed = completed;
	}

	public void updateTitle(
		String title
	) {
		if (title != null) {
			this.title = title;
		}
	}
}
