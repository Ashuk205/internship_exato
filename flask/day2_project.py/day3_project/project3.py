import nltk
from collections import defaultdict
nltk.download('punkt')
problems = [
    "I can't access my online banking account.",
    "My debit card was declined.",
    "The ATM ate my card.",
    "I need help with a wire transfer.",
    "There are unauthorized charges on my credit card.",
    "I can't reset my online banking password.",
    "I lost my debit card.",
    "I need to update my address.",
    "My mobile banking app keeps crashing.",
    "How do I apply for a mortgage?",
    "I have a question about my loan statement.",
    "My check deposit is not showing up in my account.",
    "I received an overdraft fee but I have money in my account."
]
categories = {
    'Online Banking': ['online banking', 'mobile banking', 'password', 'app', 'access'],
    'Card Issues': ['debit card', 'credit card', 'ATM', 'card', 'declined', 'lost'],
    'Transactions': ['wire transfer', 'transfer', 'deposit', 'withdrawal', 'charges', 'overdraft'],
    'Account Management': ['update my address', 'address', 'apply for a mortgage', 'mortgage', 'loan', 'statement'],
    'Fraud and Security': ['unauthorized', 'fraud', 'security']
}
def categorize_problems(problems, categories):
    categorized_problems = defaultdict(list)
    
    for problem in problems:
        categorized = False
        for category, keywords in categories.items():
            if any(keyword in problem.lower() for keyword in keywords):
                categorized_problems[category].append(problem)
                categorized = True
                break
        if not categorized:
            categorized_problems['Uncategorized'].append(problem)
    
    return categorized_problems
categorized_problems = categorize_problems(problems, categories)
for category, problems in categorized_problems.items():
    print(f"\n{category} Problems:")
    for problem in problems:
        print(f" - {problem}")
