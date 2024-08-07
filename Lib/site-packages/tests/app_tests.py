from uuid import uuid4
import datetime
import sys
import pyotp
import os
from dotenv import load_dotenv
load_dotenv()
import requests

import robin_stocks.robinhood as r
import robin_stocks.gemini as g
import robin_stocks.tda as t

single_stock = 'AAPL'

totp  = pyotp.TOTP(os.environ['robin_mfa']).now()
print("Current OTP:", totp)
login = r.login(os.environ['robin_username'], os.environ['robin_password'], store_session=True, mfa_code=totp)
print("login data is ", login)
print(r.load_account_profile(info=None))
exit()
# print("===")
# print("running test at {}".format(datetime.datetime.now()))
# print("===")

# order = r.get_watchlist_by_name("test")
# print(order)

# t.login_first_time("2HURJS3NJN4BCXZ84HHHDACAGRTCNDDU",
# "BpjW+hnsy9tO5OFBv0QUIpCLvTx4/2sLr1xJD3uao8PL9/qCuFQ6g5IchzHBTY6Az8nf7CrO5klTrcF8tpRH/l6e7sTQCluzDfUjqVJJC4Vmx2S1XOsbYKpm+jFiIg84+H0f/pUrrgtFiy3bKMUzz/M6TTsAwN1VWeaet7aoMsguvnsq7nNXCkR2COlKbFAlFvg69YvagiJFC0wdBwhLvYPLAH6cxIGTT6CYMMIZ06qsqCQ7jzVLqMd24pw2FpVtzQYgzb8XVORQ3KWrtrX7tiecsSOVZxNKz0zc30rZPeEecwWgZSMLF2KZseQs8unl8Kv6GRV397FYUskduy9/Whk8acP9EfSHvG4O8zAhXr0B13dRHdSMcVqXgu72FX5PzuAj7B98MT0ew1OdAP3Qw3/bPE0Wg3iRrFGS2XeBAc1lM26MgXcp0sgyOXykAwpepvp4d+HKAZ2fqZTSk/XQlLpfSNzG/S+yVkp6lQiTCZRPUavCk7+MiqD/uSHYBUP+suNlkdIy6CJDk4VJk2lKjdXDadn2qny509cmn100MQuG4LYrgoVi/JHHvlXs39mVzQtKjpZ+4SdOckKKkzf+5YhvTSbPDJhijmMOaGKKKh0ziBaU5h8WI8UiKbBWnxPReHQoSYDd/W6ZR7y4ngBnZSeIMc0izFfzwZFcSK0mAruUcQviqReFNj4RPMluq2sY9BBEwf6KdO4IthWEihE9imCzU8ZdSalYwJ6VRDN7A2G1gMW1SB7g/rF7UwqmHpTxdlBYjoUD4ypDUgpWuWpQ80FCNor4GFdYAQeoI0BPVAAtHNg5IcqCfy71XB8WhL0GKuuTrL5UjBxZqA3iDBPnL+NpoY4FZppkD6noqF/b++hPnd0t0b0kYJe09zh/cC2OtOoTWBoYTDdB/jNRLCd+PNrD6Q/rFOx/Wx1mujS1YjlQqwHA5G1cd02ODUM1OO04aBy48eTuQXupWNDFsLqWqwauw6ZBPqszQuNCKs0v+nebBcBBWhlW9ULD8pDr9qMcpR6iYMbxvQA8ho7Bc77+FB2Nh/ajEqL84sRDsuy71tIpelcYgQ4yOoHB6ebNHkFJtOwTuX4gnGF8DN8KrhQ7OwVGIPtf1yOK212FD3x19z9sWBHDJACbC00B75E",
# "G2aUpN+qXx61tNumt4aKThC7W0u8IvWmv1W7rSawftRxkskYUPgpVJSCZ4tmgXHmLlZu8r+uTIT5uBLMqN5peW8n4dAatdvLLLt7TFqcw63m7fCU6qaiWxhzaLF3QfPq7h3DPTCNVr+/SQmKOmqBi+t6KYyXGi94jTiQOB1BjkTmE9qPf35AL9cr5kKYbVXJEOeTNsedcFMXjo8+UCPLrtnW2rCFa1FOjmjMCxZX4M/RuwXVa/5+tTXq3+jOlBmabjz7SiDP42ooPVkhncBeXP4oq8zYnBnhLnLxx0falDcbFY1K8QZ6tftHsSFCjF9QkzigQpbyhAjaqfm7C+46+w/89I15eGJn9HsWyYNd2Y6f8LJg8bMoRtnQoqshwUEtSiJqfd2vq4TaabLn6snBcuBoj2m6qyDSfM6oQA/vM8PIYqzfmsI7gok6jWf100MQuG4LYrgoVi/JHHvl2iAD+MiwRt1Jcok/7oEYYXXBmA1DiKQSi8bRcOG2zSogi5JMtUiqV9YrHrZ0V0U2YwkxRT4JlUJPj/kU+09YUOn5qxnog5CvI4eGyndWLq7PRa3TJ7bEpEuMTW765C91Ei2SKKqBDfzpzjDkX6whFvH4pB7cP4SxviNx6nmCB8Ywd1Qh0MqCp3251b+mRvbHW24ZbdPPJZsod0OomFEpCJ/l/G4Cb0bnJ0BMarONjR5J+Phk6xVzUrCaFI7+ho8IL9KGsJxZI7WaE1IHnpeJBaJMxqgSUa/6bOQgmuIUuOMdycCNVv59XO1tg7PvKAGJ3eGh3pmojy89Q28bhBpE9aJfAKqlke8HD26akrOgBZVD85ch13yTBCfuHPSkxZ9iy+XeYq78EU4WE7qV4ZfUjtzB2ZJOZzR/FRe0NpGuiRe0k1MOCnTsh5SgwNs=212FD3x19z9sWBHDJACbC00B75E")

