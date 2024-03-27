import requests
from bs4 import BeautifulSoup

# Define the URL for the Mafengwo travel page
url = "https://www.mafengwo.cn/jd/10065/gonglve.html"

# Send a GET request to the URL
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find the elements containing the attractions
attraction_elements = soup.find_all("div", class_="bd")

# Extract and print the details of attractions
for attraction in attraction_elements:
    attraction_link = attraction.find("a")["href"]
    attraction_name = attraction.find("a").text.strip()
    attraction_description = attraction.find("div", class_="summary").text.strip()
    print(f"Name: {attraction_name}")
    print(f"Description: {attraction_description}")
    print(f"URL: {attraction_link}")
    print()
