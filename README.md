---
title: BIBLE_AGENT
app_file: app.py
sdk: gradio
sdk_version: 5.31.0
---
# BibleAgent Crew

Bible Agent is an AI-powered application designed to provide multi-layered biblical insights by leveraging multiple specialized agents. Built using CrewAI and deployed with Gradio on Hugging Face Spaces, it offers users rich responses to biblical queries with context, commentary, and pastoral wisdom.

## Architecture
The system utilizes three main agents:

- Bible Agent: Fetches relevant Bible verses.

- Theological Scholar Agent: Searches for expert commentary and uses web search tools for deeper research.

- Seasoned Pastor Agent: Synthesizes the results and delivers a spiritually insightful summary.

## Workflow
1. User Input: The user asks a question (e.g., “What does the Bible say about love?”).

2. Bible Agent: Retrieves relevant verses from different Bible versions.

3. Theological Scholar Agent: Gathers expert commentaries using web tools.

4. Seasoned Pastor Agent: Integrates scripture and scholarship into a concise, practical response.

## Key Features
Multi-agent system using CrewAI

Web search powered by SerperDevTool

Deployed with Gradio on Hugging Face Spaces

Agentic Workflow: Modular, extensible, and interpretable


Live Demo:
[Try it on Hugging Face Spaces](https://huggingface.co/spaces/Kenneth19p/BIBLE_AGENT)

## Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/bible_agent/config/agents.yaml` to define your agents
- Modify `src/bible_agent/config/tasks.yaml` to define your tasks
- Modify `src/bible_agent/crew.py` to add your own logic, tools and specific args
- Modify `src/bible_agent/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the BIBLE_AGENT Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The BIBLE_AGENT Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the BibleAgent Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