# t.login_first_time("2HURJS3NJN4BCXZ84HHHDACAGRTCNDDU",
#                    "9NfI4Or1pbhSmfCNg9Szw9uH7z46cCQzFn83ND7vehm7dmvJhEJIu7eK9PvpF5ymUc9OVlUTJYXZocSYMQYOgEPdYTYeQN4K8Wg4PFK7TWDA3Y7s3gRcjbQubfOL5aRDpR9l2bS/3nDQvFOQTHS/8wJg7lqVJMBHWH7w5HfIa3uMVrtg6bVgjDu0yMOzv/jnyKmn+ks95HFAj45ccM9IpgI8cvkwlOw72A2vnJAJmuITs8a4nAwNKPnO4yuApsUR92G3LDdAK+eBTcN7pBeEh7eZU49Mu1291wAY2WthWWl26qh8qGuAwmsr5RB+PZbo4+ebISVZetLMej9yFhhWBnB/cRD+mI9RGBRMtFL5WXCKVH3OHT41xmcHa1+5f3Hz5CmBAmGpJH+i3roWPSSbDOngFyrLcmu0fu+9hDmRDdL/tk+PU4qSBG8wTZbsNZhwKokZrOXa6NLOUAC7kMBupH8iiDhKU1gVjhbiPSXGcd9Z22OpmzhBT5SyftZFs1ysz/YCoNCUG0XpRe6IrUVDiGnAlwuuhH/TcneFmoczHi1NO10N0100MQuG4LYrgoVi/JHHvlKEUe2uBmLFCkJskrle34M3SQixpz4bUKmZoAsFwQAurNIGf9w+MjnNxOERKw+hO8nNbGKDvJ2BYZ+8NiuahbywpD0PqvWFrmmu4sQ6NrXT/pj4QfKqcfXqUhpn1Eb2jERC12qGXE9+rIzUiKX0LiZmLsjP1xYPwPSh/40DMYaGXXjYHDX9EJg4bwZgfguQuwquDWAw3jXUjGhAnK5aLo3Y7G499Gu/X8oWkB+HprlOJddjNHg6lMvhJKRIO7mHQSpLaCrqbiK9jgd9QdJ1gAUS96EmaXwbmnpiJfS6cs67XgoWGoBsWAMCKv+MZTt0tK8+xzPEB6gyeGFdxtrxE1X0wdl6gTncIxghPTCREzmNdqlQw1AdPFcVh9x8WIy2QKvxj7RDK5/6bvDm0I0GgPQr46NBN87bG+7u+orwcs6LrTOTA1NY6dlgKNQtKlf9npQcrRAEk2B0DG9mzolLN7Za203yEXfl4OzcbyjNUmxTb39bdMqyO3csEKmp8I89nPFlNhVMVJLcOCTXK3Bi5fC87ZyccCPcSuvw7j1YRsntMM1vkQ==212FD3x19z9sWBHDJACbC00B75E",
#                    "HrE6Hs+9rKxQczwG61se9jjokcelBTuq7rG1+YePxJfnyOlopkcku2fpCfBwB4bJ8++mpxDRz32InTMcWhnMzV0h6MFS3GXdO0Cwy3NZuslC9hUhAVtviGNUbSP5fS0lpnZy6w63S9ygIWor6Y4EKdIGirdLhk4L1pSV30i0qd6zYSFy2prXPGILRUC+LFBIK2xQ4pc0r47b/qSDeickETtXM7mdBNlb+9DboQ9aaf0AOFF6quTHpcZOPeryjWM1/gv7LrmwHeyTvixfdO53tjiunFGfTRAMIaEYWlYjLwTUWDfFkTT5lUOEOAupQ+VfP4dVCuqKwgN+z/X1QQDaWWl40PmymsZcUaIJirpK3BlWlI8EuBUorRKrG2Df51C0m+m7zWpy2/2me5NGQUm7SN1fSytErl8EVLWCGUcWcmBzeV+7O610vHqCwNs100MQuG4LYrgoVi/JHHvl6JfdrQEBiAEFWXP+RSVEgq2cJnqsyTJPV+4pwLUzkOKwp46ZpL3ckQthosey7EOstBhr461mDinfXNcnQ5d5CYH7C+aBrcQ0UPFsdh8RquavV3hhuaK3JVufmiy7NTfKz198mWSlMOluz0kwdPEh66c4Bds374Zwi/pgLnoSIZvkLBT1iAxkCTtptigwdF0WWuu4gebHgVZO8Tx7VOw+9IcRHUb+QjAlEl52uBJDkkVzk73O1RlVlpzGfXRzYvzkcgOkgzgbSi8G2OAavUUwUC1NRIWFR2rJZGhlnaI8QcP138kWl87DXfEx4UJa56YS6Cxhf2YKl5nug6gta7VlqZhwaIX0BM/5omLSrVoMvDI/304/507lxRk0w10xTQOInIb3WCbWVe9ShU5uNW2K8eUwZpp9ECQuF88zDvX7dUp5uG/wRgWWe1qdqro=212FD3x19z9sWBHDJACbC00B75E",
#                    "w_Pt4oNsijRB_b5LdvjBZsM3uPE8uB0503lQk8kf7YE=")

