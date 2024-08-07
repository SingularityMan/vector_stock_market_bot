# Vector Stock Market Bot
![image](https://github.com/user-attachments/assets/24b73d6c-2b0f-4ef8-8a2a-a12db1f46eaf)

Welcome to the Vector Stock Market Bot! This bot is designed to automatically rebalance your Robinhood portfolio by gathering information about each ticker and performing buy/sell actions as needed. It operates hands-free, ensuring balanced transactions and avoiding the Pattern Trader rule.

# Table of Contents
- [Features](#Features)
- [Installation](#Installation)
- [Prerequisites](#Prerequisites)
- [Installing Ollama](#Installing Ollama)
- [Setting Up the Virtual Environment](#Setting Up the Virtual Environment)
- [Usage](#Usage)
- [Contributing](#Contributing)
- [License](#License)
- [Disclaimer](#Disclaimer)

# Features

- Automated Rebalancing: Uses robin_stocks and Polygon.io's REST API client to gather information on stocks within a given portfolio and makes buy/sell decisions based on the analysis.
- Hands-Free Trading: Executes trades via robin_stocks, ensuring transactions are balanced while avoiding the Pattern Trader rule.
- Daily Operations: Runs indefinitely, performing one trade per ticker per day, and evenly distributing buying power among them.
  
# Installation
### Prerequisites
- Robinhood Account: Create a Robinhood account if you don't have one.
- Polygon.io API Key: Generate a REST API key using Polygon.io's free tier. [Instructions here](https://polygon.io/pricing).
- Environment Variable: Store your API key in an environment variable named POLYGON_API_KEY.

# Environment Variable Set Up

### Windows
`setx POLYGON_API_KEY "your_api_key_here"`
### MacOS/Linux
`export POLYGON_API_KEY="your_api_key_here"`

# Installing Ollama

[Install ollama](https://ollama.com/) and run `llama3:8b-instruct-fp16` or any model you'd like. 
If running a different model, update the model name in the `run()` function in `main.py`.

## VRAM requirements
Depends on which model you will run, but `llama3:8b-instruct-fp16` typically requires 16GB VRAM to run on your GPU.

# Setting Up the Virtual Environment
## Create a virtual environment:

`python -m venv vector_stock_market_bot`

*Windows:*

`.\vector_stock_market_bot\Scripts\activate`

MacOS/Linux:

`source vector_stock_market_bot/bin/activate`

## Install the required packages:

`pip install -r requirements.txt`

# Usage
## Important Notes
- Run the bot either before 9:30 AM or after 4:00 PM to avoid token expiration during transactions.
- ***Do not make any trades manually while the bot is running in order to avoid triggering the pattern trader rule.***
### Steps to Run
Activate the virtual environment:

### Windows
`.\vector_stock_market_bot\Scripts\activate`

### MacOS/Linux
`source vector_stock_market_bot/bin/activate`

### Run the main script:

`python main.py`

- Enter your Robinhood username and password when prompted.

- Allow the bot to run indefinitely.

# Contributing

Please read our [Contributing Guidelines](CONTRIBUTING.md) and [Code of Conduct](CODE_OF_CONDUCT.md) for details on our code of conduct and the process for submitting pull requests.

# License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/SingularityMan/vector_stock_market_bot/tree/main?tab=MIT-1-ov-file#) file for details.

# Disclaimer
I am not a financial advisor. This bot is provided as-is, without any guarantees or warranties. You are using this bot at your own risk, and I am not responsible for any financial losses or other damages that may result from its use. Always do your own research and consider consulting with a qualified financial advisor before making any investment decisions.
