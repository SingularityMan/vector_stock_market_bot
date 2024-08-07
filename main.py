import os
import time
import requests
import json
import robin_stocks.robinhood as r
import datetime
import pytz
from polygon import RESTClient
from polygon.rest.models import (
    TickerNews, MarketStatus, MarketHoliday,
)

def run(user_input):

    # Use Ollama's API to generate a response
    url = "http://localhost:11434/api/chat"
    headers = {
        "Content-Type": "application/json"
    }

    messages = [{"role": "user", "content": user_input}]

    # Define the payload
    payload = {
        "model": "llama3.1:8b-instruct-fp16",
        "messages": messages,
        "stream": False,
        "options": {
            "temperature": 0.1,
            "num_ctx": 8000
            # "stop": []
        }
    }

    # Make the POST request, extract text response
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    response_data = response.json()
    text_response = response_data.get("message", {}).get("content", "No response received")
    return text_response

def refresh_token(username, password, token_expires_at, token):

    # Check if the token is expired
    if time.time() > token_expires_at:
        # If the token is expired, refresh it
        print("Token expired. Refreshing token.")
        r.logout()
        login = r.login(username, password, expiresIn=60*60*12)
        token_expires_at = time.time()+login['expires_in']
        token = login['access_token']
        # print("New Token:", token)
    else:
        print("Token is still valid. Expires in", token_expires_at-time.time(), "seconds.")
        # print("Token:", token)
    return token_expires_at, token

# No news error
class NoNewsError(Exception):
    pass

def get_market_holidays(api_key):
    client = RESTClient(api_key)
    holidays = client.get_market_holidays()
    return holidays

def generate_text(user_input):
    response = ""
    while response is None or response.strip() == "" or response == " ":
        try:
            response = run(user_input)
            if response.startswith('"') and response.endswith('"'):
                response = response[1:-1]
            response = response.strip()
        except Exception as e:
            print(e)
            print("Error generating text. Trying again.")
            continue
        return response

# Get ticker info from robinhood
def get_ticker_info(ticker):
    info = r.stocks.get_stock_quote_by_symbol(ticker)
    return info

# Get advanced ticker info
def get_advanced_ticker_info(ticker):
    info = r.stocks.get_fundamentals(ticker)
    return info

def get_quarterly_earnings(ticker):
    info = r.stocks.get_earnings(ticker)
    return info

def make_decision(response):
    user_input = "<s>[INST]" \
                  "Review this information and respond with a one-word response and include the following: [buy], [sell], or [hold].\n" \
                  "Here is the following information:\n\n" \
                  "{}\n\n" \
                  "If there is no text or the information is not clear, respond with [hold].\n" \
                  "[/INST]".format(response)

    decision = generate_text(user_input)
    while decision is None or decision.strip() == "" or decision == " ":
        print("Decision is None. Trying again.")
        decision = generate_text(user_input)
    return decision

def yayayayaya():
    print("Hey! Hey! Hey! its time to make some CRRRRRRRRRRRRRAAAAAAAAAAAAZY money!")
    time.sleep(2.50)
    print("Are ya ready?")
    time.sleep(0.75)
    print("HERE")
    time.sleep(0.25)
    print("WE")
    time.sleep(0.25)
    print("GO!")
    time.sleep(0.25)
    print("$YA!")
    time.sleep(0.25)
    print("$YA!")
    time.sleep(0.25)
    print("$YA!")
    time.sleep(0.25)
    print("$YA!")
    time.sleep(0.25)
    print("$YA!")

# Login to robinhood
# Your login credentials

username = os.getenv("ROBINHOOD_USERNAME")
password = os.getenv("ROBINHOOD_PASSWORD")

if username and password:
    pass
else:
    print("Login credentials not found, manual input required.")
    username = input("Enter your Robinhood username: ")
    password = input("Enter your Robinhood password: ")

# RESTClient for Polygon.io
polygon_api_key = os.getenv('POLYGON_API_KEY')
client = RESTClient(polygon_api_key)

# Login to Robinhood
login = r.login(username, password, expiresIn=60*60*12)
token_expires_at = time.time()+login['expires_in']
token = login['access_token']
all_stock_news = []
history = []

yayayayaya()

