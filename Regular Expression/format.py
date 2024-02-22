import re
name=input("Whats your name? ").strip() #input: Dinesh, Sutihar

# if "," in name:

#     last, first =name.split(", ")

# print(f"Hello, {name}")

#Alternative
matches=re.search(r"^(.+), (.+)$",name) 
if matches:
    last,first=matches.groups()
    name=f"{first} {last}"
print(f"Hello, {name}") #Output: Hello, Sutihar Dinesh