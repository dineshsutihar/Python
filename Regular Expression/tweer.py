#Code to check the username of tweeter user and verify it 

url= input("URL: ").strip()
print(url)

'''
username=url.replace("https://twitter.com/","")
print(f"Username: {username}")

#After removing some bugs
username=url.removeprefix("https://twitter.com/")
print(f"Username: {username}")

'''

# new method using re package
import re

#username=re.sub(r"^(https?://)?(www\.)?twitter\.com/","",url)


if matches:=re.search(r"^(https?://)?(www\.)?twitter\.com/([a-z0-9_]+)$",url,re.IGNORECASE):

    print(f"Username: {matches.group(3)}")