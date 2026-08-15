package dev.jpa.backend.hello;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/hello")
public class HelloController {

	@GetMapping
	public ResponseEntity<HelloResponse> getHello(
		@RequestParam String name
	) {
		HelloResponse hr = new HelloResponse("Hello, " + name);
		return ResponseEntity.ok(hr);
	}
}
