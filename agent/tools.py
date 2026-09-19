def calculate(a: float, b: float, operation: str) -> float:
    operation = operation.lower().strip()

    if operation in ["add", "+", "addition"]:
        return a + b

    if operation in ["subtract", "-", "subtraction"]:
        return a - b

    if operation in ["multiply", "*", "×", "multiplication", "multiply numbers"]:
        return a * b

    if operation in ["divide", "/", "division"]:
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    raise ValueError(f"Unknown operation: {operation}")