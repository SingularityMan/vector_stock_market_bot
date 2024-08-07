# Vector Stock Market Bot
![image](https://github.com/user-attachments/assets/24b73d6c-2b0f-4ef8-8a2a-a12db1f46eaf)

Welcome to the Vector Stock Market Bot! This bot is designed to automatically rebalance your Robinhood portfolio by gathering information about each ticker and performing buy/sell actions as needed. It operates hands-free, ensuring balanced transactions and avoiding the Pattern Trader rule.

# Table of Contents
- [Features](#Features)
- [Installation](#Installation)
- [Installing Ollama](#Ollama)
- [Usage](#Usage)
- [Updating your portfolio](#Portfolio)
- [Contributing](#Contributing)
- [License](#License)
- [Disclaimer](#Disclaimer)

# Features

- Automated Rebalancing: Uses robin_stocks and Polygon.io's REST API client to gather information on stocks within a given portfolio and makes buy/sell decisions based on the analysis.
- Hands-Free Trading: Executes trades via robin_stocks, ensuring transactions are balanced while avoiding the Pattern Trader rule.
- Daily Operations: Runs indefinitely, performing one trade per ticker per day, and evenly distributing buying power among them.
  
# Installation

- Robinhood Account: Create a Robinhood account if you don't have one.
- Polygon.io API Key: Generate a REST API key using Polygon.io's free tier. [Instructions here](https://polygon.io/pricing).
- Environment Variable: Store your API key in an environment variable named `POLYGON_API_KEY`. Do the same for `ROBINHOOD_USERNAME` and `ROBINHOOD_PASSWORD`.

## Environment Variable Set Up

### Windows
`setx POLYGON_API_KEY "your_api_key_here"`

`setx ROBINHOOD_USERNAME "your_username_here"`

`setx ROBINHOOD_PASSWORD "your_password_here"`
### MacOS/Linux
`export POLYGON_API_KEY="your_api_key_here"`

`export ROBINHOOD_USERNAME="your_username_here"`

`export ROBINHOOD_PASSWORD="your_password_here"`

# Ollama

[Install ollama](https://ollama.com/) and run `llama3:8b-instruct-fp16` or any model you'd like. 
If running a different model, update the model name in the `run()` function in `main.py`.

NOTE: Depends on which model you will run, but `llama3:8b-instruct-fp16` typically requires 16GB VRAM to run on your GPU.

# Setting Up the Virtual Environment

`python -m venv vector_stock_market_bot`

Windows:

`.\vector_stock_market_bot\Scripts\activate`

MacOS/Linux:

`source vector_stock_market_bot/bin/activate`

## Install the required packages:

`pip install -r requirements.txt`

# Usage
***IMPORTANT NOTE:***
- ***Run the bot either before 9:30 AM or after 4:00 PM to avoid token expiration during transactions.***
- ***Do not make any trades manually while the bot is running in order to avoid triggering the pattern trader rule.***

### Run the main script:

`python main.py`

- If your Robinhood username/password are not found, enter your Robinhood username and password manually when prompted.

- Allow the bot to run indefinitely.

# Portfolio

If you would like to change the tickers to match your own portfolio, feel free to update `ticker_list`:


```
# Get ticker list of blue chip stocks and historically successfull index funds
ticker_list = [
    'AAPL', 'AGG', 'AMT', 'AMZN', 'ARKK',
    'BAC', 'BKX', 'BND', 'BNDX', 'DGRO', 'CNI',
    'DKNG', 'DUK', 'EPR', 'F', 'FAS',
    'FNGU', 'GOOG', 'GS', 'HDV', 'HRZN',
    'IEMG', 'INTC', 'IVR', 'IVV', 'IWM', 'IXJ',
    'IYR', 'JNJ', 'JPM', 'KBWB', 'KO',
    'KRE', 'LCID', 'LLY', 'LTC', 'MAIN',
    'META', 'MS', 'MSFT', 'NEE', 'NOBL',
    'NVDA', 'NVO', 'O', 'PFE', 'PG',
    'PSEC', 'QQQ', 'SCHD', 'SMCI', 'SLG', 'SOXL',
    'SPG', 'SPHD', 'SPXL', 'SPY', 'T',
    'TNA', 'TQQQ', 'TSLA', 'UNH', 'UNM', 'UPRO',
    'USB', 'VHT', 'VIG', 'VNQ', 'VTI',
    'VXUS', 'VYM', 'WFC', 'WMT', 'XLF',
    'XLP', 'XLU', 'XLV', 'XOM'
]
```


# Contributing

Please read our [Contributing Guidelines](CONTRIBUTING.md) and [Code of Conduct](CODE_OF_CONDUCT.md) for details on our code of conduct and the process for submitting pull requests.

# License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/SingularityMan/vector_stock_market_bot/tree/main?tab=MIT-1-ov-file#) file for details.

# Disclaimer
I am not a financial advisor. This bot is provided as-is, without any guarantees or warranties. You are using this bot at your own risk, and I am not responsible for any financial losses or other damages that may result from its use. Always do your own research and consider consulting with a qualified financial advisor before making any investment decisions.
