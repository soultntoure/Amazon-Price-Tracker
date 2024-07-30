import smtplib
import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

URL = "https://appbrewery.github.io/instant_pot/"
response = requests.get(URL)
contents = response.text

my_email = os.environ["EMAIL_ADDRESS"]
password = os.environ["EMAIL_PASSWORD"]

soup = BeautifulSoup(contents, "html.parser")
price = soup.find(name="span", class_="aok-offscreen").get_text()

price_without_symbol = float(price.replace("$",""))
print(price_without_symbol)




item_title = soup.find(id="productTitle").get_text().strip()
print(item_title)

if price_without_symbol < 100:
    
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:W price Alert!\n\n{item_title} is now ${price_without_symbol}\n{URL}".encode("utf-8")
        )
