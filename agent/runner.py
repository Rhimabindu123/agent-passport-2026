from agent.autogen_adapter import AutoGenAdapter


def create_agent_from_passport(passport):
    adapter_name = passport["runtime"]["adapter"]

    if adapter_name == "AutoGenAdapter":
        return AutoGenAdapter()

    raise ValueError(f"Unsupported adapter: {adapter_name}")