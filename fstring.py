letter = "hey my name is {} and i am from {}"
Name="Ashutosh"
country="India"
print(letter.format(Name, country))
 
print(letter.format(country, Name))
print(f"hey my name is {Name} and i am from {country}") 