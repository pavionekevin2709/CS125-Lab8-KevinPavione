from bs4 import BeautifulSoup
import time

# Load local HTML file
with open("sample.html", "r") as file:
    content = file.read()

# Parse HTML
soup = BeautifulSoup(content, "html.parser")

# Exercise 1: Find first h1
title = soup.find("h1")
print("Title:", title.text)

# Exercise 2: Find all list items
items = soup.find_all("li")
print("\nList Items:")
for item in items:
    print("-", item.text)

# Exercise 3: Get link
link = soup.find("a")
print("\nLink:", link.get("href"))

# Exercise 4: CSS Selectors
title_css = soup.select(".title")
print("\nCSS Selector Title:", title_css[0].text)

# Exercise 5: Simulate scraping delay
print("\nSimulating scraping with delay...")
for i in range(3):
    print("Scraping page", i+1)
    time.sleep(1)