if __name__ == '__main__':

    history = ['']

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

    valid_tickers = []

    print("Ticker list length:", len(ticker_list))

    for ticker in ticker_list:
        try:
            info = r.stocks.get_stock_quote_by_symbol(ticker)
            if info is not None:
                print(info['symbol'], "found")
                valid_tickers.append(ticker)
            else:
                print("Ticker removed:", ticker)
        except Exception as e:
            print(e)
            print("Ticker removed:", ticker)

    ticker_list = valid_tickers

    print("Ticker list length:", len(ticker_list))
    failed_transactions = []
    queued_transactions = {}
    ticker_index = 0

    """Main loop for stock bot. This bot will buy, sell, or hold stocks based on the news and the stock's performance.
    It will also check if the NYSE is open and if it is 9:30am EST. If it is not exactly 9:30am EST, the bot will skip transactions.
    If it is a holiday, the bot will also skip transactions. If the bot fails to make a transaction, it will add the ticker to 
    a list of failed transactions and try again after the initial loop is complete. If the bot succeeds in making a transaction, it will remove the ticker from the
    list of failed transactions if it was added there. The bot will also check if the user has enough buying power to make a transaction. If the user
    does not have enough buying power, the bot will skip the transaction."""

    while True:

        try:

            time.sleep(1)

            # Refresh the token if it is expired
            token_expires_at, token = refresh_token(username, password, token_expires_at, token)

            # Check if it is Saturday or Sunday
            if datetime.datetime.now(pytz.timezone('America/New_York')).weekday() == 5 or datetime.datetime.now(pytz.timezone('America/New_York')).weekday() == 6:
                print("It is the weekend. Skipping transactions.")
                continue

            # Check if it is before 9:30am EST or after 4:00pm EST
            # If so, cancel all pending orders
            if (datetime.datetime.now(pytz.timezone('America/New_York')).hour < 9 or (datetime.datetime.now().hour == 9 and datetime.datetime.now().minute < 30)) or datetime.datetime.now(pytz.timezone('America/New_York')).hour >= 16:
                print("Not between 9:30am and 4:00pm EST. Cancelling all pending orders, if any")
                try:
                    orders = r.orders.get_all_open_stock_orders()
                    for order in orders:
                        print("Cancelling order:", order['id'])
                        r.orders.cancel_stock_order(order['id'])
                    failed_transactions = []
                    queued_transactions = {}
                    time.sleep(30)
                except Exception as e:
                    print(e)
                    print("Error cancelling orders. Continuing.")
                    token_expires_at, token = refresh_token(token_expires_at, token)
                    continue

                continue

            # Check if it is 9:30am EST and if there are no failed transactions
            if (datetime.datetime.now(pytz.timezone('America/New_York')).hour != 9 or (datetime.datetime.now().hour == 9 and datetime.datetime.now().minute != 30)):
                if len(failed_transactions) == 0 and len(queued_transactions) == 0:
                    print("Not 09:30am EST. Skipping transactions.")
                    print("Current time:", str(datetime.datetime.now().hour)+":"+str(datetime.datetime.now().minute))
                    continue

            try:
                # Check if today is in a stock market holiday in polygon.io
                holidays = get_market_holidays(polygon_api_key)

                # Use strptime to convert the date string to a date object.
                today = datetime.datetime.now(pytz.timezone('America/New_York')).date()

                for holiday in holidays:
                    holiday_date = datetime.datetime.strptime(holiday.date, '%Y-%m-%d').date()
                    if holiday_date == today:
                        break
            except Exception as e:
                print(e)
                pass

            if holiday_date == today:
                print("It is a stock market holiday. Skipping transactions.")
                time.sleep(30)
                continue

            # Wait 60 seconds before making transactions
            print("Waiting 60 seconds before making transactions.")
            time.sleep(60)

            # Get account holdings and buying power
            buying_power = None
            while isinstance(buying_power, float) is False or buying_power is None:
                try:
                    holdings = r.account.build_holdings()
                    buying_power = float(r.account.load_phoenix_account(info='account_buying_power')['amount'])
                except Exception as e:
                    print(e)
                    print("No buying power found. Waiting 30 seconds before trying again.")
                    time.sleep(30)
                    continue

            print(holdings)
            print("Buying power: " + str(buying_power))
            day_trades = len(r.account.get_day_trades()['equity_day_trades'])
            print("Day trades:", day_trades)

            # Loop through the ticker list. This is usually done once a day at 9:30am EST.
            # If anything goes wrong, it will add the ticker to the failed transactions list and move on to the next ticker.
            # Any tickers in the failed transactions list will be retried as soon as possible after the initial for loop.
            # Any successful evaluations will be put in a queue to be executed.

            for ticker in ticker_list:

                # Indicates attempt to process a ticker
                ticker_index += 1

                # Checks if all the tickers have been processed before skipping.
                # If the tickers have not been processed and the ticker is in the failed transactions list or the queued transaction list, it will skip.
                # This is added in the event an error is triggered and the bot needs to continue where it left off.
                if ticker_index >= len(ticker_list):
                    if ticker not in failed_transactions:
                        continue
                elif ticker_index < len(ticker_list):
                    if ticker in failed_transactions or ticker in queued_transactions:
                        continue

                try:

                    # Get stock news
                    all_stock_news = []

                    # Get ticker info, fundamentals and quarterly earnings.
                    info = get_ticker_info(ticker)
                    ticker_fundamentals = get_advanced_ticker_info(ticker)
                    ticker_earnings = get_quarterly_earnings(ticker)

                    try:

                        polygon_news = client.list_ticker_news(ticker, limit=5)
                        for i, news in enumerate(polygon_news):
                            #print(ticker, "Call:", i)
                            all_stock_news.append(news.description)
                            if i == 7:
                                break
                            # print(news.article_url)
                    except Exception as e:
                        print("Error:", e, "\nWaiting 60 seconds before continuing.")
                        time.sleep(60)
                        pass

                    # Join all the news together
                    for text in all_stock_news:
                        if text is None:
                            all_stock_news.remove(text)
                        else:
                            #print(text)
                            pass
                    try:
                        all_stock_news = "".join(all_stock_news)
                    except TypeError:
                        all_stock_news = ""
                        pass

                    # Generate a response to the news
                    news = generate_text("<s>[INST]Summarize this text, highlighting important developments regarding the ticker, such as earnings reports, financials, announcements, events, etc.\n"
                                                "The ticker is {}.\n"
                                                "Here is the text:\n\n{}\n[/INST]".format(ticker, all_stock_news))

                    # Evaluate stock news and performance
                    stock = ticker
                    stock_price = info['last_trade_price']
                    user_input = ("<s>[INST]"
                                  "You are a stock market expert.\n"
                                  "You will review news on a ticker and make an educated guess on whether to buy, sell or hold.\n"
                                  "Be as brief as possible.\n"
                                  "Ticker name: {}\n"
                                  "ticker price: {}\n"
                                  "Additional ticker info: \n\n{}\n\n"
                                  "ticker_fundamentals: \n\n{}\n\n"
                                  "ticker earnings: \n\n{}\n\n"
                                  "ticker news: \n\n{}\n\n"
                                  "Give equal weight to both the news and the stock's performance.\n"
                                  "[/INST]".format(stock, stock_price, info, ticker_fundamentals, ticker_earnings, news))

                    response = generate_text(user_input)

                    try:
                        #if response.startswith('"') and response.endswith('"'):
                            #response = response[1:-1]
                        response = response.strip()
                        print(ticker+":", response)

                        # Make a decision to buy, sell, or hold based on the response
                        decision = make_decision(response).lower()
                        print(decision)

                    except Exception as e:
                        print(e, "Continuing.")
                        if ticker not in failed_transactions:
                            failed_transactions.append(ticker)
                        continue
                    try:
                        print("Decision:", decision)

                        # Add ticker to the queue based on the decision and available buying power
                        if ("buy" in decision or "hold" in decision) and ticker not in queued_transactions:
                            queued_transactions[ticker] = "buy"
                        elif "sell" in decision and ticker not in queued_transactions:
                            queued_transactions[ticker] = "sell"
                        else:
                            if (ticker not in holdings and buying_power > 1) and ticker not in queued_transactions:
                                queued_transactions[ticker] = "hold"

                    except Exception as e:
                        print("Error:", e, "Continuing.")
                        if ticker not in failed_transactions:
                            failed_transactions.append(ticker)
                        continue
                except Exception as e:
                    print("Error:", e, "Continuing.")
                    if ticker not in failed_transactions:
                            failed_transactions.append(ticker)
                    continue

                # Assumes the transaction was successful
                if ticker in failed_transactions:
                    failed_transactions.remove(ticker)

            # Check if there are any queued transactions and execute them.
            if len(queued_transactions) > 0:
                print("Executing queued transactions.")

                # Create a list of keys
                tickers = list(queued_transactions.keys())

                # Sort the list with a custom key function, sorting by sell first.
                sorted_tickers = sorted(tickers, key=lambda ticker: (
                queued_transactions[ticker] != 'sell', queued_transactions[ticker]))

                # Iterate through the sorted list, selling tickers first before buying the rest.
                # This ensures no leftover buying power and therefore no missed trades.
                for ticker in sorted_tickers:
                    decision = queued_transactions[ticker]

                    # Get the currently available buying power
                    actual_buying_power = None
                    actual_buying_power = float(r.account.load_phoenix_account(info='account_buying_power')['amount'])

                    # Day trade check.
                    # No transactions will be made if the user has made 3 day trades in a 5 day period.
                    day_trades = len(r.account.get_day_trades()['equity_day_trades'])

                    # Perform the trade, depending on the decision.
                    if (decision == "buy" or decision == "hold") and day_trades < 3: # Buy if decision is to buy or hold.
                        if actual_buying_power > 1:
                            print("Purchasing {}".format(ticker))
                            print("Buying power: {}".format(buying_power))

                            # Determine if the user has enough buying power to buy the stock.
                            # The purchase is evenly distributed across your portfolio.
                            if buying_power / len(ticker_list) < 1:
                                trade = r.orders.order_buy_fractional_by_price(ticker, 1, timeInForce='gfd',
                                                                               extendedHours=False)
                            elif buying_power / len(ticker_list) > actual_buying_power:
                                trade = r.orders.order_buy_fractional_by_price(ticker,
                                                                               actual_buying_power,
                                                                               timeInForce='gfd',
                                                                               extendedHours=False)
                            elif buying_power / len(ticker_list) < actual_buying_power:
                                trade = r.orders.order_buy_fractional_by_price(ticker,
                                                                               buying_power / len(ticker_list),
                                                                               timeInForce='gfd',
                                                                               extendedHours=False)
                            print(trade)
                            print("Trade id:", trade['id'])
                            time.sleep(30)
                            trade = r.orders.get_stock_order_info(trade['id'])

                            # Check if the trade was filled
                            # If not, add the ticker to the failed transactions list and try again later.
                            if trade['state'] != "filled":
                                print("Trade not filled. Continuing.")
                                if ticker not in failed_transactions:
                                    failed_transactions.append(ticker)
                                continue
                            print("Purchased", ticker)
                            if ticker in failed_transactions:
                                failed_transactions.remove(ticker)
                        else:
                            print("Not enough buying power. Continuing.")
                            if ticker in failed_transactions:
                                failed_transactions.remove(ticker)

                    # Sell if decision is to sell.
                    # This will sell all the shares of the stock.
                    elif decision == "sell" and day_trades < 3:
                        if ticker in holdings:
                            print("Selling", ticker)
                            trade = r.orders.order_sell_fractional_by_quantity(ticker,
                                                                               float(holdings[ticker]['quantity']),
                                                                               timeInForce='gfd',
                                                                               extendedHours=False)
                            print(trade)
                            print("Trade id:", trade['id'])
                            time.sleep(30)
                            trade = r.orders.get_stock_order_info(trade['id'])
                            if trade['state'] != "filled":
                                print("Trade not filled. Continuing.")
                                if ticker not in failed_transactions:
                                    failed_transactions.append(ticker)
                                continue
                            print("Sold", ticker)
                            if ticker in failed_transactions:
                                failed_transactions.remove(ticker)
                        else:
                            print(ticker, "not in holdings. Continuing.")
                            if ticker in failed_transactions:
                                failed_transactions.remove(ticker)

                    if day_trades >= 3: # Cancel all pending DECISIONS if day trade limit is reached. No transactions will be made.
                        if ticker in failed_transactions:
                            failed_transactions.remove(ticker)
                        print("Day trade limit reached. Continuing.")

                    # Ticker processed
                    del queued_transactions[ticker]

            # If all transactions, including failed transactions, are processed, reset the ticker index
            if len(failed_transactions) == 0 and ticker_index >= len(ticker_list):
                print("All transactions successful! Resetting ticker index.")
                ticker_index = 0

        except Exception as e:
            print(e)
            print("Error. Continuing.")
            token_expires_at, token = refresh_token(token_expires_at, token)
            continue
