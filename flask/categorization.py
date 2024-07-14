import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
 
# Download VADER lexicon and initialize the analyzer
nltk.download('vader_lexicon')
sid = SentimentIntensityAnalyzer()
def categorize_sentiment(text):
    # Analyze sentiment
    scores = sid.polarity_scores(text)
   
    # Determine sentiment category
    if scores['compound'] >= 0.05:
        return 'Positive'
    elif scores['compound'] <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'
 
# Example long text
long_text = """
Natural language processing (NLP) is a field of computer science, artificial intelligence, and computational linguistics
concerned with the interactions between computers and human (natural) languages. As such, NLP is related to the area of
human–computer interaction. Many challenges in NLP involve natural language understanding, that is, enabling computers to
derive meaning from human or natural language input, and others involve natural language generation.
"""

 
# Categorize sentiment of the long text
sentiment_category = categorize_sentiment(long_text)
print(f'Sentiment of the text: {sentiment_category}')