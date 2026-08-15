package dev.jpa.backend.calculator;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/calculator")
public class CalculatorController {
	@GetMapping("/add")
	public ResponseEntity<CalculatorResponse> add(
		@RequestParam int a,
		@RequestParam int b
	) {
		CalculatorResponse cr = new CalculatorResponse(a + b);
		return ResponseEntity.ok(cr);
	}
}
