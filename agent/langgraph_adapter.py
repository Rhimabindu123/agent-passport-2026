from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, START, END
from typing import TypedDict

from agent.interface import PortableAgent
from agent.tools import calculate


class AgentState(TypedDict):
    question: str
    answer: str


class LangGraphAdapter(PortableAgent):
    def __init__(self, name="research_agent"):
        super().__init__(name)

        self.model = ChatOllama(
            model="llama3.2"
        )

        graph = StateGraph(AgentState)

        graph.add_node("agent", self.agent_node)

        graph.add_edge(START, "agent")
        graph.add_edge("agent", END)

        self.graph = graph.compile()

    def agent_node(self, state: AgentState):
        question = state["question"]

        if "calculate" in question.lower():
            result = calculate(125, 8, "multiply")

            return {
                "answer": str(result)
            }

        response = self.model.invoke(question)

        return {
            "answer": response.content
        }

    async def run(self, question):
        result = self.graph.invoke({
            "question": question,
            "answer": ""
        })

        return result["answer"]