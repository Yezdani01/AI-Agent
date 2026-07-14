# Personal Assistant with Conversational Memory & Tool Integration

A lightweight, production-ready conversational AI agent built using the **Agentspan** framework and **OpenAI's GPT-4o-Mini**. This project showcases an implementation of an AI assistant capable of maintaining context across multiple conversation turns using local persistent memory, integrating custom tools (like fetching the local time), and offering full visibility via the Agentspan visual execution dashboard.

---

## 🚀 Key Features

* **Conversational Memory:** Retains context and user details (such as names and past inputs) up to 50 message turns across a session, breaking away from stateless agent architectures.
* **Tool Integration:** Demonstrates extensibility by exposing a custom Python function (`get_current_time`) to the agent for dynamic real-time lookups.
* **Server-Worker Architecture:** Powered by a local Agentspan server orchestration backend (running SQLite with WAL mode), making it robust and structurally ready for production scaling.
* **Streamlined Logging:** Configured with specific logging levels (`WARNING`) to filter out internal system noise while preserving essential debugging and tracing data.
* **Visual Dashboard Monitoring:** Real-time visibility into agent execution, prompts, token counts, and tool calls using the Agentspan Web UI.

---

## 📋 System Prerequisites & Architecture

This project is fully optimized and managed using **`uv`**, the ultra-fast Python package installer and resolver.
---

## 🛠️ Step-by-Step Setup Guide

### Step 1 — Project Initialization & Dependencies

Ensure you have `uv` installed. If not, install it via curl or your package manager. Then, install the required packages:



```bash
# Install the core Agentspan SDK and support tools using uv
uv pip install conductor-agent-sdk python-dotenv

# Alternatively, if you are initializing it as a managed project:
uv add conductor-agent-sdk python-dotenv

# Verify that the CLI tool environment is properly initialized:
uv run agentspan doctor
```


### Step 2 — Environment & API Configuration
Create a .env file in the root directory of your project to connect the worker code to the Agentspan orchestrator:
```bash
# Define the local server runtime endpoint
AGENTSPAN_SERVER_URL=http://localhost:6767/api
# Export your OpenAI API Key into your active terminal shell environment:
# For Linux/macOS
export OPENAI_API_KEY="sk-proj-YOUR-ACTUAL-OPENAI-KEY-HERE"

# For Windows PowerShell
$env:OPENAI_API_KEY="sk-proj-YOUR-ACTUAL-OPENAI-KEY-HERE"
```
### Step 3 — Boot the Agentspan Server
Before launching the agent script, start the underlying Agentspan local runtime engine. On its first execution, it will download a ~50MB JAR file and run a fast SQLite instance locally:
```bash
uv run agentspan server start
```
### Local Web UI: Open http://localhost:6767 in your browser to view the real-time visual execution stream dashboard.

### Codebase Structure (agent1.py)