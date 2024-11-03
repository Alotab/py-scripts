import requests
from bs4 import BeautifulSoup

#URL to scrap data from
URL = 'https://www.python.org/blogs/'

#Send a GET request to the URL
response = requests.get(URL)

#Parse the webpage content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')


# Find all the blog titles on the page
titles = soup.find_all('h3', class_='event-title')


# Print each title found
for i, title in enumerate(titles, start=1):
    print(f"{i}. {title.text.strip()}")


# Save the titles to a file
with open('./WebScrabber/blog_title_file.txt', 'w') as file:
    for title in titles:
        file.write(title.text.strip() + '\n')