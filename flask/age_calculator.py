from datetime import datetime

def calculate_age(birthdate):
    today = datetime.today()
    birthdate = datetime.strptime(birthdate, '%Y-%m-%d')
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

if __name__ == "__main__":
    birthdate_input = input("Enter your birthdate (YYYY-MM-DD): ")
    age = calculate_age(birthdate_input)
    print(f"You are {age} years old.")
