import asyncio

from agent.passport.passport_loader import load_passport
from agent.contract import verify_passport
from agent.runner import create_agent_from_passport


async def run_agent(passport, adapter_name, question):
    agent = create_agent_from_passport(
        passport,
        adapter_name=adapter_name
    )

    result = await agent.run(question)

    if adapter_name == "AutoGenAdapter":
        return result.messages[-1].content

    return result


async def main():
    passport = load_passport()

    verify_passport(passport)

    print("====================================")
    print("       AGENT PASSPORT DEMO")
    print("====================================")

    print("Passport verification: PASSED")
    print(f"Agent: {passport['name']}")

    print("\nSupported adapters:")
    for adapter in passport["runtime"]["supported_adapters"]:
        print(f"- {adapter}")

    question = "Calculate 125 multiplied by 8 using the calculator tool."

    for adapter_name in passport["runtime"]["supported_adapters"]:
        print("\n------------------------------------")
        print(f"Running with: {adapter_name}")
        print("------------------------------------")

        try:
            result = await run_agent(
                passport,
                adapter_name,
                question
            )

            print(f"Question: {question}")
            print(f"Result: {result}")

        except Exception as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    asyncio.run(main())