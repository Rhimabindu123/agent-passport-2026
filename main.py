import asyncio

from agent.passport.passport_loader import load_passport
from agent.contract import verify_passport
from agent.runner import create_agent_from_passport


async def main():
    passport = load_passport()

    verify_passport(passport)

    print("Passport verification: PASSED")
    print(f"Agent: {passport['name']}")
    print(f"Adapter: {passport['runtime']['adapter']}")

    question = "Calculate 125 multiplied by 8 using the calculator tool."

    result = await create_agent_from_passport(passport).run(question)

    final_message = result.messages[-1]

    print(f"Question: {question}")
    print(f"Result: {final_message.content}")


if __name__ == "__main__":
    asyncio.run(main())