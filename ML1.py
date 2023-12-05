import requests
from bs4 import BeautifulSoup
from textblob import TextBlob

def get_google_search_results(keyword):
    url = f'https://www.google.com/search?q={keyword}&num=10'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Error: {response.status_code}")
        return None

def extract_text_from_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    results = soup.find_all('div', class_='tF2Cxc')

    texts = []
    for result in results:
        text = result.get_text()
        texts.append(text)

    return texts

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity

    if sentiment > 0:
        return 'Positive'
    elif sentiment < 0:
        return 'Negative'
    else:
        return 'Neutral'

def main():
    keyword = input("Enter a keyword to analyze sentiment: ")
    html = get_google_search_results(keyword)

    if html:
        texts = extract_text_from_html(html)

        if texts:
            print("\nSentiment analysis for the keyword:", keyword)
            for i, text in enumerate(texts, start=1):
                sentiment = analyze_sentiment(text)
                print(f"{i}. Sentiment: {sentiment}")
                print(f"   Text: {text}\n")
        else:
            print("No search results found.")
    else:
        print("Failed to fetch search results.")

if __name__ == "__main__":
    main()
