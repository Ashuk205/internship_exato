import nltk
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
nltk.download('punkt')
problems = ["Transaction Discrepancy Email to Bank Customer Service: Subject: Discrepancy in Recent Transaction Dear [Bank Customer Service],I am writing to bring to your attention a discrepancy I have noticed in my recent transaction history. Upon reviewing my bank statement, I discovered an unauthorized transaction for [amount] on [date] that I did not authorize or recognize.I have attached a copy of my bank statement highlighting the transaction in question for your reference. I request your immediate assistance in investigating this matter and resolving the discrepancy as soon as possible.Additionally, I would appreciate a temporary hold on my account to prevent any further unauthorized transactions while the investigation is underway.Thank you for your prompt attention to this urgent matter.",
            "Dear [Bank Representative],I am writing to express my concern regarding a fund transfer that has been pending for [number of days]. I initiated a transfer of [amount] from my account ([account number]) to [recipient's account] on [date], but the funds have yet to be credited to the recipient's account.This delay is causing inconvenience and anxiety, especially as the transfer was intended for [reason, e.g., payment of bills, urgent expenses]. I kindly request your assistance in expediting the transfer process and ensuring the prompt crediting of funds to the intended recipient's account.Your urgent attention to this matter would be greatly appreciated.Thank you for your cooperation.",
            "Subject: Payment Error in Recent TransactionDear [Bank Manager],I am writing to report an error that occurred during a recent payment transaction conducted through my account ([account number]). On [date], I attempted to make a payment of [amount] to [payee's name or account], but the payment was not processed successfully.Upon reviewing my account activity, I noticed that the deducted amount was not credited to the payee's account, nor was it refunded to my account. This discrepancy has left me concerned about the status of the payment and its impact on my financial records.I kindly request your assistance in investigating this payment error and rectifying it at the earliest convenience. Please provide me with an update on the status of the payment and any necessary steps I need to take to resolve the issue.Thank you for your attention to this matter.",
            "Subject: Unable to Login to Online Banking Account Dear [Bank Customer Support],I am writing to seek assistance regarding an issue I am experiencing with accessing my online banking account. Despite entering the correct username and password, I am unable to log in successfully.This login issue is preventing me from accessing important banking services and managing my accounts online. I have attempted to reset my password multiple times using the Forgot Password option, but I have not received any reset instructions or emails.I kindly request your immediate attention to resolve this login problem and restore access to my online banking account as soon as possible. Please provide guidance on the necessary steps I should take to regain access or reset my password.Thank you for your prompt assistance in addressing this matter.",
            "Subject: Request for Password Reset Dear [Bank IT Department],I am reaching out to request assistance with resetting my password for online banking access. Due to security concerns, I recently updated my password, but unfortunately, I seem to have forgotten the new password.As a result, I am unable to access my online banking account to manage my finances and carry out essential transactions. I would appreciate it if you could initiate a password reset process for my account and provide instructions on how to set a new password securelPlease ensure that the password reset process is conducted promptly to minimize any disruption to my banking activities.Thank you for your attention to this matter.",
            "Subject: Assistance Required with Online Banking Services Dear [Bank Name] Customer Service,I hope this email finds you well. I am writing to seek assistance regarding several issues I am experiencing with my online banking services. Despite being a loyal customer for [duration], I am encountering difficulties with various aspects of my online banking experience.Login Issues: Unfortunately, I am unable to log in to my online banking account despite entering the correct username and password. This login problem is hindering my ability to access important banking services and perform transactions online.Password Reset: Furthermore, I recently attempted to reset my password due to security concerns. However, I did not receive any reset instructions or emails, leaving me unable to log in with the new password.Transaction Discrepancy: Additionally, I have noticed a discrepancy in my recent transaction history. An unauthorized transaction appears on my account, which I did not authorize or recognize. I am concerned about the security of my account and would appreciate a thorough investigation into this matter.Given the urgency of these issues, I kindly request your immediate attention to resolve them. Please provide guidance on how I can regain access to my online banking account, initiate a password reset process, and address the unauthorized transaction on my account.Your prompt assistance in resolving these issues is greatly appreciated. Please feel free to contact me at [your contact information] if further clarification or information is required.Thank you for your attention to this matter.",
            "I hope this message finds you well.I am writing to inform you that I encountered an error while attempting to transfer funds on [Date]. Could you please assist me in resolving this issue at your earliest convenience?Thank you for your prompt attention to this matter.",
            "I wanted to bring to your attention that I am currently experiencing difficulty connecting to the server. Despite several attempts, I have been unable to establish a connection.Could you please look into this matter and provide any guidance or assistance to help resolve the issue? Your prompt attention to this concern would be greatly appreciated.Thank you for your assistance.",
         "I trust this email finds you well.I am writing to bring to your attention a concern regarding my account. I have noticed that my account balance is not updating accurately despite recent transactions.Could you kindly investigate this matter and provide any necessary assistance to ensure that my account balance reflects the correct informationThank you very much for your attention to this matter I appreciate your prompt assistance in resolving this issue.Best regards I am utterly frustrated to report that I encountered a payment gateway timeout error while attempting to make a transaction on your platform. This is completely unacceptable and has resulted in significant inconvenience.I demand an immediate resolution to this issue. Such errors reflect poorly on your services and undermine my confidence in your platform. I expect swift action to rectify this problem without any further delays.Failure to address this matter promptly will force me to explore alternative options for my transactions.",
        "#iamfine.",
        "Thanks team , transaction successfull.",
]
categories = {
    'Transaction Issues': ['transaction', 'transfer', 'payment', 'funds'],
    'Login Problems': ['login', 'password', 'access'],
    'Account Access Issues': ['account', 'balance', 'locked', 'session'],
    'Server Connectivity': ['server', 'connect', 'timeout', 'maintenance'],
    'Other': ['error', 'unexpected'],
    'No error': ['transaction successfull']
}
 
df = pd.DataFrame(problems, columns=['Problem'])
 
# Add a column for the category labels
for category in categories.keys():
    df[category] = df['Problem'].apply(lambda x: any(keyword in x.lower() for keyword in categories[category]))
 
# Feature extraction
vectorizer = CountVectorizer(tokenizer=nltk.word_tokenize)
X = vectorizer.fit_transform(df['Problem'])
 

rf_classifier = RandomForestClassifier()
rf_classifier.fit(X, df.drop(columns=['Problem']))
 
print("Categorized Problems:")
for category in categories.keys():
    predicted = rf_classifier.predict(vectorizer.transform([problem for problem in problems]))
    count = sum(predicted[:, list(categories.keys()).index(category)])
    print(f"\n{category} Problems (Count: {count}):")
    for problem in problems:
        print(f" - {problem}")
