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

my_email = "sultankwt331@gmail.com"
password = "gzeyegedlshtpqah"

soup = BeautifulSoup(contents, "html.parser")
price = soup.find(name="span", class_="aok-offscreen").get_text()

price_without_symbol = float(price.replace("$",""))
print(price_without_symbol)




item_title = soup.find(id="productTitle").get_text().strip()
print(item_title)

if price_without_symbol < 100:
    
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(os.environ["EMAIL_ADDRESS"], os.environ["EMAIL_PASSWORD"])
        connection.sendmail(
            from_addr=os.environ["EMAIL_ADDRESS"],
            to_addrs=os.environ["EMAIL_ADDRESS"],
            msg=f"Subject:W price Alert!\n\n{item_title} is now ${price_without_symbol}\n{URL}".encode("utf-8")
        )
