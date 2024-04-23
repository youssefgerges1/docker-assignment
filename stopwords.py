import nltk 
#nltk.download('punkt')
from collections import Counter
nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words =set(stopwords.words('english'))
#print(stop_words)
with open("paragraphs.txt", "r") as file:
    text = file.read().lower()

from nltk.tokenize import word_tokenize
Words = word_tokenize(text)


Words_without_stopwords=[]
for word in Words:
    if word not in stop_words:
        Words_without_stopwords.append(word)

word_counts = Counter(Words_without_stopwords)

# Display word frequency count
for word, count in word_counts.items():
    print(f"{word}: {count}")