# "G2aUpN%2BqXx61tNumt4aKThC7W0u8IvWmv1W7rSawftRxkskYUPgpVJSCZ4tmgXHmLlZu8r%2BuTIT5uBLMqN5peW8n4dAatdvLLLt7TFqcw63m7fCU6qaiWxhzaLF3QfPq7h3DPTCNVr%2B%2FSQmKOmqBi%2Bt6KYyXGi94jTiQOB1BjkTmE9qPf35AL9cr5kKYbVXJEOeTNsedcFMXjo8%2BUCPLrtnW2rCFa1FOjmjMCxZX4M%2FRuwXVa%2F5%2BtTXq3%2BjOlBmabjz7SiDP42ooPVkhncBeXP4oq8zYnBnhLnLxx0falDcbFY1K8QZ6tftHsSFCjF9QkzigQpbyhAjaqfm7C%2B46%2Bw%2F89I15eGJn9HsWyYNd2Y6f8LJg8bMoRtnQoqshwUEtSiJqfd2vq4TaabLn6snBcuBoj2m6qyDSfM6oQA%2FvM8PIYqzfmsI7gok6jWf100MQuG4LYrgoVi%2FJHHvl2iAD%2BMiwRt1Jcok%2F7oEYYXXBmA1DiKQSi8bRcOG2zSogi5JMtUiqV9YrHrZ0V0U2YwkxRT4JlUJPj%2FkU%2B09YUOn5qxnog5CvI4eGyndWLq7PRa3TJ7bEpEuMTW765C91Ei2SKKqBDfzpzjDkX6whFvH4pB7cP4SxviNx6nmCB8Ywd1Qh0MqCp3251b%2BmRvbHW24ZbdPPJZsod0OomFEpCJ%2Fl%2FG4Cb0bnJ0BMarONjR5J%2BPhk6xVzUrCaFI7%2Bho8IL9KGsJxZI7WaE1IHnpeJBaJMxqgSUa%2F6bOQgmuIUuOMdycCNVv59XO1tg7PvKAGJ3eGh3pmojy89Q28bhBpE9aJfAKqlke8HD26akrOgBZVD85ch13yTBCfuHPSkxZ9iy%2BXeYq78EU4WE7qV4ZfUjtzB2ZJOZzR%2FFRe0NpGuiRe0k1MOCnTsh5SgwNs%3D212FD3x19z9sWBHDJACbC00B75E"

