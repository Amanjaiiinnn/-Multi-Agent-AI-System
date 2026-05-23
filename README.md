# Project Title: Multi-Agent AI System

This repository contains a collection of AI agents and utility scripts built using Python and the Agno (formerly Phidata) framework.

## Repository Structure

- **agent.py**: The core configuration for the AI agents, defining their personas and tool access.
- **TEAMS.PY**: Implementation of multi-agent orchestration, allowing different agents to collaborate on complex tasks.
- **finance.py**: A specialized financial agent capable of analyzing stock market data, retrieving analyst recommendations, and summarizing financial news.
- **youtube_analyzer.py**: An agent designed to process YouTube video content, providing summaries or extracting specific information from transcripts.
- **memory.py** & **memory2.py**: Scripts handling the persistence and long-term memory management for the agents, likely using a database like `agno.db`.
- **requirements.txt**: A list of Python dependencies required to run the agents in this repository.

## Getting Started

### 1. Installation
Clone the repository and install the dependencies:
```bash
pip install -r requirements.txt
2. Environment Variables
Ensure you have your API keys set up (e.g., OpenAI, Google, or YFinance) in your environment or a .env file.

3. Usage
You can run individual agents or the team orchestration:

python TEAMS.PY
