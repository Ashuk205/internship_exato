a = input ("enter the number:")
print(f"multiplication table of {a} is :")
try:
  for i in range(1,11):
   print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e:
   print ("invalid input")
print("print some imp line of codes ")
print("End of program")       



