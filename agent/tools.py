def calculate(a: float, b: float, operation: str) -> float:
    if operation in ["add", "+"]:
        return a + b

    if operation in ["subtract", "-"]:
        return a - b

    if operation in ["multiply", "*", "×"]:
        return a * b

    if operation in ["divide", "/"]:
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    raise ValueError("Unknown operation")