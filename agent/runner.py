from agent.autogen_adapter import AutoGenAdapter
from agent.langgraph_adapter import LangGraphAdapter


def create_agent_from_passport(passport, adapter_name=None):
    if adapter_name is None:
        adapter_name = passport["runtime"]["default_adapter"]

    supported_adapters = passport["runtime"]["supported_adapters"]

    if adapter_name not in supported_adapters:
        raise ValueError(
            f"Unsupported adapter: {adapter_name}"
        )

    if adapter_name == "AutoGenAdapter":
        return AutoGenAdapter()

    if adapter_name == "LangGraphAdapter":
        return LangGraphAdapter()

    raise ValueError(
        f"Adapter is listed but not implemented: {adapter_name}"
    )