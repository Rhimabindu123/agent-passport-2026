d# Agent Passport – Portable AI Agent Framework

## Overview

Agent Passport is a modular and verifiable AI agent framework designed to make an AI agent easier to describe, validate, and execute across different agent runtimes.

The project uses a JSON-based Agent Passport to define the agent's identity, capabilities, behavior, tools, interface, and supported runtimes.

The same passport-defined agent can currently be executed through two runtime adapters:

- AutoGen
- LangGraph

Both runtimes use Llama 3.2 through Ollama.

---

## Problem

AI agents are often tightly connected to the framework in which they are developed.

For example, an agent built using one framework may require significant changes before it can be executed using another framework.

This project separates the agent's common contract from its runtime implementation.

The main idea is:

> Passport tells us WHAT the agent is, while the Adapter tells us HOW the agent runs.

---

## Solution

The project introduces three important layers:

1. Agent Passport – describes the agent.
2. PortableAgent Interface – defines a common way to run the agent.
3. Runtime Adapters – connect the common interface to different agent frameworks.

Current runtime adapters:

- AutoGenAdapter
- LangGraphAdapter

This allows the same passport-defined agent to be executed using different runtime frameworks.

---

## Architecture

```text
                    Agent Passport
                         |
                         v
                Passport Verification
                         |
                         v
                  PortableAgent
                         |
              +----------+----------+
              |                     |
              v                     v
       AutoGenAdapter       LangGraphAdapter
              |                     |
              v                     v
           AutoGen              LangGraph
              |                     |
              +----------+----------+
                         |
                         v
                       Ollama
                         |
                         v
                    Llama 3.2
                         |
                         v
                  Calculator Tool