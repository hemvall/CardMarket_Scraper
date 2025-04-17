from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
import time

# Path to GeckoDriver (update with your actual path)
driver_path = 'D:\\'

# Set Firefox options (headless mode optional)
options = Options()
options.headless = True  # Set to False if you want to see the browser

# Initialize Selenium WebDriver for Firefox with GeckoDriver
service = Service(driver_path)
driver = webdriver.Firefox(service=service, options=options)

# Define the URL for Cardmarket Charizard search
url = "https://www.cardmarket.com/en/Pokemon/Products/Search?searchString=charizard"

# Open the webpage using Selenium
driver.get(url)

# Allow some time for the page to load
time.sleep(5)

# Find all the product containers on the page
products = driver.find_elements(By.CLASS_NAME, "product")

# Extract the price and card name for each product
charizard_cards = []

for product in products:
    # Get the card name
    name = product.find_element(By.CLASS_NAME, "product-name").text.strip()

    # Get the price (the lowest price shown on the page)
    try:
        price = product.find_element(By.CLASS_NAME, "product-price").text.strip()
    except:
        continue  # Skip if no price is found

    # Append card name and price to the list
    charizard_cards.append({
        "name": name,
        "price": price
    })

# Sort the cards by price (ascending order)
charizard_cards = sorted(charizard_cards, key=lambda x: float(x["price"].replace("€", "").replace(",", ".")))

# Display the cheapest Charizard cards
for card in charizard_cards:
    print(f"Card Name: {card['name']} - Price: {card['price']}")

# Close the browser window
driver.quit()
