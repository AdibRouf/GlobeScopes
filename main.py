from bs4 import BeautifulSoup
import requests
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

#fetch google world news page
wrldnews = requests.get('https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US%3Aen')

#parse the page with BeautifulSoup
soup = BeautifulSoup(wrldnews.content, 'html.parser')


links = soup.find_all('a', class_='gPFEn')

# Extract captions from each headline
captions = [link.get_text(strip=True) for link in links]

keyword = input("Enter a word to filter captions by: ").lower()

# Filter captions that contain the keyword
filtered_captions = [caption for caption in captions if keyword in caption.lower()]

# Join captions into one string
text = ' '.join(filtered_captions)

# Define stopwords
custom_stopwords = STOPWORDS.union({'s', 'will', 'and', 'it'})  #Words to exclude from the word cloud

# Generate word cloud without filler words (stopwords)
if text:
    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color='white',
        stopwords=custom_stopwords
    ).generate(text)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(f"Word Cloud for Captions Containing: '{keyword}'")
    plt.show()
else:
    print("No captions found with that keyword.")