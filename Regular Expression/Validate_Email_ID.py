import re #Documtation: https://docs.python.org/3/library/re.html
 
email=input("What's your email? ").strip()#strip helps to remove all the whitespace from string.

# if re.search(r"^[^@]+@[^@]+\.com$",email):
#     print("Email id is Valid")
# else:
#     print("Invalid")


#New variance
# if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.com$",email):
#     print("Email id is Valid")
# else:
#     print("Invalid")


#Another Variance
if re.search(r"^\w+@\w+\.(com|edu|in|ac)$",email,re.IGNORECASE ):
    print("Email id is Valid")
else:
    print("Invalid")