import requests
from bs4 import BeautifulSoup

def website():
    url = input("Enter the URL to scrape: ")
    try:
        response = requests.get(url)
        response.raise_for_status()  
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        print(f"\nFound {len(paragraphs)} paragraphs:\n")
        with open("paragraphs.txt", "w", encoding="utf-8") as file:
            for i, para in enumerate(paragraphs, 1):
                text = para.get_text(strip=True)
                if text:
                    print(f"{i}. {text}\n")
                    file.write(f"{i}. {text}\n\n")
        print("Paragraphs saved to 'paragraphs.txt'")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
website()
