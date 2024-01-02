import requests
from bs4 import BeautifulSoup
from googletrans import Translator

# URL of the web page to be translated
url = 'https://www.online-bijbel.nl/kortbegrip/overzicht/'

# Send a GET request to the URL and get the HTML content
response = requests.get(url)
html_content = response.content

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Extract the text content from the HTML
text = soup.get_text()

# Create a translator object
translator = Translator()

# Translate the text to English
translated_text = translator.translate(text, dest='en').text

# Print the translated text
print(translated_text)
