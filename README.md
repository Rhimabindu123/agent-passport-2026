# Agent Passport

A portable AI research assistant built using AutoGen and Ollama.

## Project Overview

Agent Passport is designed around a portable agent contract.

The agent's identity, capabilities, tools, behavior, interface, and runtime
configuration are described in a `passport.json` file.

The project uses an adapter architecture so that the same portable interface
can be connected to different agent frameworks in the future.

## Architecture

```text
passport.json
      |
      v
Passport Loader
      |
      v
Passport Verification
      |
      v
Runner
      |
      v
AutoGen Adapter
      |
      v
AutoGen AssistantAgent
      |
      v
Ollama / Llama 3.2
      |
      v
Calculator Tool
      |
      v
Agent Result