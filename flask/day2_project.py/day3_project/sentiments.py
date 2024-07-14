from textblob import TextBlob

def categorize_sentiment(text):
    sentiment = TextBlob(text).sentiment.polarity
    if sentiment > 0:
        return "Positive"
    elif sentiment < 0:
        return "Negative"
    else:
        return "Neutral"

texts = [
    """
    The transaction was successful. Another transaction failed due to insufficient funds.
    We had issues with the transaction processing. Some transactions were successful while others failed.
    The transaction process needs to be improved for better reliability.
    """,
    """
    The transaction was completed successfully. The amount was debited, and the recipient confirmed receipt.
    However, another transaction failed due to a network error. We need to investigate why the transaction failed.
    """,
    """
    I tried to make a transaction, but it failed without an error message. The transaction was unsuccessful.
    Despite multiple attempts, the transaction did not go through. On the other hand, some transactions were successful.
    """,
    """
    Several transactions failed today due to server issues. We had multiple successful transactions yesterday.
    The system needs an update to ensure all transactions are processed successfully.
    """,
    """
    The transaction was successful, and the funds were transferred instantly. However, there were a few failed transactions reported.
    Our team is looking into the reasons for the transaction failures.
    """,
    """
    The server crashed unexpectedly. Server performance needs improvement.
    There were multiple server downtimes last week. Server maintenance is scheduled for the weekend.
    We need better server uptime to ensure smooth operations.
    """,
    """
    The user interface is intuitive and easy to use. However, some users reported issues with the login process.
    User experience needs to be improved, especially for first-time users. We received feedback about the dashboard layout.
    The registration process was seamless but the password reset functionality failed.
    """,
    """
    I trust this email finds you well. I am writing to bring to your attention a concern regarding my account.
    I have noticed that my account balance is not updating accurately despite recent transactions. Could you kindly investigate this matter and provide any necessary assistance to ensure that my account balance reflects the correct information? Thank you very much for your attention to this matter. I appreciate your prompt assistance in resolving this issue. Best regards.
   
    I am utterly frustrated to report that I encountered a payment gateway timeout error while attempting to make a transaction on your platform.
    This is completely unacceptable and has resulted in significant inconvenience. I demand an immediate resolution to this issue.
    Such errors reflect poorly on your services and undermine my confidence in your platform. I expect swift action to rectify this problem without any further delays. Failure to address this matter promptly will force me to explore alternative options for my transactions.
    """,
    """
    The mobile app crashes frequently, especially when attempting to upload photos. Users have complained about slow loading times.
    There are frequent bugs that cause the app to freeze. The app update did not fix the crashing issues. We need to focus on app stability.
    """,
    """
    Our website has a poor loading speed, particularly on mobile devices. Customers have reported broken links on several pages.
    The SEO ranking of our website needs improvement. We need to enhance the website's performance to attract more visitors.
    """,
    """
    There is a significant delay in customer support responses. Customers are experiencing issues with the chat support system.
    The customer support team needs better training to handle queries efficiently. We received negative feedback about our support services.
    """,
    """
    I am facing issues with online banking. The mobile app frequently crashes when I try to make transactions.
    The account balance is not updating accurately after transactions. I have encountered errors while transferring funds.
    """,
    """
    There have been unauthorized transactions on my account. I did not receive any notification for these transactions.
    Customer service was unable to provide a satisfactory explanation for the unauthorized charges.
    """,
    """
    I am unable to access my account online. The website keeps showing errors when I try to log in.
    Despite multiple attempts, I cannot reset my password. There seems to be a technical issue with the online banking system.
    """,
    """
    My credit card statement contains unauthorized charges. I did not make these transactions and suspect fraud.
    I have contacted customer service, but they have not resolved the issue yet. I am concerned about the security of my account.
    """,
    """
    I received a phishing email pretending to be from the bank. The email requested sensitive information such as my account number and password.
    I did not provide any information, but I am concerned about the security of my account. The bank should take measures to prevent such scams.
    """,
    """
    The registration process is straightforward, but a few users faced issues while signing up. We need to ensure the registration process is flawless.
    Some users reported that they didn't receive the confirmation email during the registration process.
    """,
    """
    Users are finding it difficult to reset their passwords. The password reset link is not working for some users.
    We have received multiple complaints about the password reset process being too complicated.
    """,
    """
    Several links on the website are broken, leading to 404 errors. We need to fix these broken links to improve user experience.
    Customers have reported broken links on the checkout page and the product pages.
    """,
    """
    The chat support system is often unresponsive. Customers have reported long wait times when using the chat support.
    We need to improve our chat support system to handle more queries efficiently.
    """,
    """
    I noticed unauthorized transactions on my account last week. These transactions were not initiated by me.
    Despite contacting customer service, the unauthorized transactions have not been resolved.
    """,
    """
    I am worried about the security of my account after receiving multiple phishing emails.
    The bank needs to implement better security measures to protect customers from such scams.
    """,
    """
    I received a phishing email asking for my account details. This is concerning as it appears to be from the bank.
    Such phishing emails can lead to serious security issues. The bank must take action to prevent these emails.
    """
]

# Dictionary to hold categorized texts and their counts
categorized_texts = {
    "Positive": {"count": 0, "subcategories": {}},
    "Negative": {"count": 0, "subcategories": {}},
    "Neutral": {"count": 0, "subcategories": {}}
}

# Categorize the texts and count subcategories
for text in texts:
    sentiment_category = categorize_sentiment(text)
    categorized_texts[sentiment_category]["count"] += 1
    
    # Count subcategories within each sentiment category
    for line in text.split("\n"):
        line = line.strip()
        if line:
            for subcategory in categorized_texts[sentiment_category]["subcategories"]:
                if subcategory in line.lower():
                    categorized_texts[sentiment_category]["subcategories"][subcategory] += 1
                    break
            else:
                categorized_texts[sentiment_category]["subcategories"][line.lower()] = 1

# Output the categorized texts and their counts
print("Categorized Texts:")
for category, info in categorized_texts.items():
    print(f"{category}: {info['count']} texts")
    if info["subcategories"]:
        print("Subcategories:")
        for subcategory, count in info["subcategories"].items():
            print(f"  {subcategory}: {count}")
