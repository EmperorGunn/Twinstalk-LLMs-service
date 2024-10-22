# README

## Overview

This project is an implementation of a LLM-based multi-agent system using several specialized agents built on OpenAI's GPT-4. The system includes agents that handle various tasks, including health advice, financial advice, robot control, and user interaction. The backend is powered by Flask, and the communication between the user and the agents is coordinated hierarchically.

## System Components

### Agents
There are five main agents in this system:
1. **Twinstalk**: The primary user interface agent, responsible for interacting with users and initiating conversations.
2. **VoiceTeamLLM**: Handles communication tasks related to health or financial matters and coordinates with other agents (HealthAdvisor and FinancialAdvisor) for deeper responses.
3. **RobotLLM**: Manages tasks related to robot control or manipulation. Please note that the system is currently in the testing phase, so this agent will respond with a fixed message for now.
4. **HealthAdvisor**: Provides expert responses related to health issues.
5. **FinancialAdvisor**: Provides expert responses related to financial issues.

Each agent is instantiated with a unique prompt and generates responses based on user input using the OpenAI API.

### Flask Server (`server.py`)
- The Flask server handles POST requests at the `/ask` endpoint, which allows users to interact with the system via JSON-based questions.
- The system coordinates between agents based on the user input, generating responses in a hierarchical manner, as follows:
  - `Twinstalk` processes the user input.
  - Depending on the content of the conversation, the system may involve `VoiceTeamLLM`, `HealthAdvisor`, `FinancialAdvisor`, or `RobotLLM` to further refine the response.
- Logging is enabled to track each stage of the conversation.

### Client Interface (`client.py`)
- The client interacts with the Flask server by sending questions in a loop.
- The client sends user input to the server and handles the response, printing the result to the console.
- The client provides error handling for network issues and unexpected responses.

## How to Run

### Prerequisites
1. Python 3.7 or higher.
2. Required packages (install with pip):
   - `Flask`
   - `requests`
   - `openai`

### Installation

1. Clone this repository.
2. Install the required dependencies:
   ```bash
   pip install flask requests openai
   ```
3. Place your OpenAI API key in `Agent.py`.

### Running the Server

1. Navigate to the project directory.
2. Start the Flask server:
   ```bash
   python server.py
   ```
   The server will run on `http://127.0.0.1:5000`.

### Running the Client

1. In a separate terminal, run the client:
   ```bash
   python client.py
   ```
2. Enter your question, and the system will return the response. Type `exit` to quit the client.

### Logging

- All interactions are logged in `server.log`, allowing you to track the system's decision-making process at each step.

## Example Usage

1. Start the server and client as described.
2. Enter a question into the client, such as:
   ```
   Please give me financial advice.
   ```
3. The system will coordinate responses from `Twinstalk` and potentially other agents such as `FinancialAdvisor` to generate the answer.

## Files Structure

- `Agent.py`: Defines the agent classes for handling various tasks.
- `server.py`: The Flask server that coordinates between agents and handles incoming requests.
- `client.py`: The client interface for interacting with the server.
- `prompt/`: Contains text files with the initial prompts for each agent.
- `test/`: Contains python files with test content.