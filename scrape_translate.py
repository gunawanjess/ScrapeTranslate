import os
import requests
from bs4 import BeautifulSoup
from googletrans import Translator

# Define the base URL without the number
base_url = "https://www.online-bijbel.nl/kortbegrip/vraag/"

# Create an empty list to store the URLs
urls = []

# Loop through numbers 1 to 74
for i in range(1, 75):
    # Concatenate the base URL with the current number
    full_url = f"{base_url}{i}/"
    # Add the full URL to the list
    urls.append(full_url)

# Print the list of URLs (optional)
for url in urls:
    print(url)

def fetch_text_from_website(url):
    # Function to fetch text from a given website and extract text content
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        inhoud_div = soup.find("div", class_="inhoud")
        if inhoud_div:
            inhoud_text = inhoud_div.get_text()
            print(inhoud_text)
            return inhoud_text
        else:
            print("Failed to find the specified div in the website.")
            return ""
    else:
        print("Failed to fetch text from the website.")
        return ""

def translate_text(text):
    # Function to translate text using Google Translate API
    translator = Translator()
    translation = translator.translate(text, dest='en')  # Assuming translation to English
    return translation.text

def main():
    # Main function to orchestrate the process

    for i in range(1, 75):
        website_url = f"{base_url}{i}/"
        output_file = f"C:/GitHub/ScrapeTranslate/translations/translated_text_{i}.txt"  # Name and path of the output file

        # Ensure the directory exists
        os.makedirs(os.path.dirname(output_file), exist_ok=True)

        text = fetch_text_from_website(website_url)

        if text:
            translated_text = ""
            words = text.split()  # Split the text into words
            for j in range(0, len(words), 1000):
                chunk = " ".join(words[j:j+1000])
                translated_chunk = translate_text(chunk)
                translated_text += translated_chunk + "\n"
            
            with open(output_file, "w") as file:
                file.write(translated_text)
            print(f"Translation completed. Translated text saved to {output_file}")
        else:
            print(f"Translation process failed for URL {website_url}. Please check your internet connection and website URL.")

if __name__ == "__main__":
    main()
