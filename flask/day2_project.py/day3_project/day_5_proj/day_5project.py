import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import string

# Download necessary NLTK data
nltk.download('punkt')

# Problem statements
problems = [
    "I am writing to report that my recent transaction failed during preprocessing. Please assist in resolving this issue as soon as possible. Thank you for your prompt attention.",
    "I am writing to report a payment gateway timeout error I encountered during a transaction. This issue is causing significant inconvenience. Please assist in resolving this matter promptly. Thank you for your swift attention.",
    "I am writing to inform you of an error I encountered while attempting to transfer funds. This issue needs urgent resolution. Thank you for your prompt assistance.",
    "I am writing to report an unexpected error that occurred during my recent transaction. Please assist in resolving this issue as soon as possible. Thank you for your prompt attention.",
    "I encountered an unexpected error during my recent transaction. Could you please assist in resolving this issue promptly? Thank you for your immediate attention.",
    "I am unable to access my bank account despite multiple attempts. Please assist in resolving this issue urgently. Thank you for your prompt attention.",
    "I am experiencing repeated failures when attempting to log in to my account. Please assist in resolving this issue as soon as possible. Thank you for your prompt attention.",
    "I am unable to access my account as the login page is not loading. Please assist in resolving this issue urgently. Thank you for your prompt attention.",
    "I am writing to report that my account balance is not updating despite recent transactions. Please assist in resolving this issue promptly. Thank you for your immediate attention.",
    "I am experiencing repeated issues with my session expiring unexpectedly. Please assist in resolving this matter promptly. Thank you for your immediate attention.",
    "My account has been locked due to suspected suspicious activity. Please assist in unlocking my account and resolving this issue as soon as possible. Thank you for your prompt attention.",
    "I am currently unable to connect to the server despite multiple attempts. Please assist in resolving this issue urgently. Thank you for your prompt attention.",
    "This is to inform you that our server will be down for scheduled maintenance from morning 6 am to evening 5 pm on tomorrow. During this period, our services will be temporarily unavailable. We apologize for any inconvenience caused and appreciate your understanding.",
    "#iamfine.",
    "#Thanks team, Now my work has been done successfully."
]

# Category mapping
categories = {
    'Transaction Issues': 'transaction',
    'Login Problems': 'login',
    'Account Access Issues': 'account',
    'Server Connectivity': 'server',
    'Other': 'error',
    'No error': 'successful'
}

# Preprocessing function
def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

# Preprocess all problem statements
problems_processed = [preprocess_text(text) for text in problems]

# Vectorizer
vectorizer = TfidfVectorizer(tokenizer=nltk.word_tokenize)
features = vectorizer.fit_transform(problems_processed)

# Category labels
category_labels = {cat: i for i, cat in enumerate(categories.keys())}
target_labels = [
    'Transaction Issues', 'Transaction Issues', 'Transaction Issues', 'Transaction Issues', 'Transaction Issues',
    'Login Problems', 'Login Problems', 'Login Problems', 'Account Access Issues', 'Account Access Issues',
    'Account Access Issues', 'Server Connectivity', 'Server Connectivity', 'Other', 'No error'
]
target_labels_numerical = [category_labels[cat] for cat in target_labels]

# Classifier
classifier = MultinomialNB()
classifier.fit(features, target_labels_numerical)

# Prediction function
def predict_category(text):
    text_processed = preprocess_text(text)
    text_features = vectorizer.transform([text_processed])
    predicted_category_index = classifier.predict(text_features)[0]
    return list(categories.keys())[predicted_category_index]

# Test predictions
for i, problem in enumerate(problems):
    predicted_category = predict_category(problem)
    print(f"Problem {i+1}: {problem}")
    print(f"Predicted Category: {predicted_category}\n")





# import nltk
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.naive_bayes import MultinomialNB
# import string

# # Download necessary NLTK data
# nltk.download('punkt')

# # Problem statements with more examples
# problems = [
#     "I am writing to report that my recent transaction failed during preprocessing. Please assist in resolving this issue as soon as possible. Thank you for your prompt attention.",
#     "I am writing to report a payment gateway timeout error I encountered during a transaction. This issue is causing significant inconvenience. Please assist in resolving this matter promptly. Thank you for your swift attention.",
#     "I am writing to inform you of an error I encountered while attempting to transfer funds. This issue needs urgent resolution. Thank you for your prompt assistance.",
#     "I am writing to report an unexpected error that occurred during my recent transaction. Please assist in resolving this issue as soon as possible. Thank you for your prompt attention.",
#     "I encountered an unexpected error during my recent transaction. Could you please assist in resolving this issue promptly? Thank you for your immediate attention.",
#     "I am unable to access my bank account despite multiple attempts. Please assist in resolving this issue urgently. Thank you for your prompt attention.",
#     "I am experiencing repeated failures when attempting to log in to my account. Please assist in resolving this issue as soon as possible. Thank you for your prompt attention.",
#     "I am unable to access my account as the login page is not loading. Please assist in resolving this issue urgently. Thank you for your prompt attention.",
#     "I am writing to report that my account balance is not updating despite recent transactions. Please assist in resolving this issue promptly. Thank you for your immediate attention.",
#     "I am experiencing repeated issues with my session expiring unexpectedly. Please assist in resolving this matter promptly. Thank you for your immediate attention.",
#     "My account has been locked due to suspected suspicious activity. Please assist in unlocking my account and resolving this issue as soon as possible. Thank you for your prompt attention.",
#     "I am currently unable to connect to the server despite multiple attempts. Please assist in resolving this issue urgently. Thank you for your prompt attention.",
#     "This is to inform you that our server will be down for scheduled maintenance from morning 6 am to evening 5 pm tomorrow. During this period, our services will be temporarily unavailable. We apologize for any inconvenience caused and appreciate your understanding.",
#     "#iamfine.",
#     "#Thanks team, Now my work has been done successfully."
# ]

# # Category mapping
# categories = {
#     'Transaction Issues': 'transaction',
#     'Login Problems': 'login',
#     'Account Access Issues': 'account',
#     'Server Connectivity': 'server',
#     'Other': 'other',
#     'No error': 'successful'
# }

# # Preprocessing function
# def preprocess_text(text):
#     text = text.lower()
#     text = text.translate(str.maketrans('', '', string.punctuation))
#     return text

# # Preprocess all problem statements
# problems_processed = [preprocess_text(text) for text in problems]

# # Vectorizer
# vectorizer = TfidfVectorizer(tokenizer=nltk.word_tokenize)
# features = vectorizer.fit_transform(problems_processed)

# # Category labels
# category_labels = {cat: i for i, cat in enumerate(categories.keys())}
# target_labels = [
#     'Transaction Issues', 'Transaction Issues', 'Transaction Issues', 'Transaction Issues', 'Transaction Issues',
#     'Login Problems', 'Login Problems', 'Login Problems', 'Account Access Issues', 'Account Access Issues',
#     'Account Access Issues', 'Server Connectivity', 'Other', 'Other', 'No error'
# ]
# target_labels_numerical = [category_labels[cat] for cat in target_labels]

# # Classifier
# classifier = MultinomialNB()
# classifier.fit(features, target_labels_numerical)

# # Prediction function
# def predict_category(text):
#     text_processed = preprocess_text(text)
#     text_features = vectorizer.transform([text_processed])
#     predicted_category_index = classifier.predict(text_features)[0]
#     return list(categories.keys())[predicted_category_index]

# # Test predictions
# for i, problem in enumerate(problems):
#     predicted_category = predict_category(problem)
#     print(f"Problem {i+1}: {problem}")
#     print(f"Predicted Category: {predicted_category}\n")
