from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.ollama import OllamaChatCompletionClient

from agent.interface import PortableAgent
from agent.tools import calculate


class AutoGenAdapter(PortableAgent):
    def __init__(self, name="research_agent"):
        super().__init__(name)

        self.model_client = OllamaChatCompletionClient(
            model="llama3.2"
        )

        self.agent = AssistantAgent(
            name=self.name,
            model_client=self.model_client,
            tools=[calculate],
            system_message=(
                "You are a helpful research assistant. "
                "Give clear and simple answers."
            ),
        )

    async def run(self, question):
        result = await self.agent.run(task=question)
        return result