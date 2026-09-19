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

    supported_adapters = passport["runtime"]["supported_adapters"]

    assert "AutoGenAdapter" in supported_adapters
    assert "LangGraphAdapter" in supported_adapters

    assert passport["runtime"]["default_adapter"] in supported_adapters

    return True