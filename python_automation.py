from credentionals import mobile_number
from dotenv import load_dotenv
import requests
import schedule
import time
import os

load_dotenv()

# defining a function
def send_message():
    
    resp = requests.post('https://textbelt.com/text', {
        'phone': os.getenv("MOBILE_NUMBER"),
        'message': 'Hi, Good Morning',
        # to send text ::: remove "_test" from 'key'
        'key': 'textbelt_test'
    })
    
    print()
    print(resp.json())

# setting a schedule to run the function

#schedule.every().day.at('11:25').do(send_message)
schedule.every(10).seconds.do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)
    