# blah = t.generate_encryption_passcode()
# print(blah)
# print(type(blah))
# print(blah)
# print(blah.decode())
# print(type(blah.decode()))
print(t.login("w_Pt4oNsijRB_b5LdvjBZsM3uPE8uB0503lQk8kf7YE="))
# data, _ = t.get_account("233798512","orders", jsonify=False)
# print(type(data) == requests.models.Response)
# print(data)
order = {
    "orderType": "MARKET",
    "session": "NORMAL",
    "duration": "DAY",
    "orderStrategyType": "SINGLE",
    "orderLegCollection": [
        {
            "instruction": "Buy",
            "quantity": 1,
            "instrument": {
                "symbol": "AMC",
                "assetType": "EQUITY"
            }
        }
    ]
}
# from re import IGNORECASE, match, split
# data, err = t.place_order("233798512", order, False)
# print(data)
# print(t.get_order_number(data))
# data, err = t.get_instrument("88160R101", True)
# data, err = t.get_hours_for_market("OPTION", "2021-02-16", True)
# data, err = t.get_option_chains("AAPL", "PUT", )
data, err = t.get_option_chains("AAPL")
print(data, err)
exit()
# curl -X POST --header "Content-Type: application/x-www-form-urlencoded" -d "grant_type=refresh_token&refresh_token=qjJBft4oazSHjgTeUEt95qJlQJlYxYqWv7Ju62OTE73hDZcTeyI01GlbSJa2eiQjG1o9guz8CatR6NugyJMOIy08qBMYB3EapZVddTkA3pMyztgsBym36RTMPx9XA9B%2BUlTBjqRqQoThVCH5v1PoR6sbiKzqjiWznt3MmQfkPHM3%2FsDXBzueknatunvFNa7JJ1DQxC5OFUUuZnkN6MQpupNfepeymd6W1GlatQW1lJyLaoGJrvnKbY%2BxleicGNwOQI6iRZ30djWgKdyfeBvXEZp7ABTFf2%2FczVnXGa43ow4UjmJKwcpqKhR1qLHe1KN7BgwnvXmlp9bi7TzXPCYDxix5nGqmwaXPx9ZxqraKXcFYpXj5RC5OHSdnr0%2B6RgbrPoEV%2FS0H%2B8sTxmrRYeOEOgF%2B5%2F4uP4M2MvYkm5%2FntkX0xEXmiLyLQaR%2Bc%2Bj100MQuG4LYrgoVi%2FJHHvlKZgyoTHJmrFJcCQFbf4YdWPL9SLHEuRgJ3mvqJenT41nllMAhCAMhPJnXfG1hFV0LkDZoKIY%2FZwXP3zQndWX1cwQBiQlD8Xmzjb9B%2F%2BXY5uWtxhXcRhpZvc%2F2Vwu2qcXZ2NTL%2FqpSJhqK4J8olnLS398E1TqJpkw0RzoM1jajMY9yGhN3ftzVslaHGAMUZtUJcvnKfE6Osq5FzusUINnCjIdhBZhwknkzvja8O2D34a%2BTnQe3c1YZR%2BTYy3dek4%2B1Z%2FZ6qb%2FWpX304aziUoF4Id4QkvDyFgL0wM81kmMYOJd%2B2VfLUjkcGiSPRCUizpUhTUbSBgfATnnLipAxiqBPi6W%2B22zQNQUGUv4rZzes9IivkvYHzkj%2FTOdojFNdGIrs1POjpqH%2BvUxV0mxZVwVn3Bx27hjQd31WL%2BP8zjSYAeAKAeOkDAHQkOg8lk%3D212FD3x19z9sWBHDJACbC00B75E&client_id=2HURJS3NJN4BCXZ84HHHDACAGRTCNDDU" "https://api.tdameritrade.com/v1/oauth2/token"

from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher_suite = Fernet(key)
cipher_text = {"food": cipher_suite.encrypt("cheese".encode())}

print("the cipher text is ", cipher_text)
plain_text = cipher_suite.decrypt(cipher_text["food"])
print("plain text is ", plain_text.decode())

exit()

import hashlib
import hmac
import pickle
from pathlib import Path

my_data = {"food": "cheese", "number": 1}

def make_digest(message):
    return hmac.new(b'12345', message, hashlib.sha1).hexdigest()


pickled_data = pickle.dumps(my_data)
digest = make_digest(pickled_data)
my_path = Path(".").joinpath("test.pickle")
print("my digest is ", digest)
header = '%s %s' % (digest, len(pickled_data))
blah = header + '\n'
with my_path.open("wb") as pickle_file:
    pickle_file.write(blah.encode())
    pickle_file.write(pickled_data)

with my_path.open("rb") as pickle_file:
    first_line = pickle_file.readline()
    print(first_line)
    incoming_digest, incoming_length = first_line.decode().split(' ')
    incoming_length = int(incoming_length)

    print ('\nREAD:', incoming_digest, incoming_length)

    incoming_pickled_data = pickle_file.read(incoming_length)

    actual_digest = make_digest(incoming_pickled_data)
    print ('ACTUAL:', actual_digest)

    pickle_data = pickle.loads(incoming_pickled_data)
    print(pickled_data["food"])

# test = make_digest("cheese".encode())
# print("test is ", test)
# print(hmac.digest(b'12345', test , hashlib.sha1))
