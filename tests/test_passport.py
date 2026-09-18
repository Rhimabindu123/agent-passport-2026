from agent.runner import create_agent_from_passport
import inspect
from agent.passport.passport_loader import load_passport
from agent.tools import calculate
from agent.contract import verify_passport
from agent.interface import PortableAgent
from agent.autogen_adapter import AutoGenAdapter

def test_passport_has_required_fields():
    passport = load_passport()

    assert "name" in passport
    assert "version" in passport
    assert "input" in passport
    assert "output" in passport
    assert "capabilities" in passport
    assert "tools" in passport
    assert "behavior" in passport
    assert "runtime" in passport
    assert "interface" in passport
    assert passport["interface"]["name"] == "PortableAgent"
    assert passport["interface"]["method"] == "run(question)"


def test_calculator_tool():
    result = calculate(125, 8, "multiply")

    assert result == 1000
def test_passport_matches_contract():
    passport = load_passport()

    assert verify_passport(passport) is True
   


def test_portable_agent_interface():
    agent = PortableAgent("test_agent")

    assert agent.name == "test_agent"
def test_autogen_adapter():
    agent = AutoGenAdapter()

    assert isinstance(agent, PortableAgent)
    assert agent.name == "research_agent"
    assert agent.agent is not None
def test_autogen_adapter_run_method():
    agent = AutoGenAdapter()

    assert hasattr(agent, "run")
    assert inspect.iscoroutinefunction(agent.run)
def test_runner_creates_agent_from_passport():
    passport = load_passport()

    agent = create_agent_from_passport(passport)

    assert isinstance(agent, AutoGenAdapter)
    assert agent.name == "research_agent"