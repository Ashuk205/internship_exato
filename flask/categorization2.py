import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

nltk.download('punkt')

problems = [
    "I am writing to report that my recent transaction failed during preprocessing. Please assist in resolving this issue as soon as possible.Thank you for your prompt attention.",
    "I am writing to report a payment gateway timeout error I encountered during a transaction. This issue is causing significant inconvenience. Please assist in resolving this matter promptly.Thank you for your swift attention.",
    "I am writing to inform you of an error I encountered while attempting to transfer funds. This issue needs urgent resolution.Thank you for your prompt assistance.",
    "I am writing to report an unexpected error that occurred during my recent transaction. Please assist in resolving this issue as soon as possible.Thank you for your prompt attention.",
    "I encountered an unexpected error during my recent transaction. Could you please assist in resolving this issue promptly?Thank you for your immediate attention.",
    "I am unable to access my bank account despite multiple attempts. Please assist in resolving this issue urgently.Thank you for your prompt attention.",
    "I am experiencing repeated failures when attempting to log in to my account. Please assist in resolving this issue as soon as possible.Thank you for your prompt attention.",
    "I am unable to access my account as the login page is not loading. Please assist in resolving this issue urgently.Thank you for your prompt attention.",
    "I am writing to report that my account balance is not updating despite recent transactions. Please assist in resolving this issue promptly.Thank you for your immediate attention.",
    "I am experiencing repeated issues with my session expiring unexpectedly. Please assist in resolving this matter promptly.Thank you for your immediate attention.",
    "My account has been locked due to suspected suspicious activity. Please assist in unlocking my account and resolving this issue as soon as possible.Thank you for your prompt attention.",
    "I am currently unable to connect to the server despite multiple attempts. Please assist in resolving this issue urgently.Thank you for your prompt attention.",
    "This is to inform you that our server will be down for scheduled maintenance from morning 6 am to evening 5 pm on tomorrow. During this period, our services will be temporarily unavailable.We apologize for any inconvenience caused and appreciate your understanding.",
    "#iamfine.",
    "Thanks team , Now my work has been done successfully."
    "Investigate and resolve recurring instances of delayed transaction processing within our banking system, impacting customer satisfaction and operational efficiency."
    "Identify and rectify the systemic issue causing transactions to fail without generating error messages in our banking system, leading to customer confusion and operational challenges.",
]

# Define categories
categories = {
    'Transaction Issues': 'transaction',
    'Login Problems': 'login',
    'Account Access Issues': 'account',
    'Server Connectivity': 'server',
    'Other': 'error',
    'No error': 'successful'  # Added 'No error' category here
}

# Preprocess text data (optional)
def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
    # Remove punctuation
    # ... (you can add other preprocessing steps if needed)
    return text

# Preprocess problems
problems_processed = [preprocess_text(text) for text in problems]

# Feature extraction using TF-IDF 
vectorizer = TfidfVectorizer(tokenizer=nltk.word_tokenize)
features = vectorizer.fit_transform(problems_processed)

# Create a mapping between category names and numerical labels
category_labels = {cat: i for i, cat in enumerate(categories.keys())}

# Define the correct category for each problem (assuming each problem has a corresponding category)
# For the sake of this example, we'll map problems to categories based on their descriptions
target_labels = [
    'Transaction Issues', 'Transaction Issues', 'Transaction Issues', 'Transaction Issues', 'Transaction Issues',
    'Login Problems', 'Login Problems', 'Login Problems', 'Account Access Issues', 'Account Access Issues',
    'Account Access Issues', 'Server Connectivity', 'Server Connectivity', 'Other', 'No error', 'Transaction Issues', 'No error'
]

# Convert category labels to numerical labels
target_labels_numerical = [category_labels[cat] for cat in target_labels]

# Train a Multinomial Naive Bayes classifier
classifier = MultinomialNB()
classifier.fit(features, target_labels_numerical)

# Function to predict category for a new problem
def predict_category(text):
    # Preprocess text
    text_processed = preprocess_text(text)
    # Convert text to feature vector
    text_features = vectorizer.transform([text_processed])
    # Predict category
    predicted_category_index = classifier.predict(text_features)[0]
    return list(categories.keys())[predicted_category_index]

# Test the classifier on the sample problems
for i, problem in enumerate(problems):
    predicted_category = predict_category(problem)
    print(f"Problem {i+1}: {problem}")
    print(f"Predicted Category: {predicted_category}\n")
