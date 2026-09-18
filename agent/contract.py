INPUT_TYPE = "text"
OUTPUT_TYPE = "text"

REQUIRED_BEHAVIOR = [
    "Answer questions clearly",
    "Use the calculator tool when calculations are required"
]


def verify_passport(passport):
    assert passport["input"]["type"] == INPUT_TYPE
    assert passport["output"]["type"] == OUTPUT_TYPE

    for behavior in REQUIRED_BEHAVIOR:
        assert behavior in passport["behavior"]

    assert "calculate" in passport["tools"]
    assert passport["runtime"]["adapter"] == "AutoGenAdapter"

    return